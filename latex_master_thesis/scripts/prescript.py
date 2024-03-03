import argparse
from pathlib import Path


parser = argparse.ArgumentParser(description="Stuff")
parser.add_argument("--text")
args = parser.parse_args()
print(args)
# Path.cwd().joinpath('hello.txt').write_text('hello')
