# Identificar un número si es par o impar con la condición "match"

print("\nIdentificación de numeros pares o impares\n")

numero = int(input("Ingresar un número entero por favor: "))

match numero:
    case 0: 
        print("El número es un cero.")
    case numero if numero % 2 == 0:
        print("El número es par.")
    case numero if numero % 2 != 0:
        print("El número es impar.")
    case _:
        print("El número no es válido.")