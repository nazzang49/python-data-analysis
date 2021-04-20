# kaggle
# https://www.kaggle.com/ronitf/heart-disease-uci

import pandas as pd
import plotly.graph_objects as go
import cufflinks as cf
cf.go_offline(connected=True)

df = pd.read_csv('../data/heart.csv', encoding='utf-8-sig')

print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.info())
print(df.isnull().sum())

# check feature type
print(df.describe())

# sex
fig = go.Figure()
fig.add_trace(
    go.Bar(
        y=df['sex'].value_counts()
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>SEX</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>SEX</b>"
        },
        "yaxis": {
            "title": "<b>COUNT</b>"
        }
    }
)
fig.show()

# cp
fig = go.Figure()
fig.add_trace(
    go.Bar(
        y=df['cp'].value_counts()
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>CP</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>CP</b>"
        },
        "yaxis": {
            "title": "<b>COUNT</b>"
        }
    }
)
fig.show()

# fbs
fig = go.Figure()
fig.add_trace(
    go.Bar(
        y=df['fbs'].value_counts()
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>FBS</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>FBS</b>"
        },
        "yaxis": {
            "title": "<b>COUNT</b>"
        }
    }
)
fig.show()

# restecg
fig = go.Figure()
fig.add_trace(
    go.Bar(
        y=df['restecg'].value_counts()
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>RESTECG</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>RESTECG</b>"
        },
        "yaxis": {
            "title": "<b>COUNT</b>"
        }
    }
)
fig.show()

# age
fig = go.Figure()
fig.add_trace(
    go.Box(
        y=df['age']
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>AGE</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>AGE</b>"
        }
    }
)
fig.show()

# trestbps
fig = go.Figure()
fig.add_trace(
    go.Box(
        y=df['trestbps']
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>TRESTBPS</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>TRESTBPS</b>"
        }
    }
)
fig.show()

# chol
fig = go.Figure()
fig.add_trace(
    go.Box(
        y=df['chol']
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>CHOL</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>CHOL</b>"
        }
    }
)
fig.show()

# thalach
fig = go.Figure()
fig.add_trace(
    go.Histogram(
        x=df['thalach']
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>THALACH</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>THALACH</b>"
        }
    }
)
fig.show()

# correlation
df_corr = df.corr()
df_corr.iplot(kind='heatmap', colorscale='ylorrd')

# age - trestbps
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['trestbps'],
        y=df['age'],
        mode='markers'
    )
)
fig.update_layout(
    {
        "title": {
            "text": "<b>AGE - TRESTBPS</b>",
            "font": {
                "size": 15
            }
        },
        "xaxis": {
            "title": "<b>TRESTBPS</b>"
        },
        "yaxis": {
            "title": "<b>AGE</b>"
        }
    }
)
fig.show()

