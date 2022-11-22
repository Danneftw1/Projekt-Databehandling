from dash import html, dcc
import dash_bootstrap_components as dbc
from uppgift_1_grafer import *
from övriga_grafer import *


class Layout:
    def __init__(
        self,
        dropdown_options_medals_athlets,
        dropdown_options_sweden_medals,
        sub_options_dropdown,
        game_dict,
        treemap_medal_dict,
    ) -> None:

        self._dropdown_options_medals_athlets = dropdown_options_medals_athlets
        self._dropdown_options_sweden_medals = dropdown_options_sweden_medals
        self._sub_options_dropdown = sub_options_dropdown
        self._game_dict = game_dict
        self._treemap_medal_dict = treemap_medal_dict

    def layout(self):

        return dbc.Container(
            [
                dbc.Navbar(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    [
                                        html.Img(
                                            src="assets/images/Olympics-Logo-700x394.png",
                                            height="30px",
                                        )
                                    ]
                                ),
                                dbc.Col([dbc.NavbarBrand("Sweden")]),
                            ]
                        ),
                    ],
                ),
                dbc.Row(
                    children=[
                        dbc.Col(
                            dbc.Container(
                                [
                                    dbc.Row(
                                        children=[
                                            dbc.Col(
                                                [
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
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
                                                                                                    dcc.RadioItems(
                                                                                                        className="radio-button",
                                                                                                        id="sub-options-dropdown",
                                                                                                        options=self._sub_options_dropdown,
                                                                                                        value="Medals Won",
                                                                                                    ),  # open-high-low-close(options)
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
                                                                    dbc.Card(
                                                                        [
                                                                            dbc.CardBody(
                                                                                [
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
                                                                    dbc.Card(
                                                                        [
                                                                            dbc.CardBody(
                                                                                [
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
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
                                                                                    html.H2(
                                                                                        "How Many Medals Sweden Has Won In The Olympics"
                                                                                    ),
                                                                                ],
                                                                                width=7,
                                                                            ),
                                                                            dbc.Col(
                                                                                [
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
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
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
                                                    dbc.Card(
                                                        [
                                                            dbc.CardBody(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                [
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
                    ],
                    className="g-0",
                    justify="start",
                ),
            ],
            fluid=True,
        )
