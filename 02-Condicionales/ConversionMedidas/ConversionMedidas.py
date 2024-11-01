"""
 
   __  __ ___ ___ ___ ___   _   ___ 
  |  \/  | __|   \_ _|   \ /_\ / __|
  | |\/| | _|| |) | || |) / _ \\__ \
  |_|  |_|___|___/___|___/_/ \_\___/
                                    
 
"""

#Converitmos de metros a km y a cm

print("\nConversion de medidas\n")

medida = float(input("Ingrese la medida en metros: "))
opcion = input("\n ¿A qué medida lo quieres convertir?"
               "\n A. Convertir a kilometros"
               "\n B. Convertir a centimetros"
               "\n C. Convertir a pulgadas\n")

if (opcion == "A"):
    total = medida/1000
    print("La cantidad en kilometros es: ", total)

elif (opcion == "B"):
    total = medida*100
    print("La cantidad en centimetros es: ", total)

elif (opcion == "C"):
    total = (medida*39.37) / 1
    print("La cantidad en pulgadas es: ", total)

else :
    print("Elegiste una letra que no existe")

