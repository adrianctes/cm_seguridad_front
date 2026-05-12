import flet as ft
import asyncio


class ModalLegajo:

    def __init__(self, page):

        self.page = page

        # =========================
        # LOADER
        # =========================
        self.loading = ft.ProgressRing(
            visible=False,
            width=18,
            height=18
        )

        # =========================
        # CAMPOS
        # =========================
        self.txt_cuil = ft.TextField(label="CUIL", expand=True)
        self.txt_apellido = ft.TextField(label="Apellido", expand=True)
        self.txt_nombre = ft.TextField(label="Nombre", expand=True)

        self.ddl_sexo = ft.Dropdown(
            label="Sexo",
            expand=True,
            options=[
                ft.dropdown.Option("M"),
                ft.dropdown.Option("F"),
            ]
        )

        self.ddl_categoria = ft.Dropdown(
            label="Categoría",
            expand=True,
            options=[
                ft.dropdown.Option("A"),
                ft.dropdown.Option("B"),
                ft.dropdown.Option("C"),
            ]
        )

        self.ddl_modalidad = ft.Dropdown(
            label="Modalidad",
            expand=True,
            options=[
                ft.dropdown.Option("Planta"),
                ft.dropdown.Option("Contratado"),
                ft.dropdown.Option("Temporal"),
            ]
        )

        self.chk_sac = ft.Checkbox(label="SAC", value=False)
        self.chk_activo = ft.Checkbox(label="Activo", value=True)

        self.txt_cuil = ft.TextField(label="CUIL", expand=True,
                                   keyboard_type=ft.KeyboardType.NUMBER,
                                   max_length=13,
                                   on_change=self.solo_numeros_cuil)

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
                    spacing=16,

                    controls=[

                        # HEADER
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    spacing=2,
                                    controls=[
                                        ft.Text(
                                            "Nuevo Legajo",
                                            size=18,
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        ft.Text(
                                            "Complete los datos del empleado",
                                            size=11,
                                            color="#64748B"
                                        )
                                    ]
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.CLOSE,
                                    on_click=self.cerrar
                                )
                            ]
                        ),

                        ft.Divider(),

                        # =========================
                        # FORM (FIX AQUÍ)
                        # =========================
                        ft.Column(

                            spacing=12,

                            controls=[
                                ft.Row([
                                    ft.Column(
                                        controls=[self.txt_cuil],
                                       # expand=True,
                                        width=350
                                    ),
                                  
                                ]),
                                
                                ft.Row([
                                    self.txt_apellido,
                                    self.txt_nombre,
                                ]),
                                ft.Row([
                                   
                                    self.ddl_sexo,
                                    self.ddl_categoria,
                                ]),

                                

                                ft.Row([
                                    self.ddl_modalidad,
                                    self.chk_sac,
                                    self.chk_activo,
                                ]),

                               
                            ]
                        ),

                        ft.Divider(),

                        # FOOTER
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            spacing=10,
                            controls=[
                                self.loading,

                                ft.OutlinedButton(
                                    "Cancelar",
                                    on_click=self.cerrar
                                ),

                                ft.FilledButton(
                                    "Guardar",
                                    on_click=self.guardar
                                )
                            ]
                        )
                    ]
                )
            )
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
    # VALUES
    # =========================
        self.txt_apellido.value = ""
        self.txt_nombre.value = ""
        self.txt_cuil.value = ""

        self.ddl_sexo.value = None
        self.ddl_categoria.value = None
        self.ddl_modalidad.value = None

        self.chk_sac.value = False
        self.chk_activo.value = True

        # =========================
        # ERRORS (ESTO ES LO IMPORTANTE)
        # =========================
        self.txt_apellido.error = None
        self.txt_nombre.error = None
        self.txt_cuil.error = None

        self.ddl_sexo.error_text = None
        self.ddl_categoria.error_text = None
        self.ddl_modalidad.error_text = None

        self.ddl_sexo.helper_text = None
        self.ddl_categoria.helper_text = None
        self.ddl_modalidad.helper_text = None

        # =========================
        # UPDATE UI
        # =========================
        self.txt_apellido.update()
        self.txt_nombre.update()
        self.txt_cuil.update()

        self.ddl_sexo.update()
        self.ddl_categoria.update()
        self.ddl_modalidad.update()

        self.chk_sac.update()
        self.chk_activo.update()
    # =========================
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
            self.ddl_modalidad.error_text = "Seleccione categoria"
            valido = False    
       

        self.page.update()


        if primer_error:
            await primer_error.focus()

        return valido

    # =========================
    # GUARDAR
    # =========================
    async def guardar(self, e):

        if not await self.validar_formulario():
            return

        self.loading.visible = True
        self.page.update()

        try:

            data = {
                "apellido": self.txt_apellido.value,
                "nombre": self.txt_nombre.value,
                "sexo": self.ddl_sexo.value,
                "categoria": self.ddl_categoria.value,
                "modalidad": self.ddl_modalidad.value,
                "sac": self.chk_sac.value,
                "activo": self.chk_activo.value,
                "cuil": self.txt_cuil.value,
            }

            await asyncio.sleep(1)

            self.page.snack_bar = ft.SnackBar(
                content=ft.Text("Guardado correctamente"),
                bgcolor="green"
            )
            self.page.snack_bar.open = True

            self.dialog.open = False

        except Exception as ex:

            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Error: {ex}"),
                bgcolor="red"
            )
            self.page.snack_bar.open = True

        finally:

            self.loading.visible = False
            self.page.update()
    
    def solo_numeros_cuil(self, e):

        valor = e.control.value

        # deja solo dígitos
        limpio = "".join(filter(str.isdigit, valor))

        if valor != limpio:
            e.control.value = limpio
            e.control.update()