# Crea un programa que pida una palabra al usuario y use un bucle for para contar cuántas vocales contiene.

print("\nContar vocales de una palabra")

palabra = input("\nIngresa una palabra: ")

vocales = "aeiouAEIOU"
contador = 0

#Bucle para contar vocales
for i in palabra:
    if i in vocales:
        contador +=1

print(f"La palabra {palabra} contiene {contador} vocales")