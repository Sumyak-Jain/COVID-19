import plotly.graph_objects as go
import pandas as pd
import pycountry

#latest date dataset
URL_DATASET = r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-24-2020.csv'
df = pd.read_csv(URL_DATASET)

df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered'] #genrating active cases
df1 = df.groupby('Country_Region')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()

list_countries = df1['Country_Region'].unique().tolist()
d_country_code = {}  # To hold the country names and their ISO
for country in list_countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)
        country_code = country_data[0].alpha_3
        d_country_code.update({country: country_code})
    except:
        print('Not add ISO code for ->', country)
        # If could not find country, make ISO code ' '
        d_country_code.update({country: ' '})

for k, v in d_country_code.items():
    df1.loc[(df1.Country_Region == k), 'iso_alpha'] = v


for col in df1.columns:
    df1[col] = df1[col].astype(str)

 # displaying the details
df1['text'] = df1['Country_Region'] + '<br>' + \  
    'Confirmed: ' + df1['Confirmed'] +'<br>'\
    'Recovered: ' + df1['Recovered'] + '<br>' + \
    'Deaths: ' +df1['Deaths'] + '<br>' + \
    'Active: ' +df1['Active']


fig = go.Figure(data=go.Choropleth(
    locations = df1['iso_alpha'],
    z = df1['Confirmed'],
    text = df1['text'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '',
    colorbar_title = 'No. of Cases',
))

fig.update_layout(
    title_text='COVID 19',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='LATEST AS PER DATASET'+'<br>'\
        'Confirmed , Recovered , Death and Active Cases'+'<br>'\
        'Analysed by SUMYAK JAIN',
        showarrow = False
        
    )]
)

fig.show()
