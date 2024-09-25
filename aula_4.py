import flet as ft


def main(page : ft.Page):
    icon1 = ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK)
    icon2 = ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.GREEN_400, size=50)
    icon3 = ft.Icon(name=ft.icons.RECENT_ACTORS, color=ft.colors.BLUE, size=50)
    icon4 = ft.Icon(name='settings', color='#c1c1c1', size=50, tooltip='configuracoes')

    page.add(icon1, icon2, icon3, icon4)




ft.app(target=main)