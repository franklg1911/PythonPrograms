# Crea un programa que solicite la edad del usuario y lo clasifique en categorías como "Niño", "Adolescente", "Adulto" o "Senior", basándote en rangos de edades.

print("\nClasificación por edad a una persona\n")

edad = int(input("Ingrese la edad de la persona: "))

if (edad >= 0 and edad <= 12):
    categoria = "Niño"

elif (edad >= 13 and edad <=17):
    categoria = "Adolescente"

elif (edad >= 18 and edad <= 64):
    categoria = "Adulto"

elif(edad >= 65):
    categoria = "Senior"

print(f"La persona es un {categoria}")