from pathlib import Path
import symforce as sf
from bal_loader import download_all, unpack_all, parse_all
import subprocess
import re
import numpy as np


def run(cmd: str):
    return subprocess.run(f"timeout 1000 {cmd}", shell=True, capture_output=True)


data_dir = Path(__file__).resolve().parent / "data"
download_all(data_dir)
unpack_all(data_dir)
parse_all(data_dir)

sci = r"\s*(-?\d+\.\d+e[+-]\d{2})"
dec = r"\s*(\d)+"
flt = r"\s*(\d+\.\d+)"
flt_or_sci = r"\s*((?:\d+\.\d+)|(?:\d+\.\d+e[+-]\d{2}))"


def run_gtsam(fpath: str) -> tuple[list[float], list[float]]:
    gtsam = "/include/gtsam/build/examples/SFMExample_bal {fpath} | ts -s %.s"
    gtsam_init_pat = re.compile(r"(.*?)\s*Initial error:\s*?(.*)")
    gtsam_pat = re.compile(f"{flt} newError: {flt_or_sci}")

    ret = run(gtsam.format(fpath=fpath))
    msg = ret.stdout.decode().strip()
    m0 = gtsam_init_pat.search(msg)
    times, errors = [float(m0[1])], [float(m0[2])]
    for match in gtsam_pat.finditer(msg):
        times.append(float(match[1]))
        errors.append(float(match[2]))
    return times, errors


ceres_common = "--num_iterations 200 --input {fpath}"


ceres_pat = re.compile(f"{dec}{sci * 6}{dec}{sci * 2}")


def run_ceres_cmd(ceres_cmd: str, fpath: str) -> tuple[list[float], list[float]]:
    ret = run(ceres_cmd.format(fpath=fpath))
    msg = ret.stdout.decode().strip()
    times, errors = [], []
    for match in ceres_pat.finditer(msg):
        times.append(float(match[10]))
        errors.append(float(match[2]))
    return times, errors


def run_ceres_cpu_cgnr(fpath: str) -> tuple[list[float], list[float]]:
    ceres_cpu = f"/include/ceres-solver/build/bin/bundle_adjuster --linear_solver cgnr {ceres_common}"
    return run_ceres_cmd(ceres_cpu, fpath)


def run_ceres_cpu_schur(fpath: str) -> tuple[list[float], list[float]]:
    ceres_cpu = f"/include/ceres-solver/build/bin/bundle_adjuster {ceres_common}"
    return run_ceres_cmd(ceres_cpu, fpath)


def run_ceres_cuda_cgnr(fpath: str) -> tuple[list[float], list[float]]:
    ceres_cuda = (
        "/include/ceres-solver/build/bin/bundle_adjuster "
        "--sparse_linear_algebra_library cuda_sparse "
        "--dense_linear_algebra_library cuda "
        "--linear_solver cgnr "
        f"{ceres_common}"
    )
    return run_ceres_cmd(ceres_cuda, fpath)


def run_ceres_cuda_schur(fpath: str) -> tuple[list[float], list[float]]:
    ceres_cuda = (
        "/include/ceres-solver/build/bin/bundle_adjuster "
        "--sparse_linear_algebra_library cuda_sparse "
        "--dense_linear_algebra_library cuda "
        f"{ceres_common}"
    )
    return run_ceres_cmd(ceres_cuda, fpath)


def run_caspar(
    fpath: str, pcg_iter: int, pcg_rel_tol: float
) -> tuple[list[float], list[float]]:
    caspar = (
        "python /workspaces/papers/caspar/perf/gen_and_run.py {fpath} "
        f"{pcg_iter} {pcg_rel_tol}"
    )
    pat = re.compile(f"score_best: {sci}.*?dt_tot: {flt}")
    ret = run(caspar.format(fpath=fpath))
    msg = ret.stdout.decode().strip()
    times, errors = [0.0], [float(re.search(f"score_init: {sci}", msg)[1])]
    for match in pat.finditer(msg):
        times.append(float(match[2]))
        errors.append(float(match[1]))
    return times, errors


def run_caspar_fast(fpath: str):
    return run_caspar(fpath, 5, 1e-2)


def run_caspar_slow(fpath: str):
    return run_caspar(fpath, 50, 1e-6)


res_dir = Path(__file__).parent / "results"
data_dir
fpath = Path("/workspaces/papers/caspar/perf/data/venice/problem-52-64053-pre.txt")
funcs: list = [
    run_gtsam,
    run_ceres_cpu_cgnr,
    run_ceres_cpu_schur,
    run_ceres_cuda_cgnr,
    run_ceres_cuda_schur,
    run_caspar_fast,
    run_caspar_slow,
]
for scene in data_dir.iterdir():
    problems = sorted(
        scene.glob("problem-*.txt"), key=lambda x: int(x.stem.split("-")[1])
    )
    for fpath in [problems[0], problems[-1]]:
        for func in funcs:
            file = (
                res_dir / fpath.parent.name / fpath.stem / str(func.__name__)
            ).with_suffix(".npz")
            if file.exists():
                continue
            file.parent.mkdir(parents=True, exist_ok=True)
            print(file.relative_to(res_dir))
            time, err = func(fpath)
            np.savez_compressed(file, time, err)
