import pandas as pd



list_of_df = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)')

df = pd.DataFrame(list_of_df[2])#create this to use the read url and find the [2] table on the page
#print(df.head())
#df.columns = df.columns.droplevel(0)
#df.columns = [c[0] + "_" + c[1] for c in df.columns]

df['United Nations[15]'] = df['United Nations[15]'].replace('85328323', '69696969')
print(df.dtypes)

print(df)
