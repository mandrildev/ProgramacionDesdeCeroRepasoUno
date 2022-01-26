# 3. Hacer un programa que le pida al usuario una frase y luego un número límite para su frase.
# Devolver el texto ingresado por el usuario cortado al llegar al límite de caracteres que el mismo ingresó.

# 4. Hacer un programa que le pida un texto al usuario y:
# a. Reemplazar la palabra "yo" por la palabra "eu" (tanto en mayúsculas como en minúsculas)
# b. Reemplazar la palabra "soy" por la palabra "sou" (tanto en mayúsculas como en minúsculas)
# c. Borrar los espacios al principio y al final del texto (strip)
# d. Devuelva la frase final cortada usando el límite provisto
# e. Devuelva la cantidad de caracteres que tenga la frase final con el siguiente texto
#    "La frase tiene (x) caracteres".

frase = input("Ingrese una frase: ")
limite = int(input("Ingrese un número límite de caracteres para la frase: "))

palabra_vieja_1 = "yo"
palabra_vieja_2 = "soy"

palabra_nueva_1 = "eu"
palabra_nueva_2 = "sou"

frase = frase.strip()
frase = frase.replace(palabra_vieja_1, palabra_nueva_1)
frase = frase.replace(palabra_vieja_2, palabra_nueva_2)
frase = frase[0:limite]

print(frase)
print("La frase tiene " + str(limite) + " caracteres.")