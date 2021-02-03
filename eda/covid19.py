# EDA about covid19
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# data from https://github.com/CSSEGISandData/COVID-19/tree/master/who_covid_19_situation_reports
path = "../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
df = pd.read_csv(path + "04-01-2020.csv",
                 delimiter=",",
                 encoding="utf-8")

# 1 - check data
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)

# 2 - analyze feature
# check column
print(df.columns)

# check detail info => mean, min, max, std, count
print(df.describe())

# check correlation among features by pearson coefficient => default
# ref from https://umbum.dev/1006?category=751025
print(df.corr())

# visualize by seaborn
fig, ax = plt.subplots(figsize=(9, 9))

# remove reduplication
mask = np.zeros_like(df.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# RdYlBu_r => red, yellow, blue
# annot => real value
# vmin => not relational
# vmax => relational
sns.heatmap(df.corr(),
            cmap="RdYlBu_r",
            annot=True,
            mask=mask,
            linewidths=.5,
            cbar_kws={"shrink": .5},
            vmin=-1,
            vmax=1)
plt.show()

# 3 - check column detail
countires = df["Country_Region"]
print(countires.head())
print(countires.count())
# 180 countries
print(countires.unique(), len(countires.unique()))
# count by each values => US, China, Korea, ETC
print(countires.value_counts())

# 4 - choose several essential columns
covid_stat = df[["Confirmed", "Deaths", "Recovered"]]
print(covid_stat.head())

# 5 - condition
df_test = pd.read_csv(path + "04-01-2020.csv",
                      delimiter=",",
                      encoding="utf-8")
new_df_test = df_test[df_test["Country_Region"] == "US"]
print(new_df_test)

# 6 - check NaN and solution
print(covid_stat.isnull().sum())

# remove all NaN
dropped_df = df.dropna()
print(dropped_df.info())

# subset => set criteria
subset_df = df.dropna(subset=["FIPS"])
print(subset_df.info())

# fillna => from NaN to specific value
filled_df = df.fillna(0)
print(filled_df.info())

# selected fillna
dic = {"Deaths": 0, "Recovered": 0}
selected_df = df.fillna(dic)
print(selected_df.info())

# same as SQL
df_test = df_test.groupby("Country_Region").sum()
print(df_test.head())

# change column type to another
doc = pd.read_csv(path + "01-22-2020.csv", encoding="utf-8-sig")
doc = doc[["Country/Region", "Confirmed"]]
doc = doc.dropna(subset=["Confirmed"])
doc = doc.astype({"Confirmed": "int64"})
print(doc.info())
print(doc.head())

doc = doc.duplicated()
print(doc)

doc = doc.drop_duplicates()
print(doc)