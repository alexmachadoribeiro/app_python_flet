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
                result.value = f"O valor do IMC: {imc:,.2f}."

                if imc < 18.5:
                    diagnostico.value = "Você está abaixo do peso."
                    diagnostico.color = ft.Colors.BLACK
                elif imc < 25:
                    diagnostico.value = "Você está no seu peso ideal."
                    diagnostico.color = ft.Colors.BLUE
                elif imc < 30:
                    diagnostico.value = "Você está acima do seu peso."
                    diagnostico.color = ft.Colors.GREEN
                elif imc < 35:
                    diagnostico.value = "Você está obeso."
                    diagnostico.color = ft.Colors.YELLOW
                elif imc < 40:
                    diagnostico.value = "Você está com obesidade nível II."
                    diagnostico.color = ft.Colors.ORANGE
                else:
                    diagnostico.value = "Você está com obesidade mórbida."
                    diagnostico.color = ft.Colors.RED

                diagnostico.update()
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
    diagnostico = ft.Text(size=15, weight="bold")

    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text(
                    "\nÍndice de Massa Corporal", 
                    size=30, 
                    weight="bold"
                )],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        peso, altura,
        ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
        result, diagnostico
    )


ft.app(main)
