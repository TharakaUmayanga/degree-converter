import flet as ft


def main(page: ft.Page):
    header_text = ft.Text("Degrees Converter", size=45, weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER,width=float("inf"),)
    header_column = ft.Column(
      [
          header_text,

      ]
    )
    page.add(header_column)



ft.app(main)
