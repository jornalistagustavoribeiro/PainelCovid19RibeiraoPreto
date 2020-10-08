# importing libraries

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go

# reading the dataset with the specified header by brasil.io

url = "https://brasil.io/api/dataset/covid19/caso_full/data/?city=Ribeir%C3%A3o+Preto&format=json"
headers = {"User-Agent": "python-urllib"}
r = requests.get(url, headers=headers)

# get only the column "results" from the json into a dataframe

caso_full = pd.DataFrame(r.json()["results"])

# cleaning dataframe

caso_full = caso_full.drop(
<<<<<<< HEAD
    ['city', 'city_ibge_code',
     'epidemiological_week',
     'estimated_population',
     'estimated_population_2019',
     'is_last', 'is_repeated',
     'last_available_confirmed_per_100k_inhabitants',
     'last_available_date',
     'last_available_death_rate',
     'order_for_place',
     'place_type',
=======
    ['city', 'city_ibge_code', 
     'epidemiological_week', 
     'estimated_population_2019', 
     'is_last', 'is_repeated', 
     'last_available_confirmed_per_100k_inhabitants', 
     'last_available_date', 
     'last_available_death_rate', 
     'order_for_place', 
     'place_type', 
>>>>>>> 5126c288caa53444b722c3256d0f29d608cb81ea
     'state'], axis=1)

# adding moving average

caso_full['mediaMovelCasos'] = caso_full.rolling(window=7)['new_confirmed'].mean()
caso_full['mediaMovelMortes'] = caso_full.rolling(window=7)['new_deaths'].mean()

# creating the table dataframe

tabela = caso_full.drop(
    ['new_confirmed',
     'new_deaths',
     'mediaMovelCasos',
     'mediaMovelMortes'], axis=1)

tabela = tabela.rename(columns=
<<<<<<< HEAD
                       {'date':'Data',
                        'last_available_confirmed':'Casos',
=======
                       {'date':'Data', 
                        'last_available_confirmed':'Casos', 
>>>>>>> 5126c288caa53444b722c3256d0f29d608cb81ea
                        'last_available_deaths':'Mortes'})

# creating charts

<<<<<<< HEAD
tabelaMostra = go.Figure(data=[go.Table(header=dict(values=list(tabela.columns)),
                                        cells=dict(values=[tabela.Data,
                                                           tabela.Casos,
=======
tabelaMostra = go.Figure(data=[go.Table(header=dict(values=list(tabela.columns)), 
                                        cells=dict(values=[tabela.Data, 
                                                           tabela.Casos, 
>>>>>>> 5126c288caa53444b722c3256d0f29d608cb81ea
                                                           tabela.Mortes]))])

mediaCasosDia = go.Figure()

mediaCasosDia.add_trace(
    go.Scatter(
        x=caso_full["date"],
        y=caso_full["mediaMovelCasos"],
        name="Média Móvel"))

mediaCasosDia.add_trace(
    go.Bar(
        x=caso_full["date"],
        y=caso_full["new_confirmed"],
        name="Casos no dia"))

mediaMortesDia = go.Figure()

mediaMortesDia.add_trace(
    go.Scatter(
        x=caso_full["date"],
        y=caso_full["mediaMovelMortes"],
        name="Média Móvel"))

mediaMortesDia.add_trace(
    go.Bar(
        x=caso_full["date"],
        y=caso_full["new_deaths"],
        name="Mortes no dia"))

# creating dash app

app = dash.Dash(__name__)
server = app.server
app.title = 'Covid-19 Ribeirão Preto'

app.layout = html.Div([
<<<<<<< HEAD
    html.Div('Atualizações sobre a pandemia de Covid-19 em Ribeirão Preto',
              style={'textAlign':'center'}),
    html.Div([html.A(href='mailto:jornalistagustavoribeiro@gmail.com',
                    children="jornalistagustavoribeiro@gmail.com")],
              style={'textAlign':'center'}),
    html.Div([html.A(href='https://github.com/jornalistagustavoribeiro/PainelCovid19RibeiraoPreto',
                    children="Github")],
              style={'textAlign':'center'}),
    html.Div([dcc.Graph(id="casos", figure=mediaCasosDia)]),
    html.Div([dcc.Graph(id="mortes", figure=mediaMortesDia)]),
    html.Div([dcc.Graph(id='ultimas', figure=tabelaMostra)])
])
=======
    html.Div('Atualizações sobre a pandemia de Covid-19 em Ribeirão Preto', 
              style={'textAlign':'center'}),
    html.Div([html.A(href='mailto:jornalistagustavoribeiro@gmail.com', 
                    children="jornalistagustavoribeiro@gmail.com")],
              style={'textAlign':'center'}),
    html.Div([html.A(href='https://github.com/jornalistagustavoribeiro/PainelCovid19RibeiraoPreto', 
                    children="Github")],
              style={'textAlign':'center'}), 
    html.Div([dcc.Graph(id="casos", figure=mediaCasosDia)]), 
    html.Div([dcc.Graph(id="mortes", figure=mediaMortesDia)]),
    html.Div([dcc.Graph(id='ultimas', figure=tabelaMostra)])
])

if __name__ == '__main__':
    app.run_server()

>>>>>>> 5126c288caa53444b722c3256d0f29d608cb81ea