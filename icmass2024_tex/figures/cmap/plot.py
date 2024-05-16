import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from map import get_color
from matplotlib import rc

plt.rcParams.update(
    {
        "text.usetex": True,
        "font.size": 14,
        "font.family": "Helvetica",
        "pdf.fonttype": 42,
    }
)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(projection="polar"))
ax: plt.Axes
# ax = Axes3D(fig)
dolp = np.linspace(0, 1, 100)
aolp = np.linspace(0, 2 * np.pi, 100)
dolps, aolps = np.meshgrid(dolp, aolp)
rgb = get_color(aolps / np.pi, dolps)

# ax.subplot(projection="polar")

pcol = plt.pcolormesh(aolps, dolps, rgb, rasterized=True)

ax.plot(aolp, dolps, color="k", ls="none")
ax.grid()
label_position = ax.get_rlabel_position()

# ax.text(
#     np.radians(label_position),
#     ax.get_rmax() / 2.0,
#     "My label",
#     rotation=label_position,
#     ha="center",
#     va="center",
# )
ax.set_yticks([])
ax.set_xticks(np.arange(4) * np.pi / 2)
ax.set_xticklabels([f"${i}^\circ$" for i in [0, 90, 180, 270]])
plt.savefig(
    Path(__file__).parent / "plot.pdf",
    bbox_inches="tight",
)
