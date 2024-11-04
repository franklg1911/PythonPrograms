# Realiza un contador de números y cuando ingrese un número negativo se termina de ejecutar el proceso

print("\nLista de números\n")

suma = 0

numero = int(input("Ingresa un número positivo. Para salir ingresa un número negativo: "))

while numero >= 0:
    suma += numero
    numero = int(input("Ingresa un número positivo. Para salir ingresa un número negativo: "))

print("La suma de los números ingresados es: ", suma)
    