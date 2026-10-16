#Escribe un programa en Python que inicialice una lista llamadafrutas con los elementos"manzana" ,"platano" y"naranja" .
#El programa debe presentar de forma continua un menú dentro de un buclewhile con las siguientes opciones numéricas:
#1. Ver lista completa: Muestra la lista completa por pantalla.
#2. Ver un elemento por índice: Pide una posición al usuario y muestra el elemento guardado en dicho índice.
#3. Añadir elemento: Pide el nombre de una nueva fruta y la añade al final de la lista.
#4. Modificar elemento: Pide la posición que se desea cambiar y el nuevo nombre para actualizar ese valor en la lista.
#5. Borrar elemento: Pide el índice del elemento que se quiere eliminar y lo quita de la lista.
#6. Salir: Muestra un mensaje de despedida y finaliza la ejecución del programa.

frutas = ["manzana", "platano", "naranja"]

while True:
    print("\n--- Menú de frutas ---")
    print("1. Ver lista completa")
    print("2. Ver un elemento por índice")
    print("3. Añadir elemento")
    print("4. Modificar elemento")
    print("5. Borrar elemento")
    print("6. Salir")

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Introduce un número válido.")
        continue

    if opcion == 1:
        print(frutas)
    elif opcion == 2:
        try:
            indice = int(input("Introduce el índice: "))
            print(frutas[indice])
        except ValueError:
            print("El índice debe ser un número.")
        except IndexError:
            print("No hay ninguna fruta en ese índice.")
    elif opcion == 3:
        fruta = input("Introduce el nombre de la fruta: ")
        frutas.append(fruta)
        print("Fruta añadida.")
    elif opcion == 4:
        try:
            indice = int(input("Introduce el índice que deseas modificar: "))
            fruta = input("Introduce el nuevo nombre: ")
            frutas[indice] = fruta
            print("Fruta modificada.")
        except ValueError:
            print("El índice debe ser un número.")
        except IndexError:
            print("No hay ninguna fruta en ese índice.")
    elif opcion == 5:
        try:
            indice = int(input("Introduce el índice que deseas borrar: "))
            del frutas[indice]
            print("Fruta borrada.")
        except ValueError:
            print("El índice debe ser un número.")
        except IndexError:
            print("No hay ninguna fruta en ese índice.")
    elif opcion == 6:
        print("¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Elige un número del 1 al 6.")
