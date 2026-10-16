#Escribe un programa que calcule el área de un círculo. El programa deberá pedir al usuario que introduzca el radio del círculo y, utilizando la fórmula Área = Pi *radio^2

import math
radio = float(input("Introduce el radio del círculo: "))
area = math.pi * radio ** 2
print("El área del círculo con radio", radio, "es:", area)