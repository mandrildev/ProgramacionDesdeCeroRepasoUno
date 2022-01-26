# 3. Hacer un programa que pida al usuario su edad.
# Si tiene 18 años o más, mostrar un mensaje de bienvenida.
# Caso contrario, mostrar un mensaje de error.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Bienvenido a Mandril Dev")
else:
    print("Error, usted es muy pequeño para estar aquí")