import flet as ft

def main(page: ft.Page):
    # Crie uma imagem
    img = ft.Image(
        src="gmail.png",  # Caminho para a imagem
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    # Crie um layout de linha para o botão e a imagem
    images = ft.Row(expand=1, wrap=False, scroll="always")
    page.add(img, images)

    # Adicione a imagem ao botão
    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

ft.app(target=main)
