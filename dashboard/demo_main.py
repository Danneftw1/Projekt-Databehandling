import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Output, Input
from layout import Layout

 
# creates the dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.QUARTZ],
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)

app.layout = Layout().layout()

if __name__ == "__main__":
    app.run_server(debug=True)
