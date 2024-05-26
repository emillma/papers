import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(description='Stuff')
parser.add_argument('--text')
args = parser.parse_args()
print(args)

# shutil.move(Path.cwd().joinpath('hello.txt').write_text('hello')
