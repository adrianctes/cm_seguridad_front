import flet as ft


class FamiliaresView(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.page_ref = page

        # =========================
        # CAMPOS
        # =========================
        self.nombre = ft.TextField(label="Nombre y Apellido", width=400)

        self.parentesco = ft.Dropdown(
            label="Parentesco",
            width=300,
            options=[
                ft.dropdown.Option("Padre"),
                ft.dropdown.Option("Madre"),
                ft.dropdown.Option("Hijo/a"),
                ft.dropdown.Option("Cónyuge"),
                ft.dropdown.Option("Otro"),
            ]
        )

        self.dni = ft.TextField(label="DNI", width=200)

        self.telefono = ft.TextField(label="Teléfono", width=250)

        # =========================
        # BOTÓN
        # =========================
        self.btn_agregar = ft.ElevatedButton(
             content=ft.Text("Agregar familiar"),
            icon=ft.Icons.PERSON_ADD,
            on_click=self.agregar_familiar
        )

        # =========================
        # LISTA
        # =========================
        self.lista = ft.ListView(expand=True, spacing=10)

        self.familiares = []

        self.content = self.build()

    def build(self):
        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.Text("Familiares", size=22, weight=ft.FontWeight.BOLD),

                self.nombre,
                ft.Row([self.parentesco, self.dni, self.telefono]),

                ft.Row([self.btn_agregar], alignment=ft.MainAxisAlignment.END),

                ft.Divider(),

                self.lista
            ]
        )

    def agregar_familiar(self, e):

        familiar = {
            "nombre": self.nombre.value,
            "parentesco": self.parentesco.value,
            "dni": self.dni.value,
            "telefono": self.telefono.value
        }

        self.familiares.append(familiar)

        self.lista.controls.append(
            ft.Card(
                content=ft.Container(
                    padding=10,
                    content=ft.Row([
                        ft.Text(f"{familiar['nombre']} - {familiar['parentesco']}"),
                        ft.Text(f"DNI: {familiar['dni']}"),
                        ft.Text(f"Tel: {familiar['telefono']}")
                    ], wrap=True)
                )
            )
        )

        self.page.update()