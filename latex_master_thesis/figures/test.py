from pathlib import Path
from PIL import Image

from PIL import Image
import numpy as np
from scipy.signal import correlate2d

thisdir = Path(__file__).parent


img1 = np.array(Image.open(thisdir / "idp1.png")).astype(np.float32)[..., 1]
img2 = np.array(Image.open(thisdir / "idp2.png")).astype(np.float32)[..., 1]
corr = correlate2d(img1, img2, mode="same")
here = True
