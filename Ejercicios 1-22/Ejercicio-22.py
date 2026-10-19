#EJERCICIO 22:
#Enunciado:
#Práctica: Sistema de Gestión y Resumen de Ventas de Vehículos
#Objetivo:
#Se trata de desarrollorar una aplicación para gestionar el registro de ventas de un concesionario de coches desde el año 2024 hasta la actualidad. 
#Tendremos unos datos iniciales de ventas para tener volumen y permitiremos que el usuario introduzca nuevos registros de ventas (con los datos: Marca, Modelo, AñoVenta, AñoFabricacion y precio) y
#pueda visualizar 3 tipos de resúmenes de ventas.
#Menú por pantalla:
#==========================================
#SISTEMA DE GESTIÓN DE VENTAS
#==========================================
#1.- Dar de alta una nueva venta
#2.- Resumen de ventas (Marca_Modelo_Año)
#3.- Resumen de ventas (Marca_Modelo - Todos los años)
#4.- Resumen de ventas (Marca - Todos los modelos y años)
#5.- Salir del programa
#Datos de partida:
#MARCAS_MODELOS = { "SEAT": ["Ibiza", "Leon", "Ateca", "Arona"], "Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"] }
#ventas = [
#["SEAT", "Ibiza", 2024, 2023, 18000], ["SEAT", "Ibiza", 2024, 2024, 18500], ["SEAT", "Ibiza", 2024, 2024, 19000],
#["SEAT", "Ibiza", 2025, 2024, 19500], ["SEAT", "Ibiza", 2025, 2025, 20000], ["SEAT", "Ibiza", 2025, 2025, 20200],
#["SEAT", "Ibiza", 2026, 2025, 20500], ["SEAT", "Ibiza", 2026, 2026, 21000], ["SEAT", "Ibiza", 2026, 2026, 21500],
#["SEAT", "Leon", 2024, 2024, 24000], ["SEAT", "Leon", 2024, 2024, 24500], ["SEAT", "Leon", 2024, 2023, 23800],
#["SEAT", "Leon", 2025, 2025, 25500], ["SEAT", "Leon", 2025, 2025, 26000], ["SEAT", "Leon", 2025, 2024, 25200],
#["SEAT", "Leon", 2026, 2026, 27000], ["SEAT", "Leon", 2026, 2026, 27500], ["SEAT", "Leon", 2026, 2025, 26800],
#["SEAT", "Ateca", 2024, 2024, 28000], ["SEAT", "Ateca", 2025, 2025, 29500], ["SEAT", "Ateca", 2026, 2026, 31000],
#["SEAT", "Arona", 2024, 2024, 21000], ["SEAT", "Arona", 2025, 2025, 22000], ["SEAT", "Arona", 2026, 2026, 23000],
#["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500], ["Toyota", "Corolla", 2024, 2023, 25800],
#["Toyota", "Corolla", 2025, 2025, 27500], ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
#["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500], ["Toyota", "Corolla", 2026, 2025, 28800],
#["Toyota", "Yaris", 2024, 2024, 20000], ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
#["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500], ["Toyota", "RAV4", 2026, 2026, 41000],
#["Toyota", "C-HR", 2024, 2024, 31000], ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000]
#]
#Detalle de las Opciones:
#1) Dar de alta una nueva venta:
#a) Selección de Marca: El programa imprimirá por consola las marcas disponibles en el diccionario MARCAS_MODELOS y pedirá al usuario que escriba el nombre de la marca.
#b) Selección de Modelo: Una vez elegida una marca válida, el programa imprimirá por consola la lista de modelos disponibles para esa marca específica y solicitará que el usuario escriba el nombre del modelo.
#c) Normalización y Validación de Nombres:
#1) Para evitar errores en las búsquedas y unificar el formato, el programa debe transformar la entrada del usuario asegurándose de que la primera letra sea mayúscula y el resto minúsculas.
#2) El programa debe verificar que la marca introducida exista en MARCAS_MODELOS y que el modelo pertenezca a la lista de dicha marca. Si no es así, debe mostrar un mensaje de error y volver a solicitar el dato.
#d) Validación de Datos Numéricos (try/except):
#1) Año de Venta: Debe ser un entero comprendido entre 2024 y 2026.
#2) Año de Fabricación: Debe ser un entero comprendido entre 1990 y el Año de Venta introducido.
#3) Precio: Debe ser un número entero comprendido entre 1.000 y 100.000 €.
#e) Una vez validados todos los datos, añadirá el nuevo registro a la lista ventas.
#2) Resumen de ventas por Marca, Modelo y Año de Venta:
#Recorrerá la lista ventas y construirá un diccionario donde la clave sea "Marca_Modelo_AñoVenta" (ejemplo: "Seat_Ibiza_2024").
#El valor asociado a la clave será una lista con dos elementos:
#[Total_Unidades_Vendidas, Total_Euros_Acumulados].
#Impresión: Imprimir el diccionario creado
#3) Resumen de ventas por Marca y Modelo (Todos los años):
#Igual que el anterior pero agrupa sólo por Marca y Modelo.
#4) Resumen total por Marca:
#Igual que el anterior pero agrupa sólo por Marca.
#5) Salir del programa:
#Finalizará la ejecución del programa


