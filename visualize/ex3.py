import pandas as pd

basic_path = "../documents/00_Material(Uploaded)/COVID-19-master/"

df_confirmed = pd.read_csv(basic_path + "csse_covid_19_data/csse_covid_19_daily_reports/final_df.csv")
print(df_confirmed.head())

# keep_default_na => ‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘n/a’, ‘nan’, ‘null’
# na_values => custom na
country_info = pd.read_csv(basic_path + "csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", encoding='utf-8-sig', keep_default_na=False, na_values='')
print(country_info.head())

country_info[country_info['Country_Region'] == 'Namibia']
country_info = country_info[['iso2', 'Country_Region']]
country_info = country_info.drop_duplicates(subset='Country_Region', keep='last')

print(country_info)

doc_final_country = pd.merge(df_confirmed, country_info, how='left', on='Country_Region')

# condition
# dataframe[(조건1) & (조건2)] : 조건1과 조건2 모두 만족 (and 조건)
# dataframe[(조건1) | (조건2)] : 조건1 또는 조건2 만족 (or 조건)

doc_final_country = doc_final_country.dropna(subset=['iso2'])

# iso2 => iso2 link
def create_flag_link(row):
    flag_link = 'https://www.countryflags.io/' + row + '/flat/64.png'
    return flag_link

doc_final_country['iso2'] = doc_final_country['iso2'].apply(create_flag_link)
print(doc_final_country.head())

# switch column position
cols = doc_final_country.columns.tolist()
cols.remove('iso2')
cols.insert(1, 'iso2')
doc_final_country = doc_final_country[cols]

cols[1] = 'Country_Flag'
doc_final_country.columns = cols
print(doc_final_country.head())


# https://app.flourish.studio/visualisation/5188964/edit?

