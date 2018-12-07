
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('C:\\Users\\User\\Desktop\\NYC_Jobs.csv', sep=',')
print(df.columns, '\n')

for i in range(10):
    print(df.iloc[i])
    print("**********************************************************************************")

# Agency for 10 elem
print('\n\n\n')
print("AGENCY START HERE")
for i in range(10):
    print(df.loc[[i], 'Agency'])
print('\n\n\n')
print("ALL AGENCIES")
print(df['Agency'])
print('\n\n\n')
print("ALL BUSINESS TITLES ")
print(df['Business Title'])
print('\n\n\n')
print("ALL WORKING LOCATIONS")
print(df['Work Location 1'])
print('\n\n\n')
pvt = df.pivot_table(index=['Agency'], values='# Of Positions')
print(pvt)
pvt.plot.bar()
plt.show()
print('\n\n\n')
df['median'] = df.groupby('Salary Range From')['Salary Range To'].transform(np.median)
gb = df.groupby('Work Location')
data1 = pd.DataFrame([df.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
data1 = data1.median(axis=1)
data1.plot()
plt.show()