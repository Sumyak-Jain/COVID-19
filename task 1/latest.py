import pandas as pd
data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-20-2020.csv')
data['Active'] = data['Confirmed'] - data['Deaths'] - data['Recovered']
final = data.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
print(final)
a=input("Enter a country/region:")
print(final.loc[(final['Country_Region'] == a)])
