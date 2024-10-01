import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"tu IMC es de: {imc:.2f}"
        page.update()
        
    #función para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
        
    #Validación del IMC
    
        if imc<18.5:
            dialog=ft.AlertDialog(
                title="Bajo peso",
                content="Tu IMC indica que tienes bajo peso",
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
        elif imc>=18.5 and imc<24.9:
            dialog=ft.AlertDialog(
                
                title="Peso normal",
                content="Tu IMC indica que tienes un peso normal",
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
        elif imc>=25 and imc<30:
            dialog=ft.AlertDialog(
                
                title="Sobre peso",
                content="Tu IMC indica que tienes un peso normal",
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            ) 
        else:
            dialog=ft.AlertDialog(
                
                title="Obecidad",
                content="Tu IMC indica que tienes obecidad,acude a tu medico",
                actions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ]
            )
            
            page.dialog=dialog
            page.dialog.open=True
            page.update()
        
    except ValueError:
        page.dialog.open = False
        page.update()
        

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor="yellow"
    
    txtPeso=ft.TextField(label="Ingresa tu peso")
    txtAltura=ft.TextField(label="Ingresa tu altura")
    lblIMC=ft.Text("Tu IMC es de: ")
    
    img=ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def on_calcular(e):
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
        
    def limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value="Tu IMC es de: "
        page.update()
    
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
    page.add(
        ft.Column(
            controls=[
                txtPeso,txtAltura,lblIMC
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,btnLimpiar
            ],alignment="CENTER"
        )
        )
    
    


ft.app(target=main,view=ft.AppView.WEB_BROWSER)
