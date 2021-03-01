# analysis about dead people => assignment w/o any help

import pandas as pd
import os
import json

# daily reports
dir_path = "../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"

# json file
with open("../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/country_convert.json", "r", encoding="utf-8-sig") as json_country_convert_file:
    json_country_convert_data = json.load(json_country_convert_file)

# change date format into regular
def integrate_date_fdormat(df: pd.DataFrame, date):
    date_format = date.split(".")[0].lstrip("0").replace("-", "/")
    df.columns = [date_format]
    return df

# index => Country_Region
def sum_gruop_by_country(df: pd.DataFrame):
    return df.groupby("Country_Region").sum()

# Beijing => China
def integrate_country_name(df: pd.DataFrame):
    if df["Country_Region"] in json_country_convert_data:
        df["Country_Region"] = json_country_convert_data[df["Country_Region"]]
    return df

# NaN => 0 of Deaths
def change_nan_value(df: pd.DataFrame):
    # print(df.isnull().sum(axis=0))
    # print(df[df["Deaths"].isnull()])
    # df["Deaths"] = df["Deaths"].fillna(0)
    df = df.dropna(subset=["Recovered"])
    df = df.astype({"Recovered": "int64"})
    return df

# need only 3 columns
def remove_unnecessary_column(df: pd.DataFrame):
    return df.loc[:, ["Last_Update", "Country_Region", "Recovered"]]

# change column name
def rename_column(df: pd.DataFrame):
    if df.columns.__contains__("Province/State"):
        df = df.rename({"Province/State": "Province_State", "Country/Region": "Country_Region", "Last Update": "Last_Update"}, axis="columns")
    return df

# data preprocessing before visualization
def preprocessing(df: pd.DataFrame, date):
    df = rename_column(df)
    df = remove_unnecessary_column(df)
    df = change_nan_value(df)
    df = df.apply(integrate_country_name, axis=1)
    df = sum_gruop_by_country(df)
    df = integrate_date_fdormat(df, date)
    return df

# call csv
def return_df(path, csv_name):
    return pd.read_csv(path + csv_name, delimiter=",", encoding="utf-8-sig")

# 3 factors => country, deaths, date
def generate_dateframe_by_path(path):
    file_list, csv_list = os.listdir(dir_path), list()
    for file_name in file_list:
        if file_name.split(".")[-1] == "csv":
            csv_list.append(file_name)

    print(len(csv_list))
    csv_list.sort()

    first_df_flag = True
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

        df = preprocessing(df, csv_name)

        if first_df_flag:
            final_df, first_df_flag = df, False
        else:
            final_df = pd.merge(final_df, df, how='outer', left_index=True, right_index=True)

    final_df = final_df.fillna(0)
    return final_df

final_df = generate_dateframe_by_path(dir_path)
final_df = final_df.astype("int64")
final_df.to_csv(dir_path + "/result/recovered_df.csv")

