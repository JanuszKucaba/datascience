'''
Learn matplotlib - bar plot multiple
'''


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ca-covid.csv')
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%y')
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

df = df.groupby('month')[['cases', 'deaths']].sum()
df.plot(kind='bar', stacked=True) # vertical bar
#df.plot(kind='barh', stacked=True) # horizonstal bar
#plt.savefig('bar_plot_multiply.png')

plt.show()
