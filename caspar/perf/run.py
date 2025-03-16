from pathlib import Path
import symforce as sf
from bal_loader import download_all, unpack_all, parse_all

data_dir = Path(__file__).resolve().parent / "data"
download_all(data_dir)
unpack_all(data_dir)
parse_all(data_dir)

print("Done!")
