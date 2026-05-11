import flet as ft


class LegajoToolbar:

    def __init__(self, on_create):
        self.on_create = on_create

    def build(self):
        return ft.Row([
            ft.Text("Legajos", size=25, weight="bold"),
            ft.ElevatedButton(
                "Nuevo Legajo",
                icon="add",   # ✅ FIX
                on_click=self.on_create
            )
        ], alignment="spaceBetween")