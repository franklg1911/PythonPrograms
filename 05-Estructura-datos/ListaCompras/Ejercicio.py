# Crea un programa que permita al usuario ingresar elementos a una lista de compras hasta que ingrese la palabra “salir”. Al final, muestra todos los elementos en la lista.

print("\nLista de compras\n")

lista_compras = [] # Una lista vacía

print("Ingresar los productos a la lista. Escriba 'salir' para cerrar la lista\n")

while True:
    producto = input("Ingresa el producto: ")

    if producto == "salir":
        break #Rompe el bucle

    lista_compras.append(producto) #Agrega los productos a la lista de compras

print("La lista de compras es: " , lista_compras)