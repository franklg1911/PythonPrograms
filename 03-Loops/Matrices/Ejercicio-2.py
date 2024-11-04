# Crea una matriz 3x3 que almacene los valores del 1 al 9. El tamaño de la matriz indica la cantidad de filas. Imprime cada fila de la matriz en pantalla.

print("\nMatriz de 3 dimensiones")

matriz = [
    ['1', '3', '2'],
    ['4', '5', '8'],
    ['7', '6', '9']
]

# Imprimir toda la matriz
print("Matriz 3x3")

for fila in matriz:
    print(fila)

# Imprimir cada fila
print("\nPrimera fila: ", matriz[0])
print("Segunda fila: ", matriz[1])
print("Tercera fila: ", matriz[2])