import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo
pyo.init_notebook_mode()

df = pd.DataFrame(np.random.rand(10, 2), columns=["A", "B"])

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df.index, y=df['A']
    )
)

fig.update_layout(
    {
        "title": {
            "text": "<b>Graph with go.Scatter</b>",
            "font": {
                "size": 15
            }
        },
        "showlegend": True,
        "xaxis": {
            "title": "<b>random number</b>"
        },
        "yaxis": {
            "title": "<b>A</b>"
        }
    }
)

fig.show()