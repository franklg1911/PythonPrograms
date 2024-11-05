# Define una función que cuente cuántas palabras hay en una frase ingresada como argumento.

print("\nContador de palabras\n")

def contador_palabras():
    frase = input("Ingresa la frase para contar las palabras: ")
    palabras = frase.split()
    return len(palabras)

print("Número de palabras: ", contador_palabras())

