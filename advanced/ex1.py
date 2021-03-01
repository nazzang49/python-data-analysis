import numpy as np
import pandas as pd
import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)

rand1 = np.random.rand(5)
rand2 = np.random.rand(5, 2)
print(rand1)
print(rand2)

# make df by numpy array
df = pd.DataFrame(np.random.rand(10, 2), columns=["A", "B"])
print(df)

# all kinds of graphs => if you want to check manual in detail, utilize this help function
# print(cf.help())
# print(cf.help("bar"))

df.iplot(kind="bar")
