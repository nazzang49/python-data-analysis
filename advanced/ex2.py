import numpy as np
import pandas as pd
import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)

df = pd.DataFrame(np.random.rand(10, 2), columns=["A", "B"])
# cf.help("bar")
# cf.help("scatter")

# check options
df.iplot(kind="bar", barmode="stack")
df.iplot(kind="scatter", mode="lines+markers", fill=True, xTitle="X", yTitle="Y", title="제목")

themes = cf.getThemes()
themes

# color theme
# for t in themes:
#     df.iplot(kind="scatter", mode="lines+markers", fill=True, xTitle="X", yTitle="Y", title=t, theme=t)

layout = {
    'title': 
        {
            'text':'<b>Test Graph by Dave Lee</b>',
            'font': {
                'size': 15,
                'color': '#37474F'
            },
            'x': 0.5,
            'y': 0.88

        },
    'plot_bgcolor': '#FAFAFA',
    'xaxis': {
        'showticklabels':True,
        'dtick': 2,
        'title': {
            'text':'X axis',
            'font': {
                    'size': 10,
                    'color': '#37474F'
                }
            },
        "gridcolor": "yellow"
    },
    'yaxis': {
        'showticklabels':True,
        'dtick': 0.1,
        'title': {
            'text':'Y axis',
            'font': {
                    'size': 10,
                    'color': '#37474F'
                }
            },
        "gridcolor": "green"
    }    
}
df.iplot(kind='scatter', mode='lines+markers', layout=layout)