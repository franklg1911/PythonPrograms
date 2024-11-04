# Haz un programa para crear una matriz nula Mmxn, donde se le solicite al usuario su dimensión m x n, (m son las filas y n son las columnas). 
# Imprime cada fila de la matriz en pantalla.

print("\nMatriz Nula\n")

m = int(input("Ingresa las filas por favor: "))
n = int(input("Ingresa las columnas por favor: "))

# Creamos la matriz nula

# range(n) : genera una secuencia de "n" elementos (del 0 al n-1)
# for _ in range(n) : recorre una secuencia y para cada posición, coloca un 0 en la lista
# El resultado es una lista de n ceros, como [0, 0, 0] si n = 3.

# [[0 for _ in range(n)] for _ in range(m)]
# for _ in range(m) : recorre m veces y, en cada iteración, genera una nueva fila de n ceros.
# El resultado final es una lista de listas, donde cada sublista representa una fila de la matriz.
# Ejemplo si el usuario ingresa m = 3 y n = 4
# matriz = [
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0]
# ]

matriz = [[0 for _ in range(n)] for _ in range(m)]

# Impresión

print("\nMatriz nula: ")

for fila in matriz:
    print(fila)