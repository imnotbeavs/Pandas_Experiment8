import pandas as pd
cars = pd.read_csv('cars.csv')

first5 = cars.iloc[0:5]
last5 = cars.iloc[27:32]

firstlast = pd.concat([first5,last5])
print(firstlast)