import flet as ft

from fastapi import FastAPI

from flet_web.fastapi import app as flet_app

from components.layout import Layout


app = FastAPI()


async def main(page: ft.Page):

    page.title = "Sistema Integral Seguridad"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.padding = 0

    page.spacing = 0

    page.bgcolor = "#F1F5F9"
    

    # =====================================
    # LAYOUT
    # =====================================

    layout = Layout(page)

    page.layout = layout

    page.add(
        layout.build()
    )

    # =====================================
    # VIEW INICIAL
    # =====================================

    layout.change_view("dashboard")

    page.update()

   
# =====================================
# FLET APP
# =====================================

app.mount("/", flet_app(main))