# Crea una lista de números y usa un bucle para imprimir solo los números que son mayores que 10.

print("\nSumar números de una lista mayores a 10\n")

def imprimir_mayores_10():
    lista_numeros = []

    print("Ingresa números (ingresa - 1 para salir):")

    while True:
        numero = int(input("Número: "))

        if (numero == -1):
            break
        lista_numeros.append(numero) # Agrega el numero a la lista

    print("Números mayores a 10:")

    for numero in lista_numeros:
        if numero > 10:
            print(numero)

# Llamamos a la función
imprimir_mayores_10()