import flet as ft


class LegajoTable:

    def __init__(self, service):
        self.service = service
        self.data = ft.DataTable(columns=[
            ft.DataColumn(ft.Text("Apellido")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("CUIL")),
            ft.DataColumn(ft.Text("Acciones")),
        ])

    def build(self):
        self.load_data()
        return self.data

    def load_data(self, filtro=None):
        legajos = self.service.listar(filtro)

        self.data.rows.clear()

        for l in legajos:
            self.data.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(l.apellido)),
                    ft.DataCell(ft.Text(l.nombre)),
                    ft.DataCell(ft.Text(l.cuil)),
                    ft.DataCell(
                        ft.Row([
                            ft.IconButton(icon=ft.icons.EDIT),
                            ft.IconButton(icon=ft.icons.DELETE)
                        ])
                    )
                ])
            )