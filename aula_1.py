import flet as ft


def main(page: ft.Page):
    # page.bgcolor = 'green'
    # page.bgcolor = '#818212'
    page.bgcolor = ft.colors.AMBER

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.padding = 20
    page.spacing = 100
    page.title = 'flet App'
    page.window_always_on_top = True
    page.window_title_bar_hidden = False
    page.window.frameless = False
    page.window_full_screen = False
    page.window_height = 300
    page.window_max_height = 900
    page.window_min_height = 200
    page.window_width = 300
    page.window_min_width = 200
    page.window_max_width = 900
    page.window.resizable = True
    page.window.top = 100
    page.window.left = 100
    page.window.movable = True
    page.window.prevent_close = True
    page.window.progress_bar = 1
    print(page.platform)


    def page_resize(e):
        print('tamanho:', page.window_width, page.window.height)


    #page.on_resize = page_resize

    def window_event(e):
        match e.data:
            case 'moved':
                print('moveu a pagina')
            case 'resized':
                print('tela redimensionada')
            case 'minimize':
                print('minimizou')
            case _:
                print('outra acao')

    page.on_window_event = window_event

    mensagem = ft.Text(value='Olá Mundo!', bgcolor='black')
    page.add(mensagem)

    elementos = [
        ft.Text(value='novidade'),
        ft.Text(value='testando'),
        ft.Text(value='testando'),
        ft.Text(value='ultima linha')
    ]

    page.add(*elementos)

    page.update()


ft.app(target=main)