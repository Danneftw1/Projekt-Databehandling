from dash import html, dcc
import dash_bootstrap_components as dbc
from uppgift_1_grafer import *
from övriga_grafer import *


class Layout:
    # init 
    def __init__(
        self,
        dropdown_options_medals_athlets,
        dropdown_options_sweden_medals,
        sub_options_dropdown,
        game_dict,
        treemap_medal_dict,
    ) -> None:

    # Sets all the incoming variables.
        self._dropdown_options_medals_athlets = dropdown_options_medals_athlets
        self._dropdown_options_sweden_medals = dropdown_options_sweden_medals
        self._sub_options_dropdown = sub_options_dropdown
        self._game_dict = game_dict
        self._treemap_medal_dict = treemap_medal_dict

    # Layout function
    def layout(self):

        # Returns site container.
        return dbc.Container(
            [   
                # the navbar of dashboard.
                dbc.Navbar(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    [
                                        # Olympic logo on site.
                                        html.Img( 
                                            src="assets/images/Olympics-Logo-700x394.png",
                                            height="30px", 
                                        )
                                    ]
                                ),
                                # navbar text
                                dbc.Col([dbc.NavbarBrand("Sweden")]),
                            ]
                        ),
                    ],
                ),
                dbc.Row(
                    children=[
                        dbc.Col(
                            # Main content container 
                            dbc.Container(
                                [
                                    dbc.Row(
                                        children=[
                                            dbc.Col(
                                                [   
                                                    # First big card on left (Data & Graphs for Olympics)
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
                                                                                    # Card header text.
                                                                                    html.H2(
                                                                                        "Data & Graphs for Olympics"
                                                                                    ),
                                                                                ],
                                                                                width=7,
                                                                            ),
                                                                            dbc.Col(
                                                                                [
                                                                                    dbc.Row(
                                                                                        [
                                                                                            dbc.Col(
                                                                                                [   
                                                                                                    # Graph dropdown for (Data & Graphs for Olympics).
                                                                                                    dcc.Dropdown(
                                                                                                        className="dropdown",
                                                                                                        id="sportpicker-dropdown",
                                                                                                        options=self._dropdown_options_medals_athlets,
                                                                                                        value="Snowboarding",
                                                                                                    ),
                                                                                                ]
                                                                                            ),
                                                                                        ]
                                                                                    ),
                                                                                    dbc.Row(
                                                                                        [
                                                                                            dbc.Col(
                                                                                                [
                                                                                                    # Graph radio buttons for (Data & Graphs for Olympics)
                                                                                                    dcc.RadioItems(
                                                                                                        className="radio-button",
                                                                                                        id="sub-options-dropdown",
                                                                                                        options=self._sub_options_dropdown,
                                                                                                        value="Medals Won",
                                                                                                    ),
                                                                                                ],
                                                                                                id="radio-col",
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ],
                                                                        className="row-shadow",
                                                                    ),
                                                                    # Graph for (Data & Graphs for Olympics)
                                                                    dcc.Graph(
                                                                        id="athlete-medal-graph"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        className="big-Card",
                                                    ),
                                                ],
                                                className="right-Columns",
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                [
                                                                    # Card for Pie Chart (Gender distribution) 
                                                                    dbc.Card(
                                                                        [
                                                                            dbc.CardBody(
                                                                                [
                                                                                    # Pie chart for (Gender distribution) 
                                                                                    dcc.Graph(
                                                                                        id="pie_Chart",
                                                                                        figure=sex_distribution(),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ],
                                                                        className="medium-Card",
                                                                    )
                                                                ],
                                                            )
                                                        ]
                                                    ),
                                                    dbc.Row(
                                                        [
                                                            dbc.Col(
                                                                [
                                                                    # Card for (Age distribution) 
                                                                    dbc.Card(
                                                                        [
                                                                            dbc.CardBody(
                                                                                [
                                                                                    # Graph for (Age distribution) 
                                                                                    dcc.Graph(
                                                                                        id="age_Chart",
                                                                                        figure=age_distribution(),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ],
                                                                        className="small-Card",
                                                                    )
                                                                ],
                                                            ),
                                                        ]
                                                    ),
                                                ],
                                                lg=4,
                                                xl=4,
                                                md=12,
                                                sm=12,
                                            ),
                                        ]
                                    ),
                                    dbc.Row(
                                        children=[
                                            dbc.Col(
                                                [
                                                    # Card for big card 2 (How Many Medals Sweden Has Won In The Olympics)
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
                                                                                    # Card header / titel for card 
                                                                                    html.H2(
                                                                                        "How Many Medals Sweden Has Won In The Olympics"
                                                                                    ),
                                                                                ],
                                                                                width=7,
                                                                            ),
                                                                            dbc.Col(
                                                                                [
                                                                                    # Dropdown for (sweden-medal-graph)
                                                                                    dcc.Dropdown(
                                                                                        className="dropdown",
                                                                                        id="game-picker",
                                                                                        options=self._game_dict,
                                                                                        value="0",
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ],
                                                                        className="row-shadow",
                                                                    ),
                                                                    # Graph for sweden-medal-graph
                                                                    dcc.Graph(
                                                                        id="sweden-medal-graph"
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        className="big-Card",
                                                        id="big-Card-2",
                                                    ),
                                                ],
                                                className="right-Columns",
                                            ),
                                            dbc.Col(
                                                [
                                                    # Card for pie-Chart-medals
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    # pie chart (pie-Chart-medals)
                                                                    dcc.Graph(
                                                                        figure=sports_medals_sweden_piechart(
                                                                            "Sweden",
                                                                            df_data,
                                                                        ),
                                                                        id="pie-Chart-medals",
                                                                    ),
                                                                ]
                                                            )
                                                        ],
                                                        className="medium-Card",
                                                        id="medium-Card-2",
                                                    )
                                                ],
                                                lg=4,
                                                xl=4,
                                                md=12,
                                                sm=12,
                                            ),
                                        ]
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    # Card for (treemap_graph)
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
                                                                                    # Radio buttons for (treemap_graph)
                                                                                    dcc.RadioItems(
                                                                                        id="treemap_buttons",
                                                                                        options=self._treemap_medal_dict,
                                                                                        value="Gold",
                                                                                        className="radiobuttons",
                                                                                    )
                                                                                ],className="row-shadow", align= "End"
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
                                                                                    # Graph for (treemap_graph)
                                                                                    dcc.Graph(
                                                                                        id="treemap_graph"
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ]
                                                                    ),
                                                                ]
                                                            ),
                                                        ],
                                                        className="big-Card",
                                                        id="Tree-Card",
                                                    )
                                                ]
                                            ),
                                        ]
                                    ),
                                ],
                                id="Container-1",
                                fluid=True,
                            ),
                        ),
                    ],
                    className="g-0",
                    justify="start",
                ),
            ],
            fluid=True,
        )
