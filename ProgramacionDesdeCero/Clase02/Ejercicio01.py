# 1. Hacer un programa que pida al usuario su nombre,
# apellido, edad y años de experiencia laboral.
# Debe mostrar la edad en la que la persona comenzó a trabajar.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
anios_experiencia_laboral = input("Ingrese sus años de experiencia laboral: ")

edad_comienzo_laboral = int(edad) - int(anios_experiencia_laboral)

print(edad_comienzo_laboral)