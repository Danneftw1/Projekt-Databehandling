from dash import html, dcc
import dash_bootstrap_components as dbc

class Layout:

    def __init__(self, dropdown_options_medals_athlets, dropdown_options_sweden_medals, sub_options_dropdown, game_dict) -> None:
        
        self._dropdown_options_medals_athlets = dropdown_options_medals_athlets
        self._dropdown_options_sweden_medals = dropdown_options_sweden_medals
        self._sub_options_dropdown = sub_options_dropdown
        self._game_dict = game_dict

    def layout(self):

        return dbc.Container(
            [dbc.Navbar(children=[
                
                dbc.Row(children=[
                    
                    dbc.Col([
                        html.Img(src= "assets/images/Olympics-Logo-700x394.png", height="30px")
                    ]),

                    dbc.Col([
                        dbc.NavbarBrand("Sweden")
                    ]),

                ])

            ]),
             
             dbc.Row(children=[

                dbc.Col(

                    dbc.Container([

                        dbc.Row(children=[

                            dbc.Col([

                                dbc.Card([

                                    dbc.CardBody([
                                        html.H2("Data & Graphs for Olympics"),
                                        dcc.Dropdown(className="dropdown", id='sportpicker-dropdown', options= self._dropdown_options_medals_athlets, value='Snowboarding'),
                                        dcc.RadioItems(id = 'sub-options-dropdown', options= self._sub_options_dropdown, value= 'Medals Won'), # open-high-low-close(options)
                                        dcc.Graph(id = 'athlete-medal-graph'),
                                    ]),
                                    
                                
                                
                                ], className="big-Card"),
                            ], className="right-Columns"),

                            dbc.Col([

                                dbc.Card([

                                    dbc.CardBody([
                                        html.H2("Card #5"),
                                        dcc.Graph(id="pie_Chart"),
                                    ])

                                ], className="medium-Card")

                            ], width= 4),

                        ]),

                        dbc.Row(children=[

                            dbc.Col([
                                dbc.Card([

                                    dbc.CardBody([
                                        html.H2("How Many Medals Sweden Has Won In The Olympics"),
                                        dcc.Dropdown(className="dropdown", id = 'game-picker', options= self._game_dict, value='1'),
                                        dcc.Graph(id = 'sweden-medal-graph'),
                                    ]),
                                
                                
                                ], className="big-Card"),
                            ], className="right-Columns"),
                        ]),

                    
                    ], id="Container-1", fluid= True),
                ), 

                # dbc.Col(
                #     dbc.Container([
                        
                #         dbc.Row(children= [
                            
                #             dbc.Col([
                #                 dbc.Card([html.H2("Card #5")], className="medium-Card"),
                #             ], className="side-Columns"),

                #         ],),

                #         dbc.Row(children= [

                #             dbc.Col([
                #                 dbc.Card([html.H2("Card #6")], className="medium-Card"),
                #             ], className="side-Columns"),

                #         ]),

                #         dbc.Row(children= [

                #             dbc.Col([
                #                 dbc.Card([html.H2("Card #7")], className="medium-Card"),
                #             ], className="side-Columns"),

                #         ]),
                    
                    
                #     ], id="Container-2", fluid= True), 
                # ),
                
                
             ],className="g-0", justify="start",)
            
            ], fluid= True) 