import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-23-2020.csv', usecols = ['Last_Update', 'Country_Region', 'Confirmed', 'Deaths', 'Recovered'])
print(data["Last_Update"])
data['Active']=data['Confirmed']-data['Deaths']-data['Recovered']
final=data.groupby(["Country_Region"])["Deaths","Confirmed","Recovered","Active"].sum().reset_index()
final=final.sort_values(by='Deaths',ascending=False)
print(final)
print("enter the number of deaths of which countries have that greater then ")
a=int(input("enter the death cases"))
final=final[final['Deaths']>a]
plt.figure(figsize=(15, 8))
plt.plot(final['Country_Region'], final['Deaths'],color='red')
plt.plot(final['Country_Region'], final['Confirmed'],color='green')
plt.plot(final['Country_Region'], final['Recovered'], color='blue')
plt.plot(final['Country_Region'], final['Active'], color='brown')
tittle='Total Deaths(>',a,') Confirmed, Recovered and Active Cases by Country' 
plt.title(tittle)
plt.show()
