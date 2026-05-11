import flet as ft


class ModalLegajo:

    def __init__(self, page: ft.Page):

        self.page = page

        # =========================
        # ESTADO
        # =========================
        self.modo = "NUEVO"
        self.legajo_id = None

        # =========================
        # CAMPOS
        # =========================

        self.txt_cuil = ft.TextField(label="CUIL")

        self.txt_apellido = ft.TextField(
            label="Apellido",
            expand=True
        )

        self.txt_nombre = ft.TextField(
            label="Nombre",
            expand=True
        )

        self.dd_sexo = ft.Dropdown(
            label="Sexo",
            options=[
                ft.dropdown.Option("Masculino"),
                ft.dropdown.Option("Femenino"),
                ft.dropdown.Option("X"),
            ]
        )

        self.dd_categoria = ft.Dropdown(
            label="Categoría",
            options=[
                ft.dropdown.Option(key=1, text="Administrativo"),
                ft.dropdown.Option(key=2, text="Supervisor"),
                ft.dropdown.Option(key=3, text="Guardia"),
            ]
        )

        self.dd_modalidad = ft.Dropdown(
            label="Modalidad",
            options=[
                ft.dropdown.Option(key=1, text="Mensual"),
                ft.dropdown.Option(key=2, text="Contratado"),
            ]
        )

        self.chk_activo = ft.Checkbox(label="Activo", value=True)
        self.chk_sac = ft.Checkbox(label="SAC", value=False)

        # =========================
        # DIALOG
        # =========================

        self.dialog = ft.AlertDialog(
            modal=True,

            title=ft.Text(
                "Legajo",
                size=16,
                weight=ft.FontWeight.W_500
            ),

            shape=ft.RoundedRectangleBorder(
                radius=0
            ),

            content=ft.Container(
                width=450,
                height=350,
                padding=10,

                content=ft.Column(
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[

                        self.txt_cuil,
                        self.txt_apellido,
                        self.txt_nombre,

                        ft.Row(
                            spacing=10,
                            controls=[
                                self.dd_sexo,
                                self.dd_categoria
                            ]
                        ),

                        self.dd_modalidad,

                        ft.Row(
                            spacing=15,
                            controls=[
                                self.chk_activo,
                                self.chk_sac
                            ]
                        ),
                    ]
                )
            ),

            actions=[
                ft.TextButton("Cancelar", on_click=self.cerrar),

                ft.FilledButton(
                    "Guardar",
                    bgcolor="#2563EB",
                    color="white",
                    on_click=self.guardar
                )
            ]
        )

        # agregar UNA sola vez
        self.page.overlay.append(self.dialog)

    # =========================
    # ABRIR NUEVO
    # =========================

    def abrir_nuevo(self, e=None):

        self.modo = "NUEVO"
        self.legajo_id = None

        self.limpiar()

        self.dialog.title = ft.Text("Nuevo Legajo")
        self.dialog.open = True
        self.page.update()

    # =========================
    # ABRIR EDITAR
    # =========================

    def abrir_editar(self, legajo, e=None):

        self.modo = "EDITAR"
        self.legajo_id = legajo["id"]

        self.txt_cuil.value = legajo["cuil"]
        self.txt_apellido.value = legajo["apellido"]
        self.txt_nombre.value = legajo["nombre"]

        self.dd_sexo.value = legajo["sexo"]
        self.dd_categoria.value = legajo["categoria_id"]
        self.dd_modalidad.value = legajo["modalidad_liquidacion_id"]

        self.chk_activo.value = legajo["activo"]
        self.chk_sac.value = legajo["sac"]

        self.dialog.title = ft.Text("Editar Legajo")
        self.dialog.open = True
        self.page.update()

    # =========================
    # GUARDAR
    # =========================

    def guardar(self, e):

        data = {
            "id": self.legajo_id,
            "cuil": self.txt_cuil.value,
            "apellido": self.txt_apellido.value,
            "nombre": self.txt_nombre.value,
            "sexo": self.dd_sexo.value,
            "categoria_id": self.dd_categoria.value,
            "modalidad_liquidacion_id": self.dd_modalidad.value,
            "activo": self.chk_activo.value,
            "sac": self.chk_sac.value
        }

        if not data["apellido"] or not data["nombre"]:
            print("Apellido y Nombre son obligatorios")
            return

        if self.modo == "NUEVO":
            print("CREAR:", data)
        else:
            print("ACTUALIZAR:", data)

        self.cerrar()

    # =========================
    # CERRAR
    # =========================

    def cerrar(self, e=None):

        self.dialog.open = False
        self.page.update()

    # =========================
    # LIMPIAR
    # =========================

    def limpiar(self):

        self.txt_cuil.value = ""
        self.txt_apellido.value = ""
        self.txt_nombre.value = ""

        self.dd_sexo.value = None
        self.dd_categoria.value = None
        self.dd_modalidad.value = None

        self.chk_activo.value = True
        self.chk_sac.value = False