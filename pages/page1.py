from dash import html, dcc

signature = 'eb15715c-9754-4d56-9024-9ef0e18eb89a'
def salt(id):
    return signature + id

layout = html.Div([
    html.H1('Page 1'),
    html.P('Welcome to Page 1.'),
    html.A('Go to Page 2', href='/page2'),

    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id=salt('my-input'), value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id=salt('my-output')),
])
