import pandas as pd
from matplotlib import pyplot as plt
data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
a=input("Enter a country/region:")

z=(data.loc[(data['Country/Region'] == a)])
print(z)

print("Enter the dates")
c=input("Enter the start date: ")
b=input("Enter the end date: ")

c1=z.columns.get_loc(c)
b1=z.columns.get_loc(b)

z1=(z.iloc[0:1,c1:b1])
z2=z1.values.tolist()
dates=list(z1.columns)

cases=[]
for i in z2:
    for val in i:
        cases.append(val)
        

title=('Recovered cases in '+a)
plt.figure(figsize=(10, 5))
plt.plot(dates,cases,color='Blue')
plt.title(title)
plt.ylabel("CASES")
plt.xlabel("DATES")
plt.show()

