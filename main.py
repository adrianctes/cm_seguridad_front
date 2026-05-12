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

    layout = Layout(page)

    page.add(layout.build())

    page.update()


app.mount("/", flet_app(main))