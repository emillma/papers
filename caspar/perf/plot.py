import plotly.graph_objects as go
from pathlib import Path
import numpy as np

# Directory containing the .npz files
prob_dir = Path("/workspaces/papers/caspar/perf/results/ladybug/problem-49-7776-pre")

# Lists to store time and error values
names = []
times = []
errors = []
fig = go.Figure()

# Iterate over each .npz file in the directory
for npz_file in prob_dir.iterdir():
    time, err = np.load(npz_file).values()
    fig.add_trace(
        go.Scatter(
            x=time - time[0] + 1e-2,
            y=err,
            mode="lines+markers",
            name=npz_file.stem[4:],
        )
    )

fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.show()
