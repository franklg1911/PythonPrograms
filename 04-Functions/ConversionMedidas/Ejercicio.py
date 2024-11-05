# Escribe una función que convierta una cantidad de kilómetros a metros, y otra que convierta metros a kilómetros.

print("\nConvertir KM a M\n")

def convertir_distancia ():
    print("Selecciona la conversión que deseas realizar: ")
    print("1. De kilómetros a metros")
    print("2. De metros a kilómetros")
    print("3. Salir")

    opcion = int(input("Ingresa una opción: "))

    if (opcion == 1):
        km = float(input("Ingresa la distancia en kilómetros: "))
        metros = km * 1000
        print(f"{km} kilómetros son {metros} metros.")

    elif (opcion == 2):
        metros = float(input("Ingresa la distancia en metros: "))
        km = metros / 1000
        print(f"{metros} metros son {km} kilómetros")
    
    elif (opcion == 3):
        print("Saliendo del sistema....")
    
    else:
        print("Opción no válida")

#Llamar a la función
convertir_distancia()