MARCAS_MODELOS = {
    "SEAT": ["Ibiza", "Leon", "Ateca", "Arona"],
    "Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"],
}

ventas = [
    ["SEAT", "Ibiza", 2024, 2023, 18000], ["SEAT", "Ibiza", 2024, 2024, 18500],
    ["SEAT", "Ibiza", 2024, 2024, 19000], ["SEAT", "Ibiza", 2025, 2024, 19500],
    ["SEAT", "Ibiza", 2025, 2025, 20000], ["SEAT", "Ibiza", 2025, 2025, 20200],
    ["SEAT", "Ibiza", 2026, 2025, 20500], ["SEAT", "Ibiza", 2026, 2026, 21000],
    ["SEAT", "Ibiza", 2026, 2026, 21500], ["SEAT", "Leon", 2024, 2024, 24000],
    ["SEAT", "Leon", 2024, 2024, 24500], ["SEAT", "Leon", 2024, 2023, 23800],
    ["SEAT", "Leon", 2025, 2025, 25500], ["SEAT", "Leon", 2025, 2025, 26000],
    ["SEAT", "Leon", 2025, 2024, 25200], ["SEAT", "Leon", 2026, 2026, 27000],
    ["SEAT", "Leon", 2026, 2026, 27500], ["SEAT", "Leon", 2026, 2025, 26800],
    ["SEAT", "Ateca", 2024, 2024, 28000], ["SEAT", "Ateca", 2025, 2025, 29500],
    ["SEAT", "Ateca", 2026, 2026, 31000], ["SEAT", "Arona", 2024, 2024, 21000],
    ["SEAT", "Arona", 2025, 2025, 22000], ["SEAT", "Arona", 2026, 2026, 23000],
    ["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500],
    ["Toyota", "Corolla", 2024, 2023, 25800], ["Toyota", "Corolla", 2025, 2025, 27500],
    ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
    ["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500],
    ["Toyota", "Corolla", 2026, 2025, 28800], ["Toyota", "Yaris", 2024, 2024, 20000],
    ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
    ["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500],
    ["Toyota", "RAV4", 2026, 2026, 41000], ["Toyota", "C-HR", 2024, 2024, 31000],
    ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000],
]


def leer_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Error: el valor debe estar entre {minimo} y {maximo}.")


def leer_texto(mensaje):
    entrada = input(mensaje)
    while entrada[:1] == " ":
        entrada = entrada[1:]
    while entrada[-1:] == " ":
        entrada = entrada[:-1]
    return entrada


def dar_de_alta_venta():
    print("Marcas disponibles:", ", ".join(MARCAS_MODELOS))
    while True:
        entrada = leer_texto("Introduce la marca: ").lower()
        marca = next(
            (nombre for nombre in MARCAS_MODELOS if nombre.lower() == entrada),
            None,
        )
        if marca:
            break
        print("Error: la marca no existe.")

    modelos = MARCAS_MODELOS[marca]
    print(f"Modelos disponibles para {marca}:", ", ".join(modelos))
    while True:
        entrada = leer_texto("Introduce el modelo: ").lower()
        modelo = next(
            (nombre for nombre in modelos if nombre.lower() == entrada),
            None,
        )
        if modelo:
            break
        print("Error: el modelo no pertenece a esa marca.")

    anio_venta = leer_entero("Año de venta (2024-2026): ", 2024, 2026)
    anio_fabricacion = leer_entero(
        f"Año de fabricación (1990-{anio_venta}): ", 1990, anio_venta
    )
    precio = leer_entero("Precio en euros (1000-100000): ", 1000, 100000)
    ventas.append([marca, modelo, anio_venta, anio_fabricacion, precio])
    print("Venta registrada correctamente.")


def generar_resumen(indices):
    resumen = {}
    for marca, modelo, anio_venta, _, precio in ventas:
        campos = [marca, modelo, anio_venta]
        clave = "_".join(f"{campos[indice]}" for indice in indices)
        if clave not in resumen:
            resumen[clave] = [0, 0]
        resumen[clave][0] += 1
        resumen[clave][1] += precio
    return resumen


def mostrar_resumen(indices, titulo):
    resumen = generar_resumen(indices)
    encabezados = ["Marca", "Modelo", "Año de venta"][:len(indices)]
    encabezados += ["Unidades", "Importe total"]
    filas = [
        clave.split("_") + [
            f"{datos[0]}",
            f"{datos[1]:,}".replace(",", ".") + " €",
        ]
        for clave, datos in resumen.items()
    ]
    anchos = [
        max(len(encabezados[columna]), *(len(fila[columna]) for fila in filas))
        for columna in range(len(encabezados))
    ]

    def formato_fila(valores):
        return " | ".join(
            f"{valor:<{anchos[columna]}}"
            if columna < len(indices)
            else f"{valor:>{anchos[columna]}}"
            for columna, valor in enumerate(valores)
        )

    separador = "-+-".join("-" * ancho for ancho in anchos)
    print(f"\n{titulo}")
    print(formato_fila(encabezados))
    print(separador)
    for fila in filas:
        print(formato_fila(fila))

    total_unidades = sum(datos[0] for datos in resumen.values())
    total_euros = sum(datos[1] for datos in resumen.values())
    print(separador)
    total = ["TOTAL"] + [""] * (len(indices) - 1)
    total += [f"{total_unidades}", f"{total_euros:,}".replace(",", ".") + " €"]
    print(formato_fila(total))


def mostrar_menu():
    print("\n==========================================")
    print("SISTEMA DE GESTIÓN DE VENTAS")
    print("==========================================")
    print("1.- Dar de alta una nueva venta")
    print("2.- Resumen de ventas (Marca_Modelo_Año)")
    print("3.- Resumen de ventas (Marca_Modelo - Todos los años)")
    print("4.- Resumen de ventas (Marca - Todos los modelos y años)")
    print("5.- Salir del programa")


while True:
    mostrar_menu()
    opcion = leer_texto("Selecciona una opción: ")
    if opcion == "1":
        dar_de_alta_venta()
    elif opcion == "2":
        mostrar_resumen([0, 1, 2], "RESUMEN POR MARCA, MODELO Y AÑO")
    elif opcion == "3":
        mostrar_resumen([0, 1], "RESUMEN POR MARCA Y MODELO")
    elif opcion == "4":
        mostrar_resumen([0], "RESUMEN POR MARCA")
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Selecciona una opción del 1 al 5.")