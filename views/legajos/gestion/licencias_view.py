import flet as ft


class LicenciasView(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.page_ref = page

        # =========================
        # CAMPOS FORMULARIO
        # =========================
        self.tipo_licencia = ft.Dropdown(
            label="Tipo de licencia",
            width=400,
            options=[
                ft.dropdown.Option("Enfermedad"),
                ft.dropdown.Option("Vacaciones"),
                ft.dropdown.Option("Maternidad"),
                ft.dropdown.Option("Sin goce de haberes"),
            ]
        )

        self.fecha_desde = ft.TextField(
            label="Fecha desde (YYYY-MM-DD)",
            width=400
        )

        self.fecha_hasta = ft.TextField(
            label="Fecha hasta (YYYY-MM-DD)",
            width=400
        )

        self.observacion = ft.TextField(
            label="Observación",
            width=600,
            multiline=True,
            min_lines=2,
            max_lines=4
        )

        # =========================
        # BOTONES
        # =========================
        self.btn_agregar = ft.ElevatedButton(
            content=ft.Text("Guardar cambios"),
            icon=ft.Icons.ADD,
            on_click=self.agregar_licencia
        )

        self.btn_limpiar = ft.OutlinedButton(
            content=ft.Text("Limpiar"),
            icon=ft.Icons.CLEAR,
            on_click=self.limpiar_formulario
        )

        # =========================
        # LISTADO (SIMULADO)
        # =========================
        self.lista = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=False
        )

        # =========================
        # UI
        # =========================
        self.content = self.build()

        # datos demo
        self.licencias = []

    def build(self):
        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.Text("Licencias", size=22, weight=ft.FontWeight.BOLD),

                # ================= FORM =================
                ft.Container(
                    padding=15,
                    bgcolor="#F1F5F9",
                    border_radius=10,
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            self.tipo_licencia,
                            ft.Row([self.fecha_desde, self.fecha_hasta]),
                            self.observacion,
                            ft.Row(
                                controls=[
                                    self.btn_agregar,
                                    self.btn_limpiar
                                ],
                                alignment=ft.MainAxisAlignment.END
                            )
                        ]
                    )
                ),

                # ================= LISTA =================
                ft.Text("Historial de licencias", size=18),
                ft.Container(
                    expand=True,
                    padding=10,
                    border=ft.Border(
                                top=ft.BorderSide(1, "#E2E8F0"),
                                bottom=ft.BorderSide(1, "#E2E8F0"),
                                left=ft.BorderSide(1, "#E2E8F0"),
                                right=ft.BorderSide(1, "#E2E8F0"),
                    ),
                    border_radius=10,
                    content=self.lista
                )
            ]
        )

    def agregar_licencia(self, e):

        licencia = {
            "tipo": self.tipo_licencia.value,
            "desde": self.fecha_desde.value,
            "hasta": self.fecha_hasta.value,
            "obs": self.observacion.value,
        }

        self.licencias.append(licencia)

        self.lista.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Column(
                        controls=[
                            ft.Text(f"Tipo: {licencia['tipo']}"),
                            ft.Text(f"Desde: {licencia['desde']} - Hasta: {licencia['hasta']}"),
                            ft.Text(f"Obs: {licencia['obs']}")
                        ]
                    )
                )
            )
        )

        self.page.update()

    def limpiar_formulario(self, e):
        self.tipo_licencia.value = None
        self.fecha_desde.value = ""
        self.fecha_hasta.value = ""
        self.observacion.value = ""

        self.page.update()