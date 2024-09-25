import flet as ft


def main(page: ft.page):
    page.fonts = {
        'Kanit': '',
        'Dragon Slayer': 'fonts/Dragon Slayer.ttf'
    }
    t1 = ft.Text(
        value='Olá Mundo, seja bem-vindo',
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
      #  font_family='Dragon Slayer',
        italic=True,
        #max_lines=5,
        #overflow=ft.TextOverflow.ELLIPSIS,
        no_wrap=True,
        selectable=False,
        size=100,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.W_100

    )

    link_style = ft.TextStyle(color=ft.colors.BLUE, decoration=ft.TextDecoration.UNDERLINE)

    t2 = ft.Text(
        spans= [
            ft.TextSpan(text='Texto com link ', style=link_style, url='https://google.com'),
            ft.TextSpan(text='continua...'),
            ft.TextSpan(text='Texto em Destaque!!!')
        ],
        size=40
    )

    page.add(t1, t2)

ft.app(target=main, assets_dir='assets')