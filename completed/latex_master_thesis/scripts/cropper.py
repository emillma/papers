from pathlib import Path

# import cv2
import numpy as np
from PIL import Image
from PIL import ImageFile
import re

# ImageFile.LOAD_TRUNCATED_IMAGES = True
# matplotlib.use('QtAgg')

latex_dir = Path(__file__).parents[1]
figure_dir = latex_dir / "figures"

test_dir = latex_dir / "test"
test_dir.mkdir(exist_ok=True)

crop_done_path = Path(__file__).parent.joinpath("crop_done.txt")
crop_done_path.touch()


def arg_first_false(arr):
    return next(i for i, v in enumerate(arr) if not v)


done = str(crop_done_path.read_text()).split("\n")

ignore_hori = [".*crosstalk.*"]
ignore_vert = []
for fpath in figure_dir.glob("*"):
    if (
        not fpath.is_dir()
        and fpath.suffix in [".png", ".jpg"]
        # and str(fpath) not in done,
    ):
        print(fpath.name)
        img = np.array(Image.open(fpath))
        img = np.atleast_3d(img)[..., :3]
        img_iswhite = np.all(img > 250, axis=-1)

        if any(re.match(pat, str(fpath)) for pat in ignore_vert):
            vert_start = 0
            vert_end = None
        else:
            vert = np.all(img_iswhite, axis=1)
            vert_start = arg_first_false(vert)
            vert_end = vert.shape[0] - arg_first_false(vert[::-1])

        if any(re.match(pat, str(fpath)) for pat in ignore_hori):
            hori_start = 0
            hori_end = None
        else:
            hori = np.all(img_iswhite, axis=0)
            hori_start = arg_first_false(hori)
            hori_end = hori.shape[0] - arg_first_false(hori[::-1])

        cropped = img[vert_start:vert_end, hori_start:hori_end]
        out = test_dir / fpath.name
        Image.fromarray(cropped).save(out)
        with open(crop_done_path, "a") as crop_done_file:
            crop_done_file.write(str(fpath) + "\n")
