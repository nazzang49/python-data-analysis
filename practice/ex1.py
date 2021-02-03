import pandas as pd

df1 = pd.DataFrame({"id": [1, 2, 3], "customer_id": [1, 2, 3], "customer_name": ["Robert", "Peter", "Dave"]}, columns=["id", "customer_id", "customer_name"])
print(df1)

df2 = pd.DataFrame({"id": [1, 2, 4], "order_id": [100, 200, 300], "order_date": ["2021-01-21", "2021-02-03", "2020-10-01"]}, columns=["id", "order_id", "order_date"])
print(df2)

# concat dataframe
# up and down
df_concat = pd.concat([df1, df2])
print(df_concat)

# left and right
df_concat = pd.concat([df1, df2], axis=1)
print(df_concat)

# merge
# inner join => only same value
print(pd.merge(df1, df2, on="id"))

# outer join => all
print(pd.merge(df1, df2, on="id", how="outer"))

# left join => left
print(pd.merge(df1, df2, on="id", how="left"))

# right join => right
print(pd.merge(df1, df2, on="id", how="right"))

df1 = df1.set_index("id")
df2 = df2.set_index("id")

print(pd.merge(df1, df2, left_index=True, right_index=True))
print(pd.merge(df1, df2, left_index=True, right_index=True, how="outer"))
print(pd.merge(df1, df2, left_index=True, right_index=True, how="left"))
print(pd.merge(df1, df2, left_index=True, right_index=True, how="right"))





