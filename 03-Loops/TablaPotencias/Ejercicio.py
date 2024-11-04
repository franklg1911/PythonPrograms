# Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de potencias del 1 al 10 del valor introducido.

print("\nTabla de potencias\n")

numero = int(input("Ingresar un número: "))

for i in range(1,11):
    resultado = numero ** i

    print(f"{numero} ^ {i} = {resultado}")