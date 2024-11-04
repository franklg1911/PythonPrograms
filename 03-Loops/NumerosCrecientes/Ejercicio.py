# Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente.

print("\nNúmeros pares de forma creciente de 0 a 200\n")

# 0 : inicio del rango
# 201 : es el límite superior (201 no incluido)
# 2 : es el paso , asegura que solo se consideren números pares

for i in range (0, 201, 2):
    print(i)
