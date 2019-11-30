import pandas as pd
cars = pd.read_csv('cars.csv')
a = cars.iloc[0:5,0::2]
b = cars.loc[[0]]
c = cars.loc[[23],['cyl']]
d = cars.loc[[1,28,18],['Model','cyl','gear']]

print(a)
print('')
print(b)
print('')
print(c)
print('')
print(d)