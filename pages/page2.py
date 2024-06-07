from dash import html, dcc

signature = '587385fb-baaa-44ba-8309-01dbcbabec1c'
def salt(id):
    return signature + id

layout = html.Div([
    html.H1('Page 2'),
    html.P('Welcome to Page 2.'),
    html.A('Go to Page 1', href='/page1'),
    
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id=salt('my-input'), value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id=salt('my-output')),
    
])
