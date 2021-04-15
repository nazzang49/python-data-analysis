import pandas as pd

# Q1) read csv
df = pd.read_csv("../documents/00_Material(Uploaded)/00_data/olist_customers_dataset.csv", encoding='utf-8-sig')

# Q2) head
print(df.head(5))
print(df['customer_id'].head(5))
print(df['customer_unique_id'].head(5))
print(df['customer_zip_code_prefix'].head(5))
print(df['customer_city'].head(5))
print(df['customer_state'].head(5))

# Q3) row count
print(df.shape[0])

# Q4) col count
print(df.shape[1])

# Q5) column list
print(df.columns)

# Q6) check index
print(df.index)

# Q7) 5-number summary
print(df.describe())

# Q8) select columns
df2 = df[['customer_zip_code_prefix', 'customer_city', 'customer_state']]
print(df2.head(5))

# Q9) if condition
df3 = df2[df2['customer_city'] == 'sao paulo']
print(df3.head(5))
print(df3.shape[0])

# Q10) value count (value counts)
print(df2['customer_city'].value_counts())

# Q11) value count (group by)
df4 = df.groupby('customer_city').count()
print(df4)
print(df4.shape[0])

# Q12) sort (value)
print(df4.sort_values(by='customer_id', ascending=False))

# Q13) sort (index)
print(df4.sort_index(ascending=True))

# Q14) value count
print(df2['customer_state'].value_counts())

# Q15) customer_state type count
print(df2['customer_state'].drop_duplicates().count())

# Q16) if condition
print(df4[df4['customer_id'] >= 1000])

# Q17) check value
print(df4[df4['customer_id'] >= 1000].index)

# Q18) check NaN by each columns
print(df.isna().sum())

# Q19) from df to list
df5 = df.drop_duplicates(subset='customer_city')
print(df5.groupby('customer_city').count().index)

doc_covid = pd.read_csv('../documents/00_Material(Uploaded)/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/04-01-2020.csv', encoding='utf-8-sig')

# Q20) pivot table
doc_covid2 = pd.pivot_table(doc_covid,
                            index=['Country_Region'],
                            values=['Confirmed'],
                            aggfunc={'Confirmed': 'median'},
                            fill_value=0,
                            margins=True,
                            margins_name='Total')
print(doc_covid2)

# Q21) add record to pivot table
doc_covid2.loc['Total'] = [doc_covid2['Confirmed'].sum()]
print(doc_covid2)