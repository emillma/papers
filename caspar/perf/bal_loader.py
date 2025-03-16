# ----------------------------------------------------------------------------
# SymForce - Copyright 2025, Skydio, Inc.
# This source code is under the Apache 2.0 license found in the LICENSE file.
# ----------------------------------------------------------------------------

from __future__ import annotations

import typing as T
from pathlib import Path
from urllib import request
from tqdm import tqdm
import numpy as np

import symforce.symbolic as sf
from bz2 import decompress

datasets = [
    "ladybug/problem-49-7776-pre.txt.bz2",
    "ladybug/problem-73-11032-pre.txt.bz2",
    "ladybug/problem-138-19878-pre.txt.bz2",
    "ladybug/problem-318-41628-pre.txt.bz2",
    "ladybug/problem-372-47423-pre.txt.bz2",
    "ladybug/problem-412-52215-pre.txt.bz2",
    "ladybug/problem-460-56811-pre.txt.bz2",
    "ladybug/problem-539-65220-pre.txt.bz2",
    "ladybug/problem-598-69218-pre.txt.bz2",
    "ladybug/problem-646-73584-pre.txt.bz2",
    "ladybug/problem-707-78455-pre.txt.bz2",
    "ladybug/problem-783-84444-pre.txt.bz2",
    "ladybug/problem-810-88814-pre.txt.bz2",
    "ladybug/problem-856-93344-pre.txt.bz2",
    "ladybug/problem-885-97473-pre.txt.bz2",
    "ladybug/problem-931-102699-pre.txt.bz2",
    "ladybug/problem-969-105826-pre.txt.bz2",
    "ladybug/problem-1031-110968-pre.txt.bz2",
    "ladybug/problem-1064-113655-pre.txt.bz2",
    "ladybug/problem-1118-118384-pre.txt.bz2",
    "ladybug/problem-1152-122269-pre.txt.bz2",
    "ladybug/problem-1197-126327-pre.txt.bz2",
    "ladybug/problem-1235-129634-pre.txt.bz2",
    "ladybug/problem-1266-132593-pre.txt.bz2",
    "ladybug/problem-1340-137079-pre.txt.bz2",
    "ladybug/problem-1469-145199-pre.txt.bz2",
    "ladybug/problem-1514-147317-pre.txt.bz2",
    "ladybug/problem-1587-150845-pre.txt.bz2",
    "ladybug/problem-1642-153820-pre.txt.bz2",
    "ladybug/problem-1695-155710-pre.txt.bz2",
    "ladybug/problem-1723-156502-pre.txt.bz2",
    "trafalgar/problem-21-11315-pre.txt.bz2",
    "trafalgar/problem-39-18060-pre.txt.bz2",
    "trafalgar/problem-50-20431-pre.txt.bz2",
    "trafalgar/problem-126-40037-pre.txt.bz2",
    "trafalgar/problem-138-44033-pre.txt.bz2",
    "trafalgar/problem-161-48126-pre.txt.bz2",
    "trafalgar/problem-170-49267-pre.txt.bz2",
    "trafalgar/problem-174-50489-pre.txt.bz2",
    "trafalgar/problem-193-53101-pre.txt.bz2",
    "trafalgar/problem-201-54427-pre.txt.bz2",
    "trafalgar/problem-206-54562-pre.txt.bz2",
    "trafalgar/problem-215-55910-pre.txt.bz2",
    "trafalgar/problem-225-57665-pre.txt.bz2",
    "trafalgar/problem-257-65132-pre.txt.bz2",
    "dubrovnik/problem-16-22106-pre.txt.bz2",
    "dubrovnik/problem-88-64298-pre.txt.bz2",
    "dubrovnik/problem-135-90642-pre.txt.bz2",
    "dubrovnik/problem-142-93602-pre.txt.bz2",
    "dubrovnik/problem-150-95821-pre.txt.bz2",
    "dubrovnik/problem-161-103832-pre.txt.bz2",
    "dubrovnik/problem-173-111908-pre.txt.bz2",
    "dubrovnik/problem-182-116770-pre.txt.bz2",
    "dubrovnik/problem-202-132796-pre.txt.bz2",
    "dubrovnik/problem-237-154414-pre.txt.bz2",
    "dubrovnik/problem-253-163691-pre.txt.bz2",
    "dubrovnik/problem-262-169354-pre.txt.bz2",
    "dubrovnik/problem-273-176305-pre.txt.bz2",
    "dubrovnik/problem-287-182023-pre.txt.bz2",
    "dubrovnik/problem-308-195089-pre.txt.bz2",
    "dubrovnik/problem-356-226730-pre.txt.bz2",
    "venice/problem-52-64053-pre.txt.bz2",
    "venice/problem-89-110973-pre.txt.bz2",
    "venice/problem-245-198739-pre.txt.bz2",
    "venice/problem-427-310384-pre.txt.bz2",
    "venice/problem-744-543562-pre.txt.bz2",
    "venice/problem-951-708276-pre.txt.bz2",
    "venice/problem-1102-780462-pre.txt.bz2",
    "venice/problem-1158-802917-pre.txt.bz2",
    "venice/problem-1184-816583-pre.txt.bz2",
    "venice/problem-1238-843534-pre.txt.bz2",
    "venice/problem-1288-866452-pre.txt.bz2",
    "venice/problem-1350-894716-pre.txt.bz2",
    "venice/problem-1408-912229-pre.txt.bz2",
    "venice/problem-1425-916895-pre.txt.bz2",
    "venice/problem-1473-930345-pre.txt.bz2",
    "venice/problem-1490-935273-pre.txt.bz2",
    "venice/problem-1521-939551-pre.txt.bz2",
    "venice/problem-1544-942409-pre.txt.bz2",
    "venice/problem-1638-976803-pre.txt.bz2",
    "venice/problem-1666-983911-pre.txt.bz2",
    "venice/problem-1672-986962-pre.txt.bz2",
    "venice/problem-1681-983415-pre.txt.bz2",
    "venice/problem-1682-983268-pre.txt.bz2",
    "venice/problem-1684-983269-pre.txt.bz2",
    "venice/problem-1695-984689-pre.txt.bz2",
    "venice/problem-1696-984816-pre.txt.bz2",
    "venice/problem-1706-985529-pre.txt.bz2",
    "venice/problem-1776-993909-pre.txt.bz2",
    "venice/problem-1778-993923-pre.txt.bz2",
    "final/problem-93-61203-pre.txt.bz2",
    "final/problem-394-100368-pre.txt.bz2",
    "final/problem-871-527480-pre.txt.bz2",
    "final/problem-961-187103-pre.txt.bz2",
    "final/problem-1936-649673-pre.txt.bz2",
    "final/problem-3068-310854-pre.txt.bz2",
    "final/problem-4585-1324582-pre.txt.bz2",
    "final/problem-13682-4456117-pre.txt.bz2",
]


