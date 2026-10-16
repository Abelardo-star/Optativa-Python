# Añade al ejercicio anterior un control de errores o control de excepciones con try/except, incluye reglas de negocio con raise, por ejemplo una distancia en metros no puede ser negativa y las excepciones de ValueError y ZeroDivisionError.
while True:
    print("\nSeleccione una opción:")
    print("1. Sumar dos números enteros")
    print("2. Sumar dos números reales")
    print("3. Multiplicar dos números enteros")
    print("4. Dividir dos números enteros (división real)")
    print("5. Dividir dos números enteros (división entera)")
    print("6. Módulo de dos números enteros")
    print("7. Convertir metros a centímetros")
    print("8. Calcular el área de un círculo")
    print("9. Calcular el importe total a pagar en un restaurante")
    print("10. Calcular el IMC (Índice de Masa Corporal)")
    print("11. Salir del programa")

    opcion = input("Introduce el número de la opción que deseas ejecutar: ")

    if opcion == "11":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    try:
        if opcion == "1":
            num1 = int(input("Introduce el primer número entero: "))
            num2 = int(input("Introduce el segundo número entero: "))
            print("La suma es:", num1 + num2)
        elif opcion == "2":
            num1 = float(input("Introduce el primer número real: "))
            num2 = float(input("Introduce el segundo número real: "))
            print("La suma es:", num1 + num2)
        elif opcion == "3":
            num1 = int(input("Introduce el primer número entero: "))
            num2 = int(input("Introduce el segundo número entero: "))
            print("El producto es:", num1 * num2)
        elif opcion == "4":
            num1 = int(input("Introduce el primer número entero: "))
            num2 = int(input("Introduce el segundo número entero: "))
            print("El resultado de la división es:", num1 / num2)
        elif opcion == "5":
            num1 = int(input("Introduce el primer número entero: "))
            num2 = int(input("Introduce el segundo número entero: "))
            print("El resultado de la división entera es:", num1 // num2)
        elif opcion == "6":
            num1 = int(input("Introduce el primer número entero: "))
            num2 = int(input("Introduce el segundo número entero: "))
            print("El módulo es:", num1 % num2)
        elif opcion == "7":
            metros = float(input("Introduce la cantidad en metros: "))
            if metros < 0:
                raise ValueError("La distancia en metros no puede ser negativa.")
            print("La cantidad en centímetros es:", metros * 100)
        elif opcion == "8":
            import math

            radio = float(input("Introduce el radio del círculo: "))
            if radio < 0:
                raise ValueError("El radio no puede ser negativo.")
            print("El área del círculo es:", math.pi * radio ** 2)
        elif opcion == "9":
            coste_comida = float(input("Introduce el coste de la comida: "))
            porcentaje_propina = float(input("Introduce el porcentaje de propina: "))
            if coste_comida < 0 or porcentaje_propina < 0:
                raise ValueError("El coste y la propina no pueden ser negativos.")
            propina = coste_comida * (porcentaje_propina / 100)
            print("El importe total a pagar es:", coste_comida + propina)
        elif opcion == "10":
            peso = float(input("Introduce tu peso en kilogramos: "))
            altura = float(input("Introduce tu altura en metros: "))
            if peso < 0 or altura < 0:
                raise ValueError("El peso y la altura no pueden ser negativos.")
            imc = peso / (altura ** 2)
            print("Tu IMC es:", imc)
        else:
            print("Opción no válida. Selecciona un número del 1 al 11.")
    except ValueError as error:
        print("Error de valor:", error)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
