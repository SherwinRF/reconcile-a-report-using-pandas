# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(path)
df['state'] = df['state'].apply( lambda x: x.lower() )
df['total'] = df['Jan'] + df['Feb'] + df['Mar']
sum_row = { 'Jan':df['Jan'].sum(), 'Feb':df['Feb'].sum(), 'Mar':df['Mar'].sum(), 'total':df['total'].sum() }
df_final = df
df_final = df_final.append(sum_row, ignore_index = True)
print(df_final)


# --------------
import requests

url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1.columns = df1.iloc[11]
df1 = df1.iloc[11:,]
df1 = df1.drop(11)
df1['United States of America'] = df1['United States of America'].apply(lambda x: x.replace(" ", ""))
print(df1)


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
# Mapping
mapping = df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6, 'abbr', np.nan)
df_final['abbr'] = df_final['state'].map(mapping)
print(df_final.head(15))
# Code starts here


# --------------
# Code stars here

df_final['abbr'][6] = 'MS'
df_final['abbr'][10] = 'TN'
print(df_final)

# Code ends here


# --------------
# Code starts here

df_sub = df_final.groupby('abbr')[['abbr','Jan','Feb' ,'Mar','total']].sum()
formatted_df = df_sub.applymap(lambda x: '$' + str(x) )
print(formatted_df)

# Code ends here


# --------------
# Code starts here

sum_row = pd.DataFrame({ 'Jan':[df['Jan'].sum()], 'Feb':[df['Feb'].sum()], 'Mar':[df['Mar'].sum()], 'total':[df['total'].sum()]})
#df_sub_sum = sum_row.transpose() 
df_sub_sum = sum_row.applymap(lambda x: '$' + str(x) )
final_table = formatted_df.append(df_sub_sum)
final_table.rename(index={0:'Total'}, inplace=True)
print(final_table)

# Code ends here


# --------------
# Code starts here

df_sub['total'] = df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']
df_sub['total'].plot( kind='pie' )

# Code ends here


