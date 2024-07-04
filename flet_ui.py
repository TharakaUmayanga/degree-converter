import flet as ft
from flet_core import theme


def main(page: ft.Page):
    header_text = ft.Text("Degrees Converter", size=45, weight=ft.FontWeight.BOLD
                          )

    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE))
    page.theme_mode = ft.ThemeMode.LIGHT

    page.update()

    info_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Degrees to DMS"),
                    ft.TextField(label="Enter Degrees"),

                    ft.TextButton("Calculate")
                ],

            ),
            width=400,
            padding=10,

        )
    )
    header_row = ft.Row(
        [
            header_text,

        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    middle_col = ft.Column([
        ft.Row(
            [
                info_card
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )]

    )

    page.add(header_row)
    page.add(middle_col)


ft.app(main)
