from pathlib import Path

root_dir = Path(__file__).parents[1]
chap_dir = root_dir / "chapters"
index_name = "__include__.tex"
todo_dir = [chap_dir]


out = ""
for d in sorted([p for p in chap_dir.iterdir() if p.is_dir()]):
    files = [p for p in sorted(d.glob("[!_][!_]*.tex"))]
    print(files)
    start = (
        "Improve the following chapters without changing any Latex specific commands"
        " like \\gls{js};\n\n"
    )
    text = start + "\n\n".join(f.read_text() for f in files)

    # d.joinpath("__all__.tex").write_text(text)
    d.joinpath("__all__.tex").unlink()
# chap_dir.joinpath(index_name).write_text(out)
