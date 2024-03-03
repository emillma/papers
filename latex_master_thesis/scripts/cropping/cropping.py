from PIL import Image
from pathlib import Path
import numpy as np

thisdir = Path(__file__).parent


slices = [
    (slice(755, 790), slice(725, 800)),
    (slice(700, 735), slice(1020, 1095)),
    (slice(200, 260), slice(1100, 1170)),
    (slice(430, 450), slice(666, 716)),
    (slice(660, 760), slice(270, 440)),
]
for name in ["regular_right_96", "aolp_right_96"]:
    file = thisdir / f"{name}.jpeg"
    img = Image.open(file)
    array = np.array(img)
    for sl_idx, sl in enumerate(slices):
        crop = array[sl]
        # draw a rectangle on the original image
        array[sl[0].start - 1, sl[1]] = 255
        array[sl[0].stop, sl[1]] = 255
        array[sl[0], sl[1].start - 1] = 255
        array[sl[0], sl[1].stop] = 255

        Image.fromarray(crop).save(thisdir / f"{name}_cropped_{sl_idx}.png")
    Image.fromarray(array).save(thisdir / f"{name}_marked.png")
