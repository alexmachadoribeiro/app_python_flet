import flet as ft


def main(page: ft.Page):
    def calcular_imc(e):
        if not peso.value:
            peso.error_text = "Peso não pode ficar vazio"
            page.update()
        else:
            peso.error_text = ""
            page.update()

        if not altura.value:
            altura.error_text = "Altura não pode ficar vazio"
            page.update()
        else:
            altura.error_text = ""

            peso.value = float(peso.value.replace(",", "."))
            altura.value = float(altura.value.replace(",", "."))

            if peso.value > 0 and altura.value > 0:
                imc = peso.value / altura.value**2
                peso.value = ""
                altura.value = ""
                result.value = f"O valor do IMC do usuário é: {imc:,.2f}."

                page.update()
            elif peso.value < 0 and altura.value > 0:
                peso.error_text = "Valor inválido."
                page.update()
            elif peso.value > 0 and altura.value < 0:
                altura.error_text = "Valor inválido."
                page.update()
            else:
                peso.error_text = "Valor inválido."
                altura.error_text = "Valor inválido."
                page.update()
    
    page.title = "IMC - Índice de Massa Corporal"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    peso = ft.TextField(
        label="Peso", 
        suffix_text="kg",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    altura = ft.TextField(
        label="Altura", 
        suffix_text="m",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_submit=calcular_imc
    )
    result = ft.Text(size=20, weight="bold")

    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text("\nÍndice de Massa Corporal")]
            )
        ),
        peso, altura,
        ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
        result
    )


ft.app(main)
