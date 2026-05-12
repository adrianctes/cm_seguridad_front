import flet as ft

from services.legajo_service import LegajoService

from components.sidebar import Sidebar

from views.legajos.legajo_list_view import LegajosView


class Layout:

    def __init__(self, page: ft.Page):

        self.page = page

        # =========================
        # SERVICES
        # =========================

        self.legajo_service = LegajoService()

        # =========================
        # SIDEBAR
        # =========================

        self.sidebar = Sidebar(
            page,
            self.change_view
        )

        # =========================
        # VIEWS
        # =========================

        self.views = {

            "dashboard": ft.Container(

                expand=True,

                content=ft.Column(

                    controls=[

                        ft.Text(
                            "Dashboard",
                            size=32,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            "Bienvenido al sistema",
                            color="grey"
                        )
                    ]
                )
            ),

            "legajos": LegajosView(page)

        }

        # =========================
        # CONTENT
        # =========================

        self.content = ft.Container(

            expand=True,

            padding=20,

            content=self.views["dashboard"]

        )

    # ==================================
    # BUILD
    # ==================================

    def build(self):

        return ft.Row(

            expand=True,

            controls=[

                self.sidebar.build(),

                self.content

            ]
        )

    # ==================================
    # CHANGE VIEW
    # ==================================

    def change_view(self, view_name):

        if view_name in self.views:

            vista = self.views[view_name]

            self.content.content = vista

            # =====================================
            # RECARGAR LEGJOS
            # =====================================

            if view_name == "legajos":

                self.page.run_task(
                    vista.listar_legajos
                )

        else:

            self.content.content = ft.Container(

                content=ft.Text(
                    f"Vista '{view_name}' en construcción",
                    size=26
                )
            )

        self.page.update()