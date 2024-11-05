# Define una función es_palindromo(cadena) que tome una cadena de texto y devuelva True si es un palíndromo (es decir, si se lee igual de adelante hacia atrás) y False si no lo es.

print("\nPalíndromos\n")

def verificar_palindromo(cadena):

    # Convertir la cadena a minúscula y eliminar los espacios
    cadena = cadena.replace(" ", "").lower()

    # Verificar si la cadena es igual a su reverso
    # La sintaxis cadena[start:end:step] permite tomar una subcadena de cadena
    # Cuando usamos -1 como step, Python recorre la cadena desde el final hasta el inicio, efectivamente invirtiendo la cadena.
    # Ejemplo : Si cadena = "hola", entonces cadena[::-1] devolverá "aloh".
    return cadena == cadena[::-1]

# Entrada de datos
palabra = input("Ingresa una palabra: ")

# Llamar a la función y mostrar el resultado
if (verificar_palindromo(palabra)):
    print("La cadena es un palíndromo.")

else: 
    print("La cadena no es un palíndromo.")

