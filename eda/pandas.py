# pandas grammar
import pandas as pd
# series (1-dim) vs dataframe (n-dim)

# 1-dim with index
series = pd.Series([1, 2, 3], dtype="float64")
print(series)
print(series.index)
series.index = ["일", "이", "삼"]
print(series)

# point out specific data
print(series["일"])
print(series[0])

# delete by index
del series["일"]
print(series)

df = pd.read_csv("../documents/00_Material(Uploaded)/00_data/csv_test_dict.csv", encoding="utf-8-sig", delimiter=",")
print(df)
print(df["first_col"])
print(df.columns)

# information of dataframe
print(df.info())

# add new row
df = df.append({"first_col": "park", "second_col": "jinsu"}, ignore_index=True)
print(df)

# delete specific rows
df.drop(df[df["first_col"] == "park"].index, inplace=True)
print(df)

df = df.append({"first_col": "park", "second_col": "jinsu"}, ignore_index=True)
print(df)
print("============")

# call specific row by index value
print(df.loc[0])

# call specific row by index number
print(df.iloc[0])

# add new row by loc (1000 = index value)
df.loc[1000] = ["park", "jinyoung"]

# call specific col by column name
print(df["first_col"])
print(df.first_col)

# delete row (axis=0 / default)
df.drop([0], inplace=True)

# delete row (axis=1)
df.drop(["second_col"], axis=1, inplace=True)
print(df)

# copy df
df_copy = df["first_col"].copy()
print(df_copy)


