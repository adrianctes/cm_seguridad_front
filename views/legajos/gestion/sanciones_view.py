import flet as ft


class SancionesView(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.page_ref = page

        # =========================
        # CAMPOS
        # =========================
        self.tipo = ft.Dropdown(
            label="Tipo de sanción",
            width=300,
            options=[
                ft.dropdown.Option("Apercibimiento"),
                ft.dropdown.Option("Suspensión"),
                ft.dropdown.Option("Sumario"),
                ft.dropdown.Option("Llamado de atención"),
            ]
        )

        self.fecha = ft.TextField(label="Fecha (YYYY-MM-DD)", width=250)

        self.motivo = ft.TextField(
            label="Motivo",
            width=600,
            multiline=True,
            min_lines=2,
            max_lines=4
        )

        # =========================
        # BOTÓN
        # =========================
        self.btn_agregar = ft.ElevatedButton(
            content=ft.Text("Registrar sanción"),
            icon=ft.Icons.WARNING,
            on_click=self.agregar_sancion
        )

        # =========================
        # LISTA
        # =========================
        self.lista = ft.ListView(expand=True, spacing=10)

        self.sanciones = []

        self.content = self.build()

    def build(self):
        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.Text("Sanciones", size=22, weight=ft.FontWeight.BOLD),

                self.tipo,
                ft.Row([self.fecha]),
                self.motivo,

                ft.Row([self.btn_agregar], alignment=ft.MainAxisAlignment.END),

                ft.Divider(),

                self.lista
            ]
        )

    def agregar_sancion(self, e):

        sancion = {
            "tipo": self.tipo.value,
            "fecha": self.fecha.value,
            "motivo": self.motivo.value
        }

        self.sanciones.append(sancion)

        self.lista.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.Text(f"Tipo: {sancion['tipo']}"),
                        ft.Text(f"Fecha: {sancion['fecha']}"),
                        ft.Text(sancion['motivo'])
                    ])
                )
            )
        )

        self.page.update()