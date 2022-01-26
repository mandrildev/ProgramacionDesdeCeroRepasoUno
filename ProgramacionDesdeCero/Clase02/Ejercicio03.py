# 3. Hacer un programa que pida al usuario cuatro números
# y muestre el resultado de la suma y la resta de los dos primeros,
# de la multiplicación y división de los dos últimos,
# y de la suma de todos.

numero_uno = float(input("Ingrese el primer número: "))
numero_dos = float(input("Ingrese el segundo número: "))
numero_tres = float(input("Ingrese el tercer número: "))
numero_cuatro = float(input("Ingrese el cuarto número: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
multiplicacion = numero_tres * numero_cuatro
division = numero_tres / numero_cuatro

print(suma)
print(resta)
print(multiplicacion)
print(division)