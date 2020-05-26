import pandas as pd
from matplotlib import pyplot as plt
data= pd.read_csv('https://raw.githubusercontent.com/sumyak/COVID-19/master/task%207/datasets_557629_1188648_covid_19_india.csv')
final = data.groupby('State/UnionTerritory')['Date','Cured','Deaths','Confirmed'].sum().reset_index()
#print(final)
a=input("Enter a Indian State/UnionTerritory:")
print(final.loc[(final['State/UnionTerritory'] == a)])
b=(final.loc[(final['State/UnionTerritory'] == a)])
b1=b.values.tolist()
b2=[]
for i in b1:
    for val in i:
        b2.append(val)


print("Representation of cases in ",b2[0])
b2.remove(b2[0])
title='Representation of cases in',a
info=['Confirmed', 'Deaths', 'Cured']  
fig1,ax1=plt.subplots()
ax1.pie(b2,  labels=info, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
ax1.axis('equal')  
  
plt.show()  
