# Crea una función que convierta grados Celsius a Fahrenheit, y otra que haga lo inverso. Permite que el usuario elija qué conversión quiere realizar.

print("\nConversión de grados\n")

def celsius__a__fahrenheit (grado):
    return (grado * 9/5) + 32

def fahrenheit__a__celsius (grado):
    return (grado -32) * 5/9

#Solicitamos el grado a convertir

temperatura = float(input("Ingrese el grado a convertir: "))

#Menú de opciones
print("\nMenu de opciones")
print("1. Convertir de celsius a fahrenheit")
print("2. Convertir de fahrenheit a celsius")
print("3. Salir")

opcion = int(input("Ingrese la opción: "))

if (opcion == 1):
    print(f"La temperatura en fahrenheit es: {celsius__a__fahrenheit(temperatura)}")

elif (opcion == 2):
    print(f"La temperatura en celsius es: {fahrenheit__a__celsius(temperatura)}")

elif (opcion == 3):
    print("Hasta luego")

else: 
    print("Opción no válida")



