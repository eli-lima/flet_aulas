import flet as ft


def main(page : ft.Page):

    page.spacing = 50

    btn1 = ft.ElevatedButton(text='Clique aqui')
    btn2 = ft.ElevatedButton(text='Clique inativo', disabled=True)
    btn3 = ft.ElevatedButton(text='Botao com icone', icon=ft.icons.FAVORITE)
    btn4 = ft.ElevatedButton(text='demais propriedades',
                             bgcolor=ft.colors.RED,
                             color=ft.colors.BLACK,
                             icon=ft.icons.FAVORITE_OUTLINE,
                             icon_color=ft.colors.WHITE,
                             tooltip='Olá eu sou um botao',
                             url='https://google.com'
                             )


    page.add(btn1, btn2, btn3, btn4)

ft.app(target=main)