def download_all(out_dir: Path = Path(__file__).resolve().parent / "data") -> None:
    pre = "https://grail.cs.washington.edu/projects/bal/data"
    for name in datasets:
        fpath = out_dir / name
        fpath.parent.mkdir(exist_ok=True, parents=True)
        if fpath.exists():
            continue
        request.urlretrieve(f"{pre}/{name}", fpath)


def unpack_all(out_dir: Path = Path(__file__).resolve().parent / "data") -> None:
    for name in out_dir.rglob("*.bz2"):
        if not (txt_file := name.with_name(name.stem)).is_file():
            txt_file.write_bytes(decompress(name.read_bytes()))


def load_bal(
    fpath: Path | str,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    fpath = Path(fpath)
    assert fpath.is_file()

    if not (npz_path := fpath.with_suffix(".npz")).is_file():
        print("Loading data... (this may take a while the first time)")
        print(npz_path)

        def load(
            file: Path,
            typ: T.Type[np.number[T.Any]],
            start: int,
            nrows: int,
            cols: int | T.Sequence[int] | None = None,
        ) -> np.ndarray:
            return np.loadtxt(file, typ, skiprows=start, max_rows=nrows, usecols=cols)  # type: ignore[arg-type]

        n_cams, n_points, n_facs = load(fpath, np.int32, 0, 1)
        cam_ids, point_ids = np.ascontiguousarray(
            load(fpath, np.int32, 1, n_facs, (0, 1)).T
        )
        pixels = load(fpath, np.float32, 1, n_facs, (2, 3))
        camdata_tangent = load(fpath, np.float32, 1 + n_facs, n_cams * 9)
        camdata_tangent = camdata_tangent.reshape(n_cams, 9)
        camdata: np.ndarray = np.array(
            [
                [
                    *sf.Pose3(sf.Rot3.from_tangent(d[:3]), sf.V3(d[3:6])).to_storage(),
                    *d[6:],
                ]
                for d in camdata_tangent.astype(float)
            ],
            dtype=np.float32,
        )
        points = load(fpath, np.float32, 1 + n_facs + n_cams * 9, n_points * 3)
        points = points.reshape(n_points, 3)

        np.savez_compressed(npz_path, cam_ids, point_ids, camdata, points, pixels)
    else:
        data = np.load(npz_path, allow_pickle=False)
        cam_ids, point_ids, camdata, points, pixels = data.values()
    return cam_ids, point_ids, camdata, points, pixels


def parse_all(out_dir: Path = Path(__file__).resolve().parent / "data") -> None:
    for name in out_dir.rglob("*.txt"):
        if not (npz_path := name.with_suffix(".npz")).is_file():
            load_bal(name)
