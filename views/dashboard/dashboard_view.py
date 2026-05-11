import flet as ft


class DashboardView:

    def build(self):

        return ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                controls=[

                    ft.Text(
                        "Dashboard",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.ResponsiveRow(
                        controls=[

                            self.card(
                                "Legajos",
                                "200"
                            ),

                            self.card(
                                "Turnos",
                                "35"
                            ),

                            self.card(
                                "Liquidaciones",
                                "198"
                            ),

                            self.card(
                                "Novedades",
                                "12"
                            )

                        ]
                    )

                ]
            )
        )

    def card(self, title, value):

        return ft.Container(
            col={"sm": 6, "md": 3},
            bgcolor="white",
            border_radius=15,
            padding=20,
            shadow=ft.BoxShadow(
                blur_radius=15,
                color="#00000010"
            ),
            content=ft.Column(
                controls=[

                    ft.Text(
                        title,
                        size=15,
                        color="grey"
                    ),

                    ft.Text(
                        value,
                        size=30,
                        weight=ft.FontWeight.BOLD
                    )

                ]
            )
        )