# categorical data

import pandas as pd
import plotly.graph_objects as go
import cufflinks as cf
cf.go_offline(connected=True)

data = {
    'year': ['2017', '2017', '2019', '2020', '2021', '2021'],
    'grade': ['C', 'C', 'B', 'A', 'B', 'E'],
}

df = pd.DataFrame(data)
print(df)

df1 = df.groupby("grade").count()
df2 = df.groupby("year").count()

print(df1)
print(df2)

print(df['year'].value_counts())
print(df['grade'].value_counts())

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=df1.index, y=df1['year'], name='A'
    )
)

fig.show()

df1 = df1.reset_index()
fig = go.Figure()
fig.add_trace(
    go.Pie(
        labels=df1['grade'], values=df1['year']
    )
)

fig.show()