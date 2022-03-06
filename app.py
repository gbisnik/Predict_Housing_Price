import dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
import plotly.graph_objs as go
import pickle
from dash.dependencies import Input, Output, State

########### Define your variables ######
myheading1='Forecast Home Sale Prices in Ames, Iowa'
image1='ames_welcome.jpeg'
tabtitle = 'Ames Housing'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/austinlasseter/simple-ml-apps'

########### open the pickle file ######
# filename = open('analysis/ames_housing_lr_model.pkl', 'rb')
# unpickled_model = pickle.load(filename)
# filename.close()

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
                html.H3('Features of Home:'),
                html.Div('Year Built:'),
                dcc.Input(id='YearBuilt', value=2010, type='number', min=2006, max=2010, step=1),
                html.Div('Bathrooms:'),
                dcc.Input(id='Bathrooms', value=2, type='number', min=1, max=5, step=1),
                html.Div('Bedrooms:'),
                dcc.Input(id='BedroomAbvGr', value=4, type='number', min=1, max=5, step=1),
                html.Div('Total Square Feet:'),
                dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=5000, step=1),
                html.Div('Single Family Home:'),
                dcc.Input(id='SingleFam', value=0, type='number', min=0, max=1, step=1),
                html.Div('Large Neighborhood:'),
                dcc.Input(id='LargeNeighborhood', value=0, type='number', min=0, max=1, step=1),
                html.Div('Location:'),
                dcc.Input(id='Location', value=0, type='number', min=0, max=10, step=1),
                html.Div('GarageCarsPresent:'),
                dcc.Input(id='GarageCarsPresent', value=0, type='number', min=0, max=1, step=1),

            ], className='four columns'),
            html.Div([
                html.H3('Forecast Home Value:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',
    ),


    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    [
    Input(component_id='YearBuilt', component_property='value'),
    Input(component_id='Bathrooms', component_property='value'),
    Input(component_id='BedroomAbvGr', component_property='value'),
    Input(component_id='TotalSF', component_property='value'),
    Input(component_id='SingleFam', component_property='value'),
    Input(component_id='LargeNeighborhood', component_property='value'),
    Input(component_id='Location', component_property='value'),
    Input(component_id='GarageCarsPresent', component_property='value')
    ]
)
def ames_lr_function(YearBuilt,Bathrooms,BedroomAbvGr,TotalSF,SingleFam,LargeNeighborhood,Location,GarageCarsPresent):
    try:
        y = [-1261013.5888 + 554.5508*YearBuilt + 10337.9838*Bathrooms + -3420.1288*BedroomAbvGr + 39.8813*TotalSF + 19178.523*SingleFam + -8164.127*LargeNeighborhood +41717.0694*Location +6033.0974*GarageCarsPresent]
        # y = unpickled_model.predict([[YearBuilt,Bathrooms,BedroomAbvGr,TotalSF,SingleFam,LargeNeighborhood]])
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y
    except:
        return "inadequate inputs"

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
