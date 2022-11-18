from dash import html, dcc
import dash_bootstrap_components as dbc

class Layout:

    def layout(self):

        return dbc.Container(
            [html.Header([html.H1("Sweden OS")]),
             
             dbc.Row(children=[

                dbc.Col(

                    dbc.Container([
                    
                        dbc.Row(children=[

                            dbc.Col([
                                dbc.Card([html.H2("Card #1")], className="mini-Card"),
                            ], className="right-Columns", width= 6),

                            dbc.Col([
                                dbc.Card([html.H2("Card #2")], className="mini-Card"),
                            ], className="right-Columns", width= 6),

                        ], align= "start"),

                        dbc.Row(children=[

                            dbc.Col([

                                dbc.Card([

                                    dbc.CardBody([
                                        html.H2("Card #3"),
                                        dcc.Dropdown(className="dropdown"),
                                        dcc.Graph(),
                                    ]),
                                    
                                
                                
                                ], className="big-Card"),
                            ], className="right-Columns"),
                        ]),

                        dbc.Row(children=[

                            dbc.Col([
                                dbc.Card([

                                    dbc.CardBody([
                                        html.H2("Card #4"),
                                        dcc.Dropdown(className="dropdown"),
                                        dcc.Graph(),
                                    ]),
                                
                                
                                ], className="big-Card"),
                            ], className="right-Columns"),
                        ]),

                    
                    ], id="Container-1", fluid= True), width= 8
                ), 

                dbc.Col(
                    dbc.Container([
                        
                        dbc.Row(children= [
                            
                            dbc.Col([
                                dbc.Card([html.H2("Card #5")], className="medium-Card"),
                            ], className="side-Columns"),

                        ],),

                        dbc.Row(children= [

                            dbc.Col([
                                dbc.Card([html.H2("Card #6")], className="medium-Card"),
                            ], className="side-Columns"),

                        ]),

                        dbc.Row(children= [

                            dbc.Col([
                                dbc.Card([html.H2("Card #7")], className="medium-Card"),
                            ], className="side-Columns"),

                        ]),
                    
                    
                    ], id="Container-2", fluid= True), 
                ),
                
                
             ],className="g-0", justify="start",)
            
            ], fluid= True) 