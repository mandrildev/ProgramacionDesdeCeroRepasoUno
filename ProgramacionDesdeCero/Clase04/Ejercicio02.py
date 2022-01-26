# 2. Hacer el mismo programa que en el punto anterior pero con concatenación (+).
# No hace falta que sea multilínea.

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
visitante_nro = 345

texto = "Bienvenido " + nombre + " " + apellido + " al sistema de gestión de torta fritas. "
texto += "Usted es el visitante número " + str(visitante_nro) + "."

print(texto)