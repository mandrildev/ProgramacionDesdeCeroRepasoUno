# 1. Hacer un programa que pida el nombre y apellido de una persona y devuelva la siguiente frase:
# Bienvenido (nombre) (apellido) al sistema de gestión de torta fritas.
# Usted es el visitante número (visitante).
# a. Reemplazar (nombre) y (apellido) con los datos ingresados por el usuario.
# b. Reemplazar (visitante) con un número que esté guardado en una variable tipo int (no hardcodear!!!)
# b. Hacerlo utilizando el método format
# c. Tiene que ser multilínea

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
visitante_nro = 345

texto = """Bienvenido {} {} al sistema de gestión de torta fritas.
Usted es el visitante número {}.
"""

texto_formateado = texto.format(nombre, apellido, str(visitante_nro))
print(texto_formateado)