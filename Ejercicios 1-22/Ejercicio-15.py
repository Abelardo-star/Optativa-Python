#Añadir al ejercicio anterior una opción para salir del programa y un bucle del que sólo saldrá el programa cuando el usuario seleccione dicha opción de salida.
while True:
    print("Seleccione una opción:")
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

    if opcion == "1":
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        suma = num1 + num2
        print("La suma de", num1, "y", num2, "es:", suma)
    elif opcion == "2":
        num1 = float(input("Introduce el primer número real: "))
        num2 = float(input("Introduce el segundo número real: "))
        suma = num1 + num2
        print("La suma de", num1, "y", num2, "es:", suma)
    elif opcion == "3":
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        producto = num1 * num2
        print("El producto de", num1, "y", num2, "es:", producto)
    elif opcion == "4":
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        division = num1 / num2
        print("El resultado de dividir", num1, "por", num2, "es:", division)
    elif opcion == "5":
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        division_entera = num1 // num2
        print("El resultado de dividir", num1, "por", num2, "es:", division_entera)
    elif opcion == "6":
        num1 = int(input("Introduce el primer número entero: "))
        num2 = int(input("Introduce el segundo número entero: "))
        modulo = num1 % num2
        print("El resultado de", num1, "módulo", num2, "es:", modulo)   