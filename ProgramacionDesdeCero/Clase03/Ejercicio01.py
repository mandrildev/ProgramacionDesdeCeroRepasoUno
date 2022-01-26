# 1. Hacer un programa que pida el usuario y la contraseña a un usuario.
# Si ambos son correctos (usuario "mandril" / contraeña "dev"),
# mostrar un mensaje de bienvenida.
# Si alguno de los dos es incorrecto, mostrar un mensaje de error.

usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

usuario_correcto = "mandril"
password_correcto = "dev"

if usuario == usuario_correcto and password == password_correcto:
    print("Bienvenido al sistema")
else:
    print("Datos incorrectos")