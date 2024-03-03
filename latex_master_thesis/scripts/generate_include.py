from pathlib import Path

root_dir = Path(__file__).parents[1]
chap_dir = root_dir / "chapters"
index_name = "__include__.tex"
todo_dir = [chap_dir]


def make_index_file(dir_: Path):
    files = [p.relative_to(root_dir) for p in sorted(dir_.rglob("*[!_][!_].tex"))]
    (dir_ / index_name).write_text("\n".join(r"\input{" + str(f) + "}" for f in files))


out = ""
for d in sorted([p for p in chap_dir.iterdir() if p.is_dir()]):
    make_index_file(d)
    out += r"\include{" + str(d.relative_to(root_dir)) + r"/" + index_name + "}\n"
chap_dir.joinpath(index_name).write_text(out)
