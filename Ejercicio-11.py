#Escribe un programa que calcule el importe total a pagar en un restaurante. El programa deberá pedir al usuario el coste de la comida y el porcentaje de propina que quiere dejar, y luego devolver el importe total.
coste_comida = float(input("Introduce el coste de la comida: "))
porcentaje_propina = float(input("Introduce el porcentaje de propina que quieres dejar (por ejemplo, 15 para un 15%): "))
propina = coste_comida * (porcentaje_propina / 100)
importe_total = coste_comida + propina
print("El importe total a pagar es:", importe_total)