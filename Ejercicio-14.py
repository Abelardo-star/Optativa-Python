#Meter en un match / case los ejercicios del 9 al 13, de forma que aparezca un menú con las 5 opciones para que el usuario decida que ejercicio o enunciado quiere ejecutar.
while True:
    print("Seleccione un ejercicio para ejecutar:")
    print("9. Convertir metros a centímetros")
    print("10. Calcular el área de un círculo")
    print("11. Calcular el importe total a pagar en un restaurante")
    print("12. Calcular el IMC (Índice de Masa Corporal)")
    print("13. Mensaje de bienvenida con nombre y apellido")
    print("0. Salir")

    opcion = input("Ingrese el número del ejercicio que desea ejecutar: ")

    match opcion:
        case "9":
            metros = float(input("Introduce la cantidad en metros: "))
            centimetros = metros * 100
            print("La cantidad en centímetros es:", centimetros)
        case "10":
            import math
            radio = float(input("Introduce el radio del círculo: "))
            area = math.pi * radio ** 2
            print("El área del círculo con radio", radio, "es:", area)
        case "11":
            coste_comida = float(input("Introduce el coste de la comida: "))
            porcentaje_propina = float(input("Introduce el porcentaje de propina que quieres dejar (por ejemplo, 15 para un 15%): "))
            propina = coste_comida * (porcentaje_propina / 100)
            importe_total = coste_comida + propina
            print("El importe total a pagar es:", importe_total)
        case "12":
            peso = float(input("Introduce tu peso en kilogramos: "))
            altura = float(input("Introduce tu altura en metros: "))
            imc = peso / (altura ** 2)
            print("Tu IMC es:", imc)
        case "13":
            nombre = input("Introduce tu nombre: ")
            apellido = input("Introduce tu apellido: ")
            print("¡Bienvenido/a,", nombre, apellido + "!")
        case "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione un número del 0 al 13.")
            