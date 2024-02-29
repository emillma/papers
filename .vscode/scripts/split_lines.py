from pathlib import Path
import sys
import re

file = Path(sys.argv[1])
text = file.read_text()
out = re.sub(r"\. (?!\n)", r". \n", text)
file.write_text(out)
