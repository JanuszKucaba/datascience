'''
Learn seaborn
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('World_Bank_CO2_cleaned.xlsx')
print(df.head())

print('-' * 100)
df = df[~df['CO2 (kt)'].isnull() & ~df['CO2 Per Capita (metric tons)'].isnull() & (df['Year'] > 1980)]
print(df.head())

print('-' * 100)
df_pl = df[df['Country Name'] == 'Poland']
print(df_pl.head())

# Tips
print('-' * 100)
tips = sns.load_dataset('tips')
print(tips.head())

# scatter plot
sns.relplot(data=df[(df['Country Name'] == 'Poland') | (df['Country Name'] == 'Germany')],
            x = 'Year',
            y = 'CO2 Per Capita (metric tons)',
            aspect = 2,
            kind = 'scatter',
            col = 'Country Name')
plt.show()

sns.relplot(x ='total_bill',
           y = 'tip',
           aspect = 2.5,
           data = tips,
           size = 'size',
           hue = 'smoker',
           kind = 'scatter')
plt.show()
