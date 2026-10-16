#Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario.El programa deberá pedir al usuario su peso (en kilogramos) y su altura (en metros), y luego calcular su IMC usando la fórmula: IMC = Peso / Altura^2
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print("Tu IMC es:", imc)