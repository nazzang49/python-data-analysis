# numeric data => 범위 확인

import pandas as pd
import plotly.graph_objects as go
import cufflinks as cf

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6],
    'C': [1, 2, 3, 4, 5, 100]
})
print(df.head())

# check data range
print(df.describe())

# check data range by iplot
cf.go_offline(connected=True)
print(cf.help())

# iplot in pycharm
fig = go.Figure()
fig.add_trace(
    go.Box(
        y=df['A'], name='A'
    )
)

fig.add_trace(
    go.Box(
        y=df['C'], name='C'
    )
)
fig.show()