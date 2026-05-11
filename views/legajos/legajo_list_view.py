import flet as ft
from views.legajos.legajo_modal import ModalLegajo

class LegajosView(ft.Container):

    def __init__(self, page):

        super().__init__()

        self.page_ref = page
        self.modal_legajo = ModalLegajo(page)
        # =====================================
        # ESTADO
        # =====================================

        self.current_page = 1
        self.page_size = 10
        self.total_items = 0

        # =====================================
        # DATA MOCK
        # =====================================

        self.legajos = self.mock_data()

        # =====================================
        # CONFIG GENERAL
        # =====================================

        self.expand = True

        self.bgcolor = "#F1F5F9"

        self.padding = 25

        # =====================================
        # FILTROS
        # =====================================

        self.txt_busqueda = ft.TextField(

            hint_text="Buscar por DNI, apellido o nombre",

            prefix_icon=ft.Icons.SEARCH,

            border_radius=8,

            filled=True,

            bgcolor="white",
           
            border_color="#CBD5E1",

            expand=True,

            height=44
        )

        self.chk_activos = ft.Checkbox(
            label="Solo activos",
            value=True,
            active_color="#030813",
            check_color="white"
        )

        # =====================================
        # TABLA
        # =====================================

        self.table = ft.DataTable(

            expand=True,

            heading_row_color="#E2E8F0",

            data_row_min_height=58,

            data_row_max_height=58,

            border=ft.Border.all(
                1,
                "#E2E8F0"
            ),

            vertical_lines=ft.BorderSide(
                1,
                "#E2E8F0"
            ),

            horizontal_lines=ft.BorderSide(
                1,
                "#E2E8F0"
            ),

            heading_text_style=ft.TextStyle(
                size=13,
                weight=ft.FontWeight.BOLD,
                color="#0F172A"
            ),

            columns=[

                ft.DataColumn(ft.Text("Legajo")),

                ft.DataColumn(ft.Text("DNI")),

                ft.DataColumn(ft.Text("Apellido")),

                ft.DataColumn(ft.Text("Nombre")),

                ft.DataColumn(ft.Text("Estado")),

                ft.DataColumn(ft.Text("Acciones"))
            ],

            rows=[]
        )

        # =====================================
        # LABELS
        # =====================================

        self.lbl_total = ft.Text(
            "Total: 0",
            size=13,
            color="#64748B"
        )

        self.lbl_page = ft.Text(
            "",
            size=13,
            color="#475569"
        )

        # =====================================
        # CONTENIDO PRINCIPAL
        # =====================================

        self.content = ft.Column(

            expand=True,

            spacing=20,

            controls=[

                # =================================
                # HEADER
                # =================================

                ft.Row(

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                    controls=[

                        ft.Column(

                            spacing=2,

                            controls=[

                                ft.Text(
                                    "Legajos",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color="#0F172A"
                                ),

                                ft.Text(
                                    "Administración de personal",
                                    size=14,
                                    color="#64748B"
                                )
                            ]
                        ),

                        ft.FilledButton(

                            "Nuevo Legajo",

                            icon=ft.Icons.ADD,
                            on_click=self.modal_legajo.abrir_nuevo,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(
                                    radius=0
                                ),
                                bgcolor="#030B16",
                                padding=20
                            )
                        )
                    ]
                ),

                # =================================
                # FILTROS
                # =================================

                ft.Container(

                    bgcolor="white",

                    border_radius=0,

                    padding=20,

                    border=ft.Border.all(
                        1,
                        "#E2E8F0"
                    ),

                    content=ft.Row(

                        spacing=15,

                        controls=[

                            self.txt_busqueda,

                            self.chk_activos,

                            ft.FilledButton(

                                "Buscar",

                                icon=ft.Icons.SEARCH,

                                height=44,

                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(
                                        radius=0
                                    ),
                                    bgcolor="#030B16",
                                ),

                                on_click=self.buscar
                            )
                        ]
                    )
                ),

                # =================================
                # TABLA
                # =================================

                ft.Container(

                    expand=True,

                    bgcolor="white",

                    border_radius=0,

                    border=ft.Border.all(
                        1,
                        "#E2E8F0"
                    ),

                    padding=20,

                    content=ft.Column(

                        expand=True,

                        spacing=15,

                        controls=[

                            ft.Row(

                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                                controls=[

                                    ft.Text(
                                        "Listado de Legajos",
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color="#0F172A"
                                    ),

                                    self.lbl_total
                                ]
                            ),

                            ft.Divider(height=1),

                            ft.Container(

                                expand=True,

                                content=ft.ListView(
                                    expand=True,
                                    controls=[self.table]
                                )
                            ),

                            # =================================
                            # PAGINACION
                            # =================================

                            ft.Row(

                                alignment=ft.MainAxisAlignment.END,

                                spacing=5,

                                controls=[

                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_LEFT,
                                        on_click=self.prev_page
                                    ),

                                    self.lbl_page,

                                    ft.IconButton(
                                        icon=ft.Icons.CHEVRON_RIGHT,
                                        on_click=self.next_page
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )

        self.load_data()

    # =====================================
    # MOCK DATA
    # =====================================

    def mock_data(self):

        data = []

        for i in range(1, 53):

            data.append({

                "legajo": i,

                "dni": f"30{i:06}",

                "apellido": f"González {i}",

                "nombre": f"Juan {i}",

                "activo": i % 2 == 0
            })

        return data

    # =====================================
    # LOAD DATA
    # =====================================

    def load_data(self):

        self.table.rows.clear()

        filtro = (
            self.txt_busqueda.value or ""
        ).lower()

        activos = self.chk_activos.value

        data = [

            x for x in self.legajos

            if (

                filtro in x["dni"].lower()

                or filtro in x["apellido"].lower()

                or filtro in x["nombre"].lower()

            )

            and (

                x["activo"]
                if activos
                else True
            )
        ]

        self.total_items = len(data)

        self.lbl_total.value = (
            f"Total registros: {self.total_items}"
        )

        start = (
            (self.current_page - 1)
            * self.page_size
        )

        end = start + self.page_size

        paginated = data[start:end]

        for item in paginated:

            activo = item["activo"]

            self.table.rows.append(

                ft.DataRow(

                    cells=[

                        # LEGAJO

                        ft.DataCell(
                            ft.Text(str(item["legajo"]))
                        ),

                        # DNI

                        ft.DataCell(
                            ft.Text(item["dni"])
                        ),

                        # APELLIDO

                        ft.DataCell(
                            ft.Text(item["apellido"])
                        ),

                        # NOMBRE

                        ft.DataCell(
                            ft.Text(item["nombre"])
                        ),

                        # ESTADO

                        ft.DataCell(

                            ft.Container(

                                bgcolor=(
                                    "#DCFCE7"
                                    if activo
                                    else "#FEE2E2"
                                ),

                                border_radius=20,

                                padding=ft.Padding.symmetric(
                                    horizontal=12,
                                    vertical=5
                                ),

                                content=ft.Text(

                                    "Activo"
                                    if activo
                                    else "Inactivo",

                                    color=(
                                        "#166534"
                                        if activo
                                        else "#991B1B"
                                    ),

                                    size=12,

                                    weight=ft.FontWeight.W_500
                                )
                            )
                        ),

                        # =================================
                        # MENU CONTEXTUAL
                        # =================================

                        ft.DataCell(

                            ft.PopupMenuButton(

                                icon=ft.Icons.MORE_VERT,

                                items=[

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.VISIBILITY_OUTLINED,

                                        content=ft.Text(
                                            "Ver detalle"
                                        )
                                    ),

                                    ft.PopupMenuItem(),

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.GROUPS_OUTLINED,

                                        content=ft.Text(
                                            "Familiares"
                                        ),

                                        on_click=lambda e, item=item:
                                        self.open_familiares(item)
                                    ),

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.GAVEL_OUTLINED,

                                        content=ft.Text(
                                            "Sanciones"
                                        ),

                                        on_click=lambda e, item=item:
                                        self.open_sanciones(item)
                                    ),

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.EVENT_NOTE_OUTLINED,

                                        content=ft.Text(
                                            "Licencias"
                                        ),

                                        on_click=lambda e, item=item:
                                        self.open_licencias(item)
                                    ),

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.WORK_HISTORY_OUTLINED,

                                        content=ft.Text(
                                            "Historial laboral"
                                        ),

                                        on_click=lambda e, item=item:
                                        self.open_historial(item)
                                    ),

                                    ft.PopupMenuItem(),

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.EDIT_OUTLINED,

                                        content=ft.Text(
                                            "Editar"
                                        )
                                    ),

                                    ft.PopupMenuItem(

                                        icon=ft.Icons.DELETE_OUTLINE,

                                        content=ft.Text(
                                            "Eliminar"
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )

        total_pages = max(
            1,
            (self.total_items + self.page_size - 1)
            // self.page_size
        )

        self.lbl_page.value = (
            f"Página {self.current_page} de {total_pages}"
        )

    # =====================================
    # EVENTOS
    # =====================================

    def buscar(self, e):

        self.current_page = 1

        self.load_data()

        self.page_ref.update()

    def next_page(self, e):

        total_pages = max(
            1,
            (self.total_items + self.page_size - 1)
            // self.page_size
        )

        if self.current_page < total_pages:

            self.current_page += 1

            self.load_data()

            self.page_ref.update()

    def prev_page(self, e):

        if self.current_page > 1:

            self.current_page -= 1

            self.load_data()

            self.page_ref.update()

    # =====================================
    # MENU CONTEXTUAL
    # =====================================

    def open_familiares(self, item):

        self.show_message(
            f"Familiares del legajo {item['legajo']}"
        )

    def open_sanciones(self, item):

        self.show_message(
            f"Sanciones del legajo {item['legajo']}"
        )

    def open_licencias(self, item):

        self.show_message(
            f"Licencias del legajo {item['legajo']}"
        )

    def open_historial(self, item):

        self.show_message(
            f"Historial laboral del legajo {item['legajo']}"
        )

    # =====================================
    # UTIL
    # =====================================

    def show_message(self, text):

        self.page_ref.snack_bar = ft.SnackBar(
            content=ft.Text(text)
        )

        self.page_ref.snack_bar.open = True

        self.page_ref.update()