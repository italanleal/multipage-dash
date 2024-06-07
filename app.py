from dash import Dash

app = Dash(__name__, suppress_callback_exceptions=True)
app.title = "Multi-Page Dash App"
server = app.server  # This will be useful if you deploy the app to a platform like Heroku
