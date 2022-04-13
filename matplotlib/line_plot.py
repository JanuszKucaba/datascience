'''
Learn matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('ca-covid.csv')
df.drop('state', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%y')
df['month'] = df['date'].dt.month
df.set_index('date', inplace=True)

df[df['month'] == 12]['cases'].plot()
#plt.savefig('line_plot.png')

plt.xlabel('Day')
plt.ylabel('# of cases')

plt.show()
