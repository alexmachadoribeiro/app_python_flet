import flet as ft


def main(page: ft.Page):
    def mostrar_texto(e):
        texto_saida.value = f"Texto inserido: {texto_entrada.value}"
        page.update()
    
    page.title = "Eventos"
    page.theme_mode = ft.ThemeMode.LIGHT

    texto_entrada = ft.TextField(label="Informe o seu nome: ")
    texto_saida = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Text(
                "Programação Orientada a Eventos",
                size=40,
                weight="bold"
            )
        ),
        texto_entrada,
        ft.ElevatedButton("Enviar", on_click=mostrar_texto),
        texto_saida
    )


ft.app(main)
