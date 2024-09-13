import pandas as pd
import rich
import sys



df = pd.read_csv("hd2022.csv", encoding='latin1')
rich.print(df)
rich.print(df.columns)
rich.print(df.shape)

# picking columns
rich.print(df[['UNITID', 'INSTNM']])
rich.print(df.filter(regex='.*URL'))

# picking rows

# all institutions in Florida
rich.print(df[df['STABBR'] == 'FL'])

# institutions in Florida that have 'University' in their name
fl_univ = df.query('STABBR == "FL" & INSTNM.str.contains("University")',
                engine='python')
rich.print(fl_univ)

# first 10 rows
rich.print(fl_univ.iloc[0:10])

# first 10 rows, third column
rich.print(fl_univ.iloc[0:10,2])

rich.print(fl_univ.loc[651])

# reset the index to the UNITID
fl_univ.index = fl_univ['INSTNM']
rich.print(fl_univ)
rich.print(fl_univ.loc['Stetson University'])
#rich.print(fl_univ.iloc['Stetson University'])
#rich.print(fl_univ['Stetson University'])
rich.print(fl_univ.at['Stetson University','ADDR'])

rich.print(fl_univ.describe())
rich.print(fl_univ[['ADDR','CITY']].count())

sys.exit()
stetson = df[df['INSTNM'] == 'Stetson University'].iloc[0]
rich.print(stetson.to_dict())

df_finaid = pd.read_csv("sfa2122.csv", encoding='latin1')
df_finaid_dictionary = pd.read_excel("sfa2122.xlsx", sheet_name="varlist")
print(df_finaid)
print(df_finaid_dictionary)
stetson_finaid = df_finaid[stetson['UNITID'] == df_finaid['UNITID']].iloc[0].to_dict()
stetson_finaid_newkeys = {}
for key in stetson_finaid:
    new_key = df_finaid_dictionary[df_finaid_dictionary['varname'] == key]['varTitle']
    if len(new_key) > 0:
        new_key = new_key.iloc[0]
        stetson_finaid_newkeys[new_key] = stetson_finaid[key]
rich.print(stetson_finaid_newkeys)
