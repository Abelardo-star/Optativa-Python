#Tienes una lista de datos de ventas donde cada registro es una tupla con el formato: 
#("producto", cantidad, precio_unitario). Los datos los metes directamente en el programa, pongamos 5 tuplas o lineas de la compra, ejemplo de tupla: manzanas, cantidad 3 kilos y precio 2,7 eur.
#El programa debe hacer lo siguiente:
#Convierta el nombre del producto a mayúsculas.
#Calcule el total gastado en cada producto (cantidad * precio) y redondee el resultado final
#a 2 decimales usando la función round().
#Muestre por pantalla el total de esa compra y el total de la suma de todas las cantidades.

ventas = [
    ("manzanas", 3, 2.7),
    ("plátanos", 2, 1.8),
    ("naranjas", 5, 1.25),
    ("peras", 4, 2.1),
    ("uvas", 1.5, 3.6),
]

total_compra = 0
total_cantidades = 0

print("Detalle de la compra:")
for producto, cantidad, precio_unitario in ventas:
    total_producto = round(cantidad * precio_unitario, 2)
    print(f"{producto.upper()}: {total_producto:.2f} €")
    total_compra += total_producto
    total_cantidades += cantidad

print(f"\nTotal de la compra: {round(total_compra, 2):.2f} €")
print(f"Total de cantidades: {total_cantidades:g} kg")
