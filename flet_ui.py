import flet as ft


def main(page: ft.Page):
    header_text = ft.Text("Degrees Converter", size=45, weight=ft.FontWeight.BOLD
                          )
    header_row = ft.Row(
        [
            header_text,


        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    info_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("The Enchanted Nightingale"),
                        subtitle=ft.Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein."
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        ))
    page.add(header_row)


ft.app(main)
