'''
Learning pandas
'''

import pandas as pd


# Pandas Series
a = pd.Series([-1, 1, 3, 5, 7])
print(a * 10)
print('-' * 20)

print(a.abs())
print('-' * 20)

print(a.describe())
print('-' * 20)

a.index = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
print(a)
print('-' * 20)

print(a['Fifth'])
print('-' * 20)
print('-' * 20)

# Pandas DataFrame
# - making DataFrame
a = [['Isabel', 24], ['Michael', 12], ['Tom', 39], ['Eve', 45]]
df_a = pd.DataFrame(a)
df_a.columns = 'Name', 'Age'
print(df_a)
print('-' * 20)

b = {'Name': ['Eve', 'Michael', 'Kristof', 'Kate', 'Lucy'],
    'City': ['New York', 'London', 'Paris', 'Kiev', 'Moscow']}
df_b = pd.DataFrame(b)
# df_b.index = ['Mechanic', 'Plumber', 'Turner', 'Milling', 'Electronic']
print(df_b)
