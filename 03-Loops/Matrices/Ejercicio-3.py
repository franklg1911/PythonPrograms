# Haz un programa que pida un entero positivo n y almacene en una variable M la matriz identidad de n × n (la que tiene unos (1) en la diagonal principal y ceros (0) en el resto de celdas). 
# Imprime la matriz en pantalla.

print("\nMatriz de identidad\n")

# Solicitamos el tamaño de la matriz de identidad

n = int(input("Introduce el número de positivo para el tamaño de la matriz de identidad: "))

# Creamos la matriz de identidad

# for i in range(n) recorre cada fila.
# for j in range(n) recorre cada columna.
# 1 if i == j else 0 : 
# Coloque 1 cuando el índice de fila (i) es igual al índice de columna (j) — esto es la diagonal principal.
# Coloque 0 en las otras posiciones.

M = [[1 if i == j else 0 for j in range (n)] for i in range(n)]

# Impresión

print("\nMatriz de identidad: ")

for fila in M:
    print(fila)