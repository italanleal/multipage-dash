from dash import html, dcc, Input, Output

signature = '587385fb-baaa-44ba-8309-01dbcbabec1c'
def salt(id):
    return signature + id

def setCallback(app):
    @app.callback(
        Output(component_id=salt('my-output'), component_property='children'),
        Input(component_id=salt('my-input'), component_property='value')
    )

    def update_output_div(input_value):
        return f'Output: {input_value}'
    
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
