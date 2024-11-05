# Define una función calcular_factorial(numero) que tome un número y devuelva su factorial. Usa la función dentro de un programa que pida al usuario un número y muestre el resultado.

print("\nCalculadora factorial\n")

def calculadora_factorial(numero):
    if (numero < 0):
        return "El factorial de '0' no está definido para números negativos."

    # Inicilizamos el factorial en 1
    factorial = 1

    # Crea un número que va desde 1 hasta numero (incluido)
    # Genera una secuencia de números desde 1 hasta numero, lo que permite multiplicar cada uno para calcular el factorial.
    for i in range(1, numero + 1):
        # Es una forma abreviada de poner factorial = factorial * i
        # En cada iteración del bucle, i se multiplica con el valor actual de factorial, acumulando el producto de los números desde 1 hasta numero.
        factorial *= i
    return factorial

# Solicitamos el número al usuario
numero_usuario = int(input("Ingresa un número para calcular su factorial: "))

# Calcular el factorial
resultado = calculadora_factorial(numero_usuario)

# Salida
print(f"El factorial de {numero_usuario} es: {resultado}")

    