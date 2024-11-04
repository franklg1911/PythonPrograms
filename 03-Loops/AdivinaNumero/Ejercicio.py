"""
 
     _   ___ _____   _____ _  _   _     _  _ _   _ __  __ ___ ___  ___  
    /_\ |   \_ _\ \ / /_ _| \| | /_\   | \| | | | |  \/  | __| _ \/ _ \ 
   / _ \| |) | | \ V / | || .` |/ _ \  | .` | |_| | |\/| | _||   / (_) |
  /_/ \_\___/___| \_/ |___|_|\_/_/ \_\ |_|\_|\___/|_|  |_|___|_|_\\___/ 
                                                                        
 
"""

#Programa para adivinar el número ingresado por el usuario del 1 al 10

#Número a adivinar
numero_correcto = 9

#Variable para controlar si el usuario adivino o no
adivinado = False


print("\nPrograma para adivinar el número")
print("\nAdivina el número del 1 al 10")


while not adivinado:
    #Solicitar al usuario que ingrese números
    intento = int(input("Por favor ingresa un número: "))

    #Comparar el número ingresado con el correcto

    if intento < numero_correcto:
        print("Muy bajo. Inténtalo de nuevo.")
    
    elif intento > numero_correcto:
        print("Muy alto. Inténtenlo de nuevo")

    else:
        print("Felicitaciones número adivinado")
        adivinado = True









