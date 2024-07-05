import flet as ft
from flet_core import theme

from main import convert_to_dms, convert_to_degrees


def main(page: ft.Page):
    header_text = ft.Text("Degrees Converter", size=45, weight=ft.FontWeight.BOLD
                          )

    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.BLUE))
    page.theme_mode = ft.ThemeMode.LIGHT

    page.update()

    card_padding = 15

    deg_dms_txt = ft.Text()
    deg_dms_txt_input = ft.TextField(label="Enter Degrees")

    dms_deg_txt_deg = ft.TextField(label="Enter Degrees")
    dms_deg_txt_min = ft.TextField(label="Enter Minutes")
    dms_deg_txt_sec = ft.TextField(label="Enter Seconds")

    dms_deg_txt = ft.Text()

    def calculate_deg_dms_txt_clicked(e):
        try:
            degrees = float(deg_dms_txt_input.value)
            result = convert_to_dms(degrees)
            deg_dms_txt.value = result
            page.update()
        except ValueError:
            deg_dms_txt.value = "Please enter a valid number."
            page.update()

    def calculate_dms_deg_txt_clicked(e):
        try:
            degrees = float(dms_deg_txt_deg.value)
            mins = float(dms_deg_txt_min.value)
            sec = float(dms_deg_txt_sec.value)

            result = convert_to_degrees(degrees,mins,sec)
            dms_deg_txt.value = result
            page.update()
        except ValueError:
            deg_dms_txt.value = "Please enter a valid number."
            page.update()

    deg_dms_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Degrees to DMS"),
                    deg_dms_txt_input,
                    deg_dms_txt,

                    ft.FilledButton("Calculate", on_click=calculate_deg_dms_txt_clicked)
                ],

            ),
            width=400,
            padding=card_padding,

        ),

    )

    dms_deg_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("DMS to Deg"),
                    dms_deg_txt_deg,
                    dms_deg_txt_min,
                    dms_deg_txt_sec,
                    dms_deg_txt,
                    ft.FilledButton("Calculate", on_click=calculate_dms_deg_txt_clicked)
                ],

            ),
            width=400,
            padding=card_padding,

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
                deg_dms_card
            ],
            alignment=ft.MainAxisAlignment.CENTER

        ),
        ft.Row(
            [
                dms_deg_card
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )],
        spacing=30

    )

    page.add(header_row)
    page.add(middle_col)


ft.app(main)
