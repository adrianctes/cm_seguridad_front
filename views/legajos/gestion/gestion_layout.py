import flet as ft

from views.legajos.gestion.legajo_sidebar_view import Sidebar
from views.legajos.gestion.editar_view import EditarView
from views.legajos.gestion.licencias_view import LicenciasView
from views.legajos.gestion.historial_view import HistoriaView
from views.legajos.gestion.familiares_view import FamiliaresView
from views.legajos.gestion.sanciones_view import SancionesView


class GestionLegajoLayout(ft.Container):

    def __init__(self, page):
        super().__init__()

        self.page_ref = page
        self.padding = -10          
        # =========================
        # VIEWS
        # =========================
        self.views = {
            "editar": EditarView(page),
            "licencias": LicenciasView(page),
            "historia": HistoriaView(page),
            "familiares": FamiliaresView(page),
            "sanciones": SancionesView(page),
        }

        self.current_key = "editar"

        # =========================
        # SIDEBAR
        # =========================
        self.sidebar = Sidebar(page, self.change_view)

        # IMPORTANTE: usar build()
        self.sidebar_view = self.sidebar.build()

        self.sidebar.set_default_item()

        # =========================
        # MAIN VIEW
        # =========================
        self.current_key = "editar"

        self.main_container = ft.Container(
            expand=True,
            content=self.views["editar"]
        )

        self.sidebar.set_default_item()

        # =========================
        # LAYOUT FINAL
        # =========================
        self.content = self.build_layout()

    def build_layout(self):
        return ft.Row(
            expand=True,
            controls=[
                self.sidebar_view,
                self.main_container
            ]
        )

    def change_view(self, route):

        if route not in self.views:
            return

        self.current_key = route
        self.main_container.content = self.views[route]

        self.page_ref.update()

    def load(self):

        # reset sidebar
        self.sidebar.set_default_item()

        # reset view
        self.current_key = "editar"

        self.main_container.content = self.views["editar"]

        # refresh
        self.page_ref.update()

        return self