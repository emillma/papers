import sympy as sp
from sympy import Matrix
import symforce as sf
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from pathlib import Path


n_air = sp.symbols("\\eta_a", real=True, positive=True)
n_water = sp.symbols("\\eta_w", real=True, positive=True)

a_air = sp.symbols("\\theta_i", real=True, positive=True)
# a_water = sp.symbols("theta_r", real=True, positive=True)
# a_water_f = sp.asin(sp.sin(a_air) * n_air / n_water)
# n_water_f = (n_air * sp.sin(a_air)) / sp.sin(a_water)
a_water = sp.asin(sp.sin(a_air) * n_air / n_water)
vals = {
    n_air: 1,
    n_water: 1.33,
}


r_s = (n_air * sp.cos(a_air) - n_water * sp.cos(a_water)) / (
    n_air * sp.cos(a_air) + n_water * sp.cos(a_water)
)
r_p = (n_water * sp.cos(a_air) - n_air * sp.cos(a_water)) / (
    n_water * sp.cos(a_air) + n_air * sp.cos(a_water)
)

R_p = sp.simplify(r_p**2).subs(vals.items())
R_s = sp.simplify(r_s**2).subs(vals.items())

R_p_lamb = sp.lambdify(a_air, R_p)
R_s_lamb = sp.lambdify(a_air, R_s)

dolp = sp.simplify((R_s - R_p) / (R_s + R_p))
dolp_lamb = sp.lambdify(a_air, dolp)

# x = np.linspace(0, 100, 300)
a = np.linspace(0, np.pi / 2, 100)
brewster = np.arctan(1.33 / 1)


plt.rcParams.update(
    {
        "text.usetex": True,
        # "font.family": "Helvetica",
        "font.size": 14,
    }
)

fig0, ax0 = plt.subplots(figsize=(6, 3))
ax0.plot(np.rad2deg(a), R_s_lamb(a), c="#c92a2a", label="$R_\\perp$")
ax0.plot(np.rad2deg(a), R_p_lamb(a), c="#365fc7", label="$R_\\parallel$")
ax0.axvline(
    np.rad2deg(brewster),
    c="#2b8a3e",
    linestyle="-",
    alpha=0.8,
    label=f"$\\theta_B={np.rad2deg(brewster):.2f}^\\circ$",
)
ax0.set_xlabel("$\\theta_1$(deg)")
ax0.set_ylabel("Reflectance")
ax0.grid()
ax0.legend()

fig1, ax1 = plt.subplots(figsize=(6, 3))
ax1.plot(np.rad2deg(a), dolp_lamb(a), c="#365fc7", label="$DoLP$")
ax1.axvline(
    np.rad2deg(brewster),
    c="#2b8a3e",
    linestyle="-",
    alpha=0.8,
    label=f"$\\theta_B={np.rad2deg(brewster):.2f}^\\circ$",
)
ax1.set_xlabel("$\\theta_1$(deg)")
ax1.set_ylabel("$DoLP$")
ax1.grid()
ax1.legend()

dist = np.linspace(0, 30, 400)
a2 = np.arctan(dist)

fig2, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(dist, dolp_lamb(a2), c="#365fc7", label="$DoLP(\\theta_1)$")
ax2.axvline(
    np.tan(brewster),
    c="#2b8a3e",
    linestyle="-",
    alpha=0.8,
    label=f"$d_B=tan(\\theta_B)={np.tan(brewster):.2f}$",
)
ax2.set_xlabel("$d = tan(\\theta_1)$")
ax2.set_ylabel("DoLP")
ax2.grid()
ax2.legend()


# ax.plot(x, s**2 / (s**2 + p**2), label="p")
fig0.savefig(Path(__file__).parent / "brewster0.pdf", bbox_inches="tight")
fig1.savefig(Path(__file__).parent / "brewster1.pdf", bbox_inches="tight")
fig2.savefig(Path(__file__).parent / "brewster2.pdf", bbox_inches="tight")
