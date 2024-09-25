import flet as ft




def main(page: ft.Page):
    img = ft.Image(
        src='https://learnersgalaxy.ai/wp-content/uploads/2024/01/Python-Symbol.png',
        border_radius=ft.border_radius.horizontal(left=10, right=20),
        height=100,
        width=400,
        fit=ft.ImageFit.FIT_HEIGHT,
        repeat=ft.ImageRepeat.REPEAT,


    )

    img2 = ft.Image(
        src='assets/images/pp.png',
        tooltip='logo da SEAP-PB',
        src_base64=''

    )

    page.add(img, img2)



ft.app(target=main, assets_dir='assets')