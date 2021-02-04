import pandas as pd
import json

path = "../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"

def basic(doc: pd.DataFrame):
    try:
        doc = doc[["Province_State", "Country_Region", "Confirmed"]]
    except:
        doc = doc[["Province/State", "Country/Region", "Confirmed"]]
        doc.columns = ["Province_State", "Country_Region", "Confirmed"]

    doc = doc.dropna(subset=["Confirmed"])
    doc = doc.astype({"Confirmed": "int64"})
    return doc

def country_name_convert(doc: pd.DataFrame):
    with open("../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/country_convert.json", "r", encoding="utf-8-sig") as json_file:
        json_data = json.load(json_file)

    if doc["Country_Region"] in json_data:
        doc["Country_Region"] = json_data[doc["Country_Region"]]
    return doc

def change_column_name(doc: pd.DataFrame, date):
    date_column = date.split(".")[0].lstrip("0").replace("-", "/")
    doc.columns = [date_column]
    return doc

def sum_confirmed(doc: pd.DataFrame):
    return doc.groupby("Country_Region").sum()

# preprocessing
def preprocessing_by_csv_file(date):
    doc = pd.read_csv(path + date, encoding="utf-8")

    # step1
    doc = basic(doc)

    # step2
    doc = doc.apply(country_name_convert, axis=1)
    doc = doc[["Country_Region", "Confirmed"]]

    # step3
    doc = sum_confirmed(doc)

    # step4
    doc = change_column_name(doc, date)
    return doc

# call csv file list
import os

def generate_dateframe_by_path(path):
    file_list, csv_list = os.listdir(path), list()
    first_doc = True
    for file in file_list:
        if file.split(".")[-1] == 'csv':
            csv_list.append(file)

    # sort asc
    csv_list.sort()

    for file in csv_list:
        doc = preprocessing_by_csv_file(file)
        if first_doc:
            final_doc, first_doc = doc, False
        else:
            final_doc = pd.merge(final_doc, doc, how='outer', left_index=True, right_index=True)

    final_doc = final_doc.fillna(0)
    return final_doc

final_doc = generate_dateframe_by_path(path)
final_doc = final_doc.astype("int64")
final_doc.to_csv(path + "/final_df.csv")

