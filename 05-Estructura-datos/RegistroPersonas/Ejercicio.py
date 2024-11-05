# Escribe un programa en Python que permita al usuario ingresar su nombre, edad, dirección y número de teléfono, y luego muestre estos datos en pantalla.

# Instrucciones:

#    1 Crea un diccionario llamado datos_personales con las siguientes claves: "nombre", "edad", "direccion" y "telefono". Inicializa todos los valores a None.

#    2 Solicita al usuario que ingrese su nombre, edad, dirección y número de teléfono y almacena cada valor en el diccionario datos_personales.

#    3 Muestra en pantalla los datos ingresados por el usuario utilizando las claves del diccionario.


print("\nRegistro datos personales\n")

#Crear diccionario vacio para almacenar los datos
datos_personales = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "numero": None
}

#Solicitar datos al usuario
datos_personales["nombre"] = input("Ingresa tu nombre por favor: ")
datos_personales["edad"] = input("Ingresa tu edad por favor: ")
datos_personales["direccion"] = input("Ingresa tu direccion por favor: ")
datos_personales["numero"] = input("Ingresa tu numero por favor: ")

#Mostrar los datos
print("\nTus datos personales: ")
print("Tu nombre es: " , datos_personales["nombre"] + ".")
print("Tu edad es: " , datos_personales["edad"] + ".")
print("Tu dirección es: " , datos_personales["direccion"] + ".")
print("Tu número es: " , datos_personales["numero"] + ".")




