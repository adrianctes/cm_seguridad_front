import flet as ft


class HistoriaView(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.page_ref = page

        # =========================
        # CAMPOS
        # =========================
        self.fecha = ft.TextField(
            label="Fecha (YYYY-MM-DD)",
            width=300
        )

        self.descripcion = ft.TextField(
            label="Descripción del hecho",
            width=600,
            multiline=True,
            min_lines=2,
            max_lines=4
        )

        # =========================
        # BOTÓN
        # =========================
        self.btn_agregar = ft.ElevatedButton(
            content=ft.Text("Agregar evento"),
            icon=ft.Icons.ADD,
            on_click=self.agregar_evento
        )

        # =========================
        # LISTA
        # =========================
        self.lista = ft.ListView(expand=True, spacing=10)

        self.eventos = []

        self.content = self.build()

    def build(self):
        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.Text("Historia del Legajo", size=22, weight=ft.FontWeight.BOLD),

                self.fecha,
                self.descripcion,

                ft.Row([self.btn_agregar], alignment=ft.MainAxisAlignment.END),

                ft.Divider(),

                self.lista
            ]
        )

    def agregar_evento(self, e):

        evento = {
            "fecha": self.fecha.value,
            "descripcion": self.descripcion.value
        }

        self.eventos.append(evento)

        self.lista.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column([
                        ft.Text(f"Fecha: {evento['fecha']}"),
                        ft.Text(evento['descripcion'])
                    ])
                )
            )
        )

        self.page.update()