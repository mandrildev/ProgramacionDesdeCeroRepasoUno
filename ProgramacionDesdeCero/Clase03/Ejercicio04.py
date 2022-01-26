# 4. Hacer un programa que pida al usuario que ingrese su nombre.
# Si el nombre es "Don Ramon" o "Doña Florinda",
# mostrar un mensaje que diga "Es que no me tienen paciencia".

nombre = input("Ingrese su nombre: ")

don_ramon = "Don Ramon"
donia_florinda = "Doña Florinda"
paciencia = "Es que no me tienen paciencia"

if nombre == don_ramon or nombre == donia_florinda:
    print(paciencia)