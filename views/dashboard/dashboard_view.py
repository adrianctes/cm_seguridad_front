import flet as ft


class DashboardView(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.expand = True

        # 👇 ESTE es el control de espacio de la vista
        self.padding = 20

        self.content = ft.Column(
            spacing=10,
            controls=[
                ft.Text("Dashboard"),
                ft.Text("Contenido"),
            ]
        )