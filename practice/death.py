# analysis about dead people => assignment w/o any help

import pandas as pd
import numpy as np
import os

# daily reports
dir_path = "../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"

# 국가명 통일
# 시간형식 통일

def change_nan_value(df: pd.DataFrame):
    # print(df.isnull().sum(axis=0))
    # print(df[df["Deaths"].isnull()])
    df["Deaths"] = df["Deaths"].fillna(0)
    df = df.astype({"Deaths": "int64"})
    return df

def remove_unnecessary_column(df: pd.DataFrame):
    return df.loc[:, ["Last_Update", "Country_Region", "Deaths"]]

def rename_column(df: pd.DataFrame):
    if df.columns.__contains__("Country/Region"):
        df = df.rename({"Country/Region": "Country_Region", "Last Update": "Last_Update"}, axis="columns")
    return df

def preprocessing(df: pd.DataFrame):
    df = rename_column(df)
    df = remove_unnecessary_column(df)
    df = change_nan_value(df)
    print(df.head())

def return_df(path, csv_name):
    return pd.read_csv(path + csv_name, delimiter=",", encoding="utf-8-sig")

# 3 factors => country, deaths, date
def generate_dateframe_by_path(path):
    file_list, csv_list = os.listdir(dir_path), list()
    for file_name in file_list:
        if file_name.split(".")[-1] == "csv":
            csv_list.append(file_name)

    print(len(csv_list))

    for idx, csv_name in enumerate(csv_list):
        df = return_df(path, csv_name)
        if idx == 1:
            print(df.shape)
            print(df.head())
            print(df.info())
            print(df.columns)
            print(df["Last Update"].head())
        if idx == 140:
            print(df.shape)
            print(df.head())
            print(df.info())
            print(df.columns)
            print(df["Last_Update"].head())
        preprocessing(df)

generate_dateframe_by_path(dir_path)





