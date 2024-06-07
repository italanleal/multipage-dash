from dash import html, dcc, Input, Output

signature = 'eb15715c-9754-4d56-9024-9ef0e18eb89a'
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
