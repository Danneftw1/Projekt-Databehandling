from dash import html, dcc
import dash_bootstrap_components as dbc

class Layout:

    def layout(self):

        return dbc.Container(
            [html.Header([html.H1("Sweden OS")]),
             
             dbc.Row(children=[

                dbc.Col(
                    dbc.Container([html.P("Con1")], id="con1", fluid= True), width= 9
                ), 

                dbc.Col(
                    dbc.Container([html.P("Con2")], id="con2", fluid= True), 
                ),
                
                
             ],className="g-0", justify="start",)
            
            ], fluid= True) 