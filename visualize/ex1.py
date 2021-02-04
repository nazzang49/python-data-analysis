import pandas as pd

path = "../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
df1 = pd.read_csv(path + "01-22-2020.csv", encoding="utf-8")
print(df1.head())

df2 = pd.read_csv(path + "03-01-2020.csv", encoding="utf-8")
print(df2.head())

def basic_preprocessing(doc: pd.DataFrame):
    try:
        doc = doc[["Province_State", "Country_Region", "Confirmed"]]
    except:
        doc = doc[["Province/State", "Country/Region", "Confirmed"]]
        doc.columns = ["Province_State", "Country_Region", "Confirmed"]

    # criteria column
    doc = doc.dropna(subset=["Confirmed"])
    doc = doc.astype({"Confirmed": "int64"})
    return doc

# preprocessing
df1 = basic_preprocessing(df1)
print("============== First df1 ==============")
print(df1)

# call country info
country_info = pd.read_csv("../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding="utf-8-sig")
print(country_info.head())

# merge
test_df = pd.merge(df1, country_info, how="left", on="Country_Region")
print(test_df.head())
print(test_df.info())

# check not matched country => iso2 column
print(test_df.isnull().sum())

# NaN rows in iso2 column
nan_rows = test_df[test_df["iso2"].isnull()]
print(nan_rows)

import json

with open("../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/country_convert.json", 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    print(json_data.keys())

    # check value
    for key in json_data.keys():
        print(json_data[key])

# use apply function
def country_name(df: pd.DataFrame):
    # check key-match
    if df["Country_Region"] in json_data:
        # convert form key to value
        df["Country_Region"] = json_data[df["Country_Region"]]
    return df

df1 = df1.apply(country_name, axis=1)
print(df1.head())

data = "01-22-2020.csv"
date_column = data.split(".")[0].lstrip('0').replace('-', '/')
print(date_column)

# new column name
df1.columns = ['Province_State', 'Country_Region', date_column]
print(df1)