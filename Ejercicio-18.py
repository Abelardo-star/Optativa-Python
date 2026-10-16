productos = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
info_tienda = ("Frutería La Huerta", "Calle Mayor 12", "912345678", 2010)
precios = {
    "manzanas": 1.50,
    "plátanos": 2.10,
    "naranjas": 1.20,
    "kiwis": 3.45,
    "fresas": 2.80,
}


def leer_texto(mensaje):
    return input(mensaje).strip().lower()


def mostrar_productos():
    if not productos:
        print("No hay productos almacenados.")
    else:
        print("Productos:")
        for indice, producto in enumerate(productos):
            print(f"{indice}: {producto}")
    print(f"Cantidad total: {len(productos)}")


def menu_lista():
    while True:
        print("\nGestión de Lista (Productos)")
        print("a) Consultar")
        print("b) Añadir")
        print("c) Modificar")
        print("d) Eliminar")
        print("e) Volver al menú principal")
        opcion = leer_texto("Elige una opción: ")

        if opcion == "a":
            mostrar_productos()
        elif opcion == "b":
            producto = leer_texto("Nombre del producto: ")
            if producto:
                productos.append(producto)
                print(f"Producto '{producto}' añadido.")
            else:
                print("El nombre del producto no puede estar vacío.")
        elif opcion == "c":
            mostrar_productos()
            try:
                indice = int(leer_texto("Índice del producto que quieres modificar: "))
                productos[indice]
                producto = leer_texto("Nuevo nombre: ")
                if producto:
                    productos[indice] = producto
                    print("Producto modificado.")
                else:
                    print("El nombre del producto no puede estar vacío.")
            except ValueError:
                print("El índice debe ser un número entero.")
            except IndexError:
                print("No existe ningún producto en ese índice.")
        elif opcion == "d":
            mostrar_productos()
            try:
                indice = int(leer_texto("Índice del producto que quieres eliminar: "))
                eliminado = productos.pop(indice)
                print(f"Producto '{eliminado}' eliminado.")
            except ValueError:
                print("El índice debe ser un número entero.")
            except IndexError:
                print("No existe ningún producto en ese índice.")
        elif opcion == "e":
            break
        else:
            print("Opción no válida.")


def menu_tienda():
    while True:
        print("\nConsulta de Tupla (Información de la Tienda)")
        print("a) Mostrar información de la tienda")
        print("b) Volver al menú principal")
        opcion = leer_texto("Elige una opción: ")

        if opcion == "a":
            print(f"Información completa: {info_tienda}")
            print(f"Longitud de la tupla: {len(info_tienda)}")
            for indice in range(len(info_tienda)):
                print(f"info_tienda[{indice}]: {info_tienda[indice]}")
        elif opcion == "b":
            break
        else:
            print("Opción no válida.")


def menu_precios():
    while True:
        print("\nGestión de Diccionario (Precios por Kilo)")
        print("a) Consultar catálogo completo")
        print("b) Ver solo nombres o solo precios")
        print("c) Añadir o actualizar un precio")
        print("d) Eliminar una fruta")
        print("e) Volver al menú principal")
        opcion = leer_texto("Elige una opción: ")

        if opcion == "a":
            if not precios:
                print("El catálogo está vacío.")
            else:
                print("Catálogo de precios por kilo:")
                for fruta, precio in precios.items():
                    print(f"{fruta}: {precio:.2f} €")
        elif opcion == "b":
            tipo = leer_texto("Escribe 'nombres' o 'precios': ")
            if tipo == "nombres":
                print("Frutas:", list(precios.keys()))
            elif tipo == "precios":
                print("Precios:", list(precios.values()))
            else:
                print("Opción no válida. Escribe 'nombres' o 'precios'.")
        elif opcion == "c":
            fruta = leer_texto("Nombre de la fruta: ")
            if not fruta:
                print("El nombre de la fruta no puede estar vacío.")
                continue
            try:
                precio = float(leer_texto("Precio por kilo: "))
                precios[fruta] = precio
                print(f"Precio de '{fruta}' guardado: {precio:.2f} € por kilo.")
            except ValueError:
                print("El precio debe ser un número válido.")
        elif opcion == "d":
            fruta = leer_texto("Nombre de la fruta que quieres eliminar: ")
            if fruta in precios:
                del precios[fruta]
                print(f"Fruta '{fruta}' eliminada del catálogo.")
            else:
                print(f"La fruta '{fruta}' no existe en el catálogo.")
        elif opcion == "e":
            break
        else:
            print("Opción no válida.")


def main():
    while True:
        print("\nSistema de Gestión para Frutería")
        print("1. Gestión de Lista (Productos)")
        print("2. Consulta de Tupla (Información de la Tienda)")
        print("3. Gestión de Diccionario (Precios por Kilo)")
        print("4. Salir")
        opcion = leer_texto("Elige una opción: ")

        if opcion == "1":
            menu_lista()
        elif opcion == "2":
            menu_tienda()
        elif opcion == "3":
            menu_precios()
        elif opcion == "4":
            print("¡Gracias por usar el sistema de gestión de la frutería! Hasta pronto.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
