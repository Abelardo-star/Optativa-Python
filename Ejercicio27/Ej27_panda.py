import pandas as pd

nombre_archivo = "Ej 27 Pandas 1.xlsx"
nombre_hoja = "Alumnos"
datos = {}

with pd.ExcelFile(nombre_archivo, engine="openpyxl") as excel:
    
    df = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=None)
    
    df = df.fillna("")
    
    print("--- 1. DataFrame Original (sin índice) ---")
    print(df)
    print("\n" + "="*60 + "\n")
    
    datos[nombre_hoja] = df.to_dict(orient="records")


print("--- 2. Estructura con orient='records' ---")
print(datos)
print("\n" + "="*60 + "\n")

print("--- 3. Recorrido de orient='records' (Lista de diccionarios) ---")
for alumno in datos[nombre_hoja]:
    for clave, valor in alumno.items():
        print(f"{clave}: {valor}")
    print("---")

print("\n" + "="*60 + "\n")

with pd.ExcelFile(nombre_archivo, engine="openpyxl") as excel:
    df_parte2 = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=None).fillna("")

datos_dict = df_parte2.to_dict(orient="dict")
print("--- Estructura orient='dict' ---")
print(datos_dict)

print("\n--- Recorrido orient='dict' ---")
for columna, filas in datos_dict.items():
    for indice, valor in filas.items():
        print(f"Columna: {columna}, Índice: {indice} -> {valor}")

print("\n" + "="*60 + "\n")

datos_index = df_parte2.to_dict(orient="index")
print("--- Estructura orient='index' ---")
print(datos_index)

print("\n--- Recorrido orient='index' ---")
for indice, alumno in datos_index.items():
    print(f"Índice: {indice}")
    for columna, valor in alumno.items():
        print(f"  {columna}: {valor}")
    print("---")

print("\n" + "="*60 + "\n")

datos_list = df_parte2.to_dict(orient="list")
print("--- Estructura orient='list' ---")
print(datos_list)

print("\n--- Recorrido orient='list' ---")
for columna, lista_valores in datos_list.items():
    print(f"Columna: {columna}")
    for valor in lista_valores:
        print(f"  - {valor}")
    print("---")

print("\n" + "="*60 + "\n")

with pd.ExcelFile(nombre_archivo, engine="openpyxl") as excel:
    df_indice = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=0)
    df_indice = df_indice.fillna("")

print("--- DataFrame con index_col=0 (id_persona como índice) ---")
print(df_indice)
print("\n" + "="*60 + "\n")

datos_dict_id = df_indice.to_dict(orient="dict")
print("--- Estructura orient='dict' con índice ---")
print(datos_dict_id)

print("\n--- Recorrido orient='dict' con índice ---")
for columna, alumnos in datos_dict_id.items():
    for id_persona, valor in alumnos.items():
        print(f"Columna: {columna}, ID Persona: {id_persona} -> {valor}")

print("\n" + "="*60 + "\n")

datos_index_id = df_indice.to_dict(orient="index")
print("--- Estructura orient='index' con índice ---")
print(datos_index_id)

print("\n--- Recorrido orient='index' con índice ---")
for id_persona, datos_alumno in datos_index_id.items():
    print(f"ID Persona: {id_persona}")
    for columna, valor in datos_alumno.items():
        print(f"  {columna}: {valor}")
    print("---")