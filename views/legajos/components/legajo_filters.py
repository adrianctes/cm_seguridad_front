import flet as ft


class LegajoFilters:

    def __init__(self, on_filter):
        self.on_filter = on_filter

        self.apellido = ft.TextField(label="Apellido")
        self.cuil = ft.TextField(label="CUIL")

    def build(self):
        return ft.Row([
            self.apellido,
            self.cuil,
            ft.ElevatedButton("Filtrar", on_click=self.filtrar)
        ])

    def filtrar(self, e):
        self.on_filter({
            "apellido": self.apellido.value,
            "cuil": self.cuil.value
        })