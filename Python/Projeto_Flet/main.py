import flet as ft


def main(pagina: ft.Page):
   

    pagina.title = "Meu app flet"

    pagina.window_width = 300
    pagina.window_height = 300
    pagina.bgcolor = "black"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER



    def subtrair(e):
        caixa_texto.value = int(caixa_texto.value)
        caixa_texto.value -= 1
        caixa_texto.value = str(caixa_texto.value)
        pagina.update()
        pass
    
    def somar(e):
        caixa_texto.value = str(int(caixa_texto.value) + 1)
        pagina.update()
     
        pass


    #CRIANDO OS ELEMETNOS
    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=subtrair)
    caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER, color="Blue", border_color="blue")
   

    botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar)

    #ADICIONANDO NA PÁGINA

    pagina.add(
        
        ft.Row([botao_menos, caixa_texto, botao_mais], alignment=ft.MainAxisAlignment.CENTER)
      
    )

    pass



ft.app(target=main)

