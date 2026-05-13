import flet as ft
import asyncio


class ModalLegajo:

    def __init__(self, page):
        self.page = page

        # =========================
        # LOADER
        # =========================
        self.loading = ft.ProgressRing(visible=False)

        COMMON_HEIGHT = 55

        # =========================
        # CAMPOS
        # =========================
        self.txt_cuil = ft.TextField(
            label="CUIL",
            width = 350,
            height=70,
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=11,
            on_change=self.solo_numeros,
        )

        self.txt_apellido = ft.TextField(
            label="Apellido",
            expand=True,
            height=COMMON_HEIGHT,
        )

        self.txt_nombre = ft.TextField(
            label="Nombre",
            expand=True,
            height=COMMON_HEIGHT,
        )

        self.ddl_sexo = ft.Dropdown(
            label="Sexo",
            expand=True,
            height=COMMON_HEIGHT,
            options=[
                ft.dropdown.Option("M"),
                ft.dropdown.Option("F"),
            ],
        )

        self.ddl_categoria = ft.Dropdown(
            label="Categoría",
            expand=True,
            height=COMMON_HEIGHT,
            options=[
                ft.dropdown.Option("Administrativo"),
                ft.dropdown.Option("Supervisor"),
                ft.dropdown.Option("Guardia"),
            ],
        )

        self.ddl_modalidad = ft.Dropdown(
            label="Modalidad",
            expand=True,
            height=70,
            options=[
                ft.dropdown.Option("Mensual"),
                ft.dropdown.Option("Jornal"),
            ],
        )

        self.txt_telefono = ft.TextField(
            label="Teléfono",
            expand=True,
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=15,
            on_change=self.solo_numeros,
        )

        self.chk_sac = ft.Checkbox(label="SAC", value=False)
        self.chk_activo = ft.Checkbox(label="Activo", value=True)

        # =========================
        # DIALOG
        # =========================
        self.dialog = ft.AlertDialog(
            modal=True,
            bgcolor="white",
            shape=ft.RoundedRectangleBorder(radius=0),
            content_padding=0,
            inset_padding=20,
            content=ft.Container(
                width=750,
                padding=20,
                content=ft.Column(
                    tight=True,
                    spacing=15,
                    controls=[

                        # HEADER
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    spacing=2,
                                    controls=[
                                        ft.Text("Nuevo Legajo", size=18, weight=ft.FontWeight.BOLD),
                                        ft.Text("Complete los datos del empleado", size=11, color="#64748B"),
                                    ],
                                ),
                                ft.IconButton(icon=ft.Icons.CLOSE, on_click=self.cerrar),
                            ],
                        ),

                        ft.Divider(),

                        # =========================
                        # FORM
                        # =========================
                        ft.Column(
                            spacing=12,
                            controls=[

                                ft.Row([self.txt_cuil]),

                                ft.Row([self.txt_apellido, self.txt_nombre]),

                                ft.Row([self.ddl_sexo, self.ddl_categoria]),

                                # 🔥 PERFECTAMENTE ALINEADOS
                                ft.Row(
                                    spacing=10,
                                    controls=[
                                        self.ddl_modalidad,
                                        self.txt_telefono,
                                    ],
                                ),

                                ft.Row([self.chk_sac, self.chk_activo]),
                            ],
                        ),

                        ft.Divider(),

                        # FOOTER
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                self.loading,
                                ft.OutlinedButton("Cancelar", on_click=self.cerrar),
                                ft.FilledButton("Guardar", on_click=self.guardar),
                            ],
                        ),
                    ],
                ),
            ),
        )

        self.page.overlay.append(self.dialog)

    # =========================
    # ABRIR
    # =========================
    async def abrir_nuevo(self, e):
        self.limpiar()
        self.dialog.open = True
        self.page.update()

    # =========================
    # CERRAR
    # =========================
    async def cerrar(self, e):
        self.dialog.open = False
        self.page.update()

    # =========================
    # LIMPIAR
    # =========================
    def limpiar(self):

        # =========================
        # TEXTFIELDS
        # =========================
        self.txt_cuil.value = ""
        self.txt_apellido.value = ""
        self.txt_nombre.value = ""
        self.txt_telefono.value = ""

        # limpiar errores visuales
        self.txt_cuil.error = None
        self.txt_apellido.error = None
        self.txt_nombre.error = None
        self.txt_telefono.error = None

        # =========================
        # DROPDOWNS
        # =========================
        self.ddl_sexo.value = None
        self.ddl_categoria.value = None
        self.ddl_modalidad.value = None

        self.ddl_sexo.error_text = None
        self.ddl_categoria.error_text = None
        self.ddl_modalidad.error_text = None

        # =========================
        # CHECKBOX
        # =========================
        self.chk_sac.value = False
        self.chk_activo.value = True

        # =========================
        # UPDATE UI
        # =========================
        self.txt_cuil.update()
        self.txt_apellido.update()
        self.txt_nombre.update()
        self.txt_telefono.update()

        self.ddl_sexo.update()
        self.ddl_categoria.update()
        self.ddl_modalidad.update()

        self.chk_sac.update()
        self.chk_activo.update()

        self.page.update()
    
    # VALIDACIÓN
    # =========================
    async def validar_formulario(self):

        valido = True
        primer_error = None
         # reset errores
      
         # CUIL (simple validación)
        if not self.txt_cuil.value:
            self.txt_cuil.error = "El CUIL es obligatorio"
            self.txt_cuil.update()
            valido = False
            if not primer_error:
                primer_error = self.txt_cuil

        # APELLIDO
        if not self.txt_apellido.value:
            self.txt_apellido.error = "Apellido obligatorio"
            self.txt_apellido.update()
            valido = False
            if not primer_error:
                primer_error = self.txt_apellido
        else:
            self.txt_apellido.error = None
            self.txt_apellido.update()

        # NOMBRE
        if not self.txt_nombre.value:
            self.txt_nombre.error = "Nombre obligatorio"
            self.txt_nombre.update()
            valido = False
            if not primer_error:
                primer_error = self.txt_nombre
        else:
            self.txt_nombre.error = None
            self.txt_nombre.update()
         # SEXO
        if not self.ddl_sexo.value:
            self.ddl_sexo.error_text = "Seleccione sexo"
            valido = False
         # SEXO
        if not self.ddl_categoria.value:
            self.ddl_categoria.error_text = "Seleccione categoria"
            valido = False
        if not self.ddl_modalidad.value:
            self.ddl_modalidad.error_text = "Seleccione modalidad"
            valido = False    
       

        self.page.update()


        if primer_error:
            await primer_error.focus()

        return valido

    # =========
    # =========================
    # GUARDAR
    # =========================
    async def guardar(self, e):

        if not await self.validar_formulario():
            return

        self.loading.visible = True
        self.page.update()

        try:
            await asyncio.sleep(1)

            self.dialog.open = False

            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Guardado correctamente"),
                bgcolor="green",
            )
            self.page.snack_bar.open = True

        finally:
            self.loading.visible = False
            self.page.update()

    # =========================
    # SOLO NÚMEROS
    # =========================
    def solo_numeros(self, e):
        limpio = "".join(filter(str.isdigit, e.control.value or ""))
        if e.control.value != limpio:
            e.control.value = limpio
            e.control.update()