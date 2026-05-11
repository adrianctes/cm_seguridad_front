import flet as ft


class Navbar:

    def build(self):

        return ft.Container(
            height=70,
            bgcolor="white",
            padding=20,

            border=ft.Border.only(
                bottom=ft.BorderSide(1, "#E2E8F0")
            ),

            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    ft.Text(
                        "Sistema Integral",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Row(
                        controls=[

                            ft.Icon(ft.Icons.NOTIFICATIONS),

                            ft.CircleAvatar(
                                content=ft.Text("A")
                            )

                        ]
                    )

                ]
            )
        )