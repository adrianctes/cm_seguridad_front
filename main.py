import flet as ft

from components.layout import Layout


def main(page: ft.Page):

    page.title = "Sistema Integral Seguridad"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0

    app = Layout(page)

    page.add(app.build())

    page.update()


ft.run(main)