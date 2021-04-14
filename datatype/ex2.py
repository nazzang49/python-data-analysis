# numeric data => 분포 확인

import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame(np.random.rand(100000, 1), columns=['A'])
df.head()

fig = go.Figure()
fig.add_trace(
    go.Histogram(
        x=df['A'],
        name='A',
        xbins=dict(
            start=0,
            end=1.0,
            size=0.05),
        marker_color='#F50057'
    )
)

fig.update_layout(
    title_text='Sampled Results',
    xaxis_title_text='Value',
    yaxis_title_text='Count',
    bargap=0.1,
)
fig.show()

