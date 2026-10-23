#  PARTE 1: Los 6 tipos de for de los apuntes

def practica_for():
    print("\n--- 1. Lista ---")
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(fruta.upper())
 
    print("\n--- 2. Tupla ---")
    coordenadas = (10, 20, 30)
    for punto in coordenadas:
        print(f"Punto: {punto}")
 
    print("\n--- 3. Diccionario con .items() (clave y valor) ---")
    precios = {"pan": 1.2, "leche": 0.9, "café": 2.5}
    for producto, precio in precios.items():
        print(f"{producto}: {precio}€")
 
    print("\n--- 4. Diccionario sin .items() (solo claves) ---")
    for producto in precios:
        print(f"{producto} -> {precios[producto]}€")
 
    print("\n--- 5. Diccionario con .values() (solo valores) ---")
    # OJO: .values lleva paréntesis -> .values()
    for precio in precios.values():
        print(precio)
    print("Alternativa:")
    for precio in precios.values():
        print(f"Precio: {precio}€")
 
    print("\n--- 6. Cadena de caracteres ---")
    texto = "Python"
    for letra in texto:
        print(letra * 2)

#  PARTE 2: Lista de listas

alumnos = [
    ["Ana", 8, 7, 9],
    ["Luis", 5, 6, 4],
    ["Marta", 10, 9, 9],
]
 
 
def menu_lista_de_listas():
    while True:
        print("\n===== LISTA DE LISTAS (alumnos) =====")
        print("1. Imprimir la lista completa")
        print("2. Recorrer con for (nombre y notas)")
        print("3. Recorrer con for anidado (nota a nota)")
        print("4. Acceder por índice (fila y columna)")
        print("5. Añadir un alumno nuevo")
        print("6. Añadir una nota a un alumno")
        print("7. Media de cada alumno")
        print("8. Eliminar un alumno")
        print("0. Volver")
        opcion = input("Elige una opción: ")
 
        if opcion == "1":
            print(alumnos)
 
        elif opcion == "2":
            for alumno in alumnos:
                nombre = alumno[0]
                notas = alumno[1:]
                print(f"{nombre}: {notas}")
 
        elif opcion == "3":
            for alumno in alumnos:
                print(f"Notas de {alumno[0]}:")
                for nota in alumno[1:]:
                    print(f"   - {nota}")
 
        elif opcion == "4":
            print("Primer alumno:", alumnos[0])
            print("Nombre del segundo alumno:", alumnos[1][0])
            print("Segunda nota de Marta:", alumnos[2][2])
 
        elif opcion == "5":
            nombre = input("Nombre: ")
            n1 = int(input("Nota 1: "))
            n2 = int(input("Nota 2: "))
            n3 = int(input("Nota 3: "))
            alumnos.append([nombre, n1, n2, n3])
            print("Alumno añadido.")
 
        elif opcion == "6":
            nombre = input("¿A qué alumno? ")
            nota = int(input("Nota nueva: "))
            encontrado = False
            for alumno in alumnos:
                if alumno[0] == nombre:
                    alumno.append(nota)
                    encontrado = True
                    print("Nota añadida.")
            if not encontrado:
                print("Ese alumno no existe.")
 
        elif opcion == "7":
            for alumno in alumnos:
                notas = alumno[1:]
                media = sum(notas) / len(notas)
                print(f"{alumno[0]}: media {media:.2f}")
 
        elif opcion == "8":
            nombre = input("¿Qué alumno quieres eliminar? ")
            for alumno in alumnos:
                if alumno[0] == nombre:
                    alumnos.remove(alumno)
                    print("Alumno eliminado.")
                    break
            else:
                print("Ese alumno no existe.")
 
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
 
 

#  PARTE 3: Diccionario de listas


asignaturas = {
    "Programación": [8, 7, 9],
    "Bases de datos": [6, 5, 7],
    "Redes": [9, 10],
}
 
 
def menu_diccionario_de_listas():
    while True:
        print("\n===== DICCIONARIO DE LISTAS (asignaturas) =====")
        print("1. Imprimir el diccionario completo")
        print("2. Recorrer con .items() (asignatura y notas)")
        print("3. Recorrer solo las claves")
        print("4. Recorrer solo los valores (.values())")
        print("5. Recorrer notas una a una (for anidado)")
        print("6. Añadir una asignatura nueva")
        print("7. Añadir una nota a una asignatura")
        print("8. Media de cada asignatura")
        print("9. Eliminar una asignatura")
        print("0. Volver")
        opcion = input("Elige una opción: ")
 
        if opcion == "1":
            print(asignaturas)
 
        elif opcion == "2":
            for asignatura, notas in asignaturas.items():
                print(f"{asignatura}: {notas}")
 
        elif opcion == "3":
            for asignatura in asignaturas:
                print(f"{asignatura} -> {asignaturas[asignatura]}")
 
        elif opcion == "4":
            for notas in asignaturas.values():
                print(notas)
 
        elif opcion == "5":
            for asignatura, notas in asignaturas.items():
                print(f"{asignatura}:")
                for nota in notas:
                    print(f"   - {nota}")
 
        elif opcion == "6":
            nombre = input("Nombre de la asignatura: ")
            if nombre in asignaturas:
                print("Esa asignatura ya existe.")
            else:
                asignaturas[nombre] = []
                print("Asignatura añadida (sin notas todavía).")
 
        elif opcion == "7":
            nombre = input("¿A qué asignatura? ")
            if nombre in asignaturas:
                nota = int(input("Nota nueva: "))
                asignaturas[nombre].append(nota)
                print("Nota añadida.")
            else:
                print("Esa asignatura no existe.")
 
        elif opcion == "8":
            for asignatura, notas in asignaturas.items():
                if len(notas) > 0:
                    media = sum(notas) / len(notas)
                    print(f"{asignatura}: media {media:.2f}")
                else:
                    print(f"{asignatura}: sin notas")
 
        elif opcion == "9":
            nombre = input("¿Qué asignatura quieres eliminar? ")
            if nombre in asignaturas:
                del asignaturas[nombre]
                print("Asignatura eliminada.")
            else:
                print("Esa asignatura no existe.")
 
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
 
 
#  MENÚ PRINCIPAL

def main():
    while True:
        print("\n########## MENÚ PRINCIPAL ##########")
        print("1. Prácticas de for (los 6 ejemplos)")
        print("2. Lista de listas")
        print("3. Diccionario de listas")
        print("0. Salir")
        opcion = input("Elige una opción: ")
 
        if opcion == "1":
            practica_for()
        elif opcion == "2":
            menu_lista_de_listas()
        elif opcion == "3":
            menu_diccionario_de_listas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
 
 
main()