# EDA about covid19
import pandas as pd

# data from https://github.com/CSSEGISandData/COVID-19/tree/master/who_covid_19_situation_reports
df = pd.read_csv("../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv", encoding="utf-8")

# check data
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)









