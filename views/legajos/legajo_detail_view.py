import flet as ft


class LegajoDetailView(ft.Column):

    def __init__(self, page, service, legajo_id):
        super().__init__()
        self.page = page
        self.service = service

        legajo = self.service.obtener_por_id(legajo_id)

        self.controls = [
            ft.Text(f"Apellido: {legajo.apellido}"),
            ft.Text(f"Nombre: {legajo.nombre}"),
            ft.Text(f"CUIL: {legajo.cuil}"),
            ft.Text(f"Activo: {legajo.activo}"),
            ft.ElevatedButton("Volver", on_click=lambda e: page.go("/legajos"))
        ]