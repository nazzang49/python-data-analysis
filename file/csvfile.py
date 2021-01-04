# csv = comma-separated value

# import pandas as pd
# df = pd.read_csv("../documents/00_Material(Uploaded)/00_data/USvideos.csv", delimiter=",", encoding="utf-8")
# print(df.head())
# print(df.tail())

import csv
file = open("../documents/00_Material(Uploaded)/00_data/USvideos.csv", 'r', encoding="utf-8-sig")
# list type
datas = csv.reader(file, delimiter=",")
for data in datas:
    print(data)

# newline => 개행 처리
file = open("../documents/00_Material(Uploaded)/00_data/csv_test.csv", 'w', encoding="utf-8-sig", newline="")
writer = csv.writer(file, delimiter=",")
writer.writerow(["1", "2", "3"])
file.close()

# save as dict type with column name
with open("../documents/00_Material(Uploaded)/00_data/csv_test_dict.csv", 'w', encoding="utf-8-sig", newline="") as writer_csv:
    writer = csv.DictWriter(writer_csv, fieldnames=["first_col", "second_col"])
    writer.writeheader()
    writer.writerow({"first_col": "park", "second_col": "jinyoung"})

# read csv dict file
with open("../documents/00_Material(Uploaded)/00_data/csv_test_dict.csv", 'r', encoding="utf-8-sig", newline="") as reader_csv:
    reader = csv.DictReader(reader_csv)
    for r in reader:
        print(r["first_col"], r["second_col"])

