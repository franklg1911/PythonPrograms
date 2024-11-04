# Crea una Matriz 4x4 que almacene los valores de un teclado matricial. Imprime la matriz, la cuarta fila y el asterisco (*) en pantalla.

# Creamos la matriz 4x4 del teclado matricial

print("\nTeclado matricial\n")

teclado = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D'],
]

# Imprimir toda la matriz
print("Matriz completa:")

for fila in teclado:
    print(fila)

# Imprimir la cuarta fila
print("\nCuarta fila: ", teclado[3])

# Imprimir el asterisco *
print("\nAsterisco *: ", teclado[3][0])