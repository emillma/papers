import numpy as np

a = np.arange(160)

out = np.zeros((32, 11), dtype=int)
out[:, 0] = np.arange(32)
out[:, 1:6] = a.reshape((32, 5))
out[:, -5:] = a.reshape((5, 32)).T
values = "\\\\\n".join(
    [f"{r[0]}&" + "&".join(f"$d_{{{c}}}$" for c in r[1:]) for r in out]
)
out_str = f"""

{values}

"""
print(out_str)
