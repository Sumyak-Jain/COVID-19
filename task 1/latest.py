import pandas as pd
from matplotlib import pyplot as plt

# read dataset
data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-20-2020.csv')
data['Active'] = data['Confirmed'] - data['Deaths'] - data['Recovered']
final = data.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(final) #dsiplay dataframe
a=input("Enter a country/region:")
print(final.loc[(final['Country_Region'] == a)])
b=(final.loc[(final['Country_Region'] == a)])
b1=b.values.tolist() #nested list
b2=[]
for i in b1:
    for val in i:
        b2.append(val) #flattern nested list
print("Representation of cases in ",b2[0])
b2.remove(b2[0])
info=['Confirmed', 'Deaths', 'Recovered', 'Active']
plt.bar(info,b2,color = 'green') #bar graph 
plt.title('Bar Graph')  
plt.xlabel('Information')  
plt.ylabel('Counts')  
plt.show() 
