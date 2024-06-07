from dash import dcc, html, Input, Output
from app import app
from pages import page1, page2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output(component_id=page1.salt('my-output'), component_property='children'),
    Input(component_id=page1.salt('my-input'), component_property='value')
)

@app.callback(
    Output(component_id=page2.salt('my-output'), component_property='children'),
    Input(component_id=page2.salt('my-input'), component_property='value')
)

def update_output_div(input_value):
    return f'Output: {input_value}'

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return '404 - Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)