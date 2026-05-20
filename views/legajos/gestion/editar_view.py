import flet as ft


class EditarView(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.page_ref = page
        self.padding =20

        # =========================
        # CAMPOS
        # =========================
        self.txt_nombre = ft.TextField(
            label="Nombre",
            width=400
        )

        self.txt_apellido = ft.TextField(
            label="Apellido",
            width=400
        )

        self.txt_dni = ft.TextField(
            label="DNI",
            width=400,
            keyboard_type=ft.KeyboardType.NUMBER
        )

        self.txt_direccion = ft.TextField(
            label="Dirección",
            width=400
        )

        # =========================
        # BOTÓN
        # =========================
        self.btn_guardar = ft.ElevatedButton(
            content=ft.Text("Guardar cambios"),
            icon=ft.Icons.SAVE,
            on_click=self.guardar
        )

        # =========================
        # UI
        # =========================
        self.content = self.build()

    def build(self):
        return ft.Column(
            expand=True,
            spacing=20,
            controls=[
                ft.Text("Editar Legajo", size=22, weight=ft.FontWeight.BOLD),

                ft.Row([self.txt_nombre, self.txt_apellido]),
                self.txt_dni,
                self.txt_direccion,

                ft.Divider(),

                ft.Row(
                    controls=[self.btn_guardar],
                    alignment=ft.MainAxisAlignment.END
                )
            ]
        )

    async def guardar(self, e):
        data = {
            "nombre": self.txt_nombre.value,
            "apellido": self.txt_apellido.value,
            "dni": self.txt_dni.value,
            "direccion": self.txt_direccion.value,
        }

        print("Guardando:", data)

        # Acá después conectás tu API (httpx)
        # async with httpx.AsyncClient() as client:
        #     await client.put("http://api/legajo", json=data)

        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("Cambios guardados correctamente")
        )
        self.page.snack_bar.open = True
        self.page.update()