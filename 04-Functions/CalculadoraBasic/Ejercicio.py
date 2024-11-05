# Escribe una función para cada operación aritmética (suma, resta, multiplicación, división). Luego, solicita al usuario dos números y pide qué operación quiere realizar.

print("\nCalculadora básica\n")

#Funciones de calculadora basica
def suma (num1, num2):
    return num1 + num2

def resta (num1, num2):
    return num1 - num2

def multiplicacion (num1, num2):
    return num1 * num2

def division (num1, num2):
    return num1 / num2

#Solicitamos los dos números
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

#Menu de opciones
print("\n--- Menú de opciones ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

opcion = int(input("\nIngrese la opción deseada: "))

if (opcion == 1):
    print(f"La suma de los dos números es: {suma(numero_1, numero_2)}")

elif (opcion == 2):
        print(f"La resta de los dos números es: {resta(numero_1, numero_2)}")

elif (opcion == 3):
        print(f"La multiplicación de los dos números es: {multiplicacion(numero_1, numero_2)}")

elif (opcion == 4):
        print(f"La división de los dos números es: {division(numero_1, numero_2)}")

elif (opcion == 5):
    print("Hasta luego")

else:
     print("Opción no válida")