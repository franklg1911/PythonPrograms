#Programa para calcular el area de un cuadrado - circulo - triangulo

print("\nPrograma para calcular áreas de un cuadrado - circulo - triangulo")

opcion = input("\n¿Qué área deseas calcular?"
                 "\n A. Cuadrado"
                 "\n B. Circulo"
                 "\n C. Triángulo\n")

#Área del cuadrado
if (opcion == "A"):
    lado = float(input("Por favor ingrese el lado del cuadrado: "))
    area_cuadrado = lado * lado
    print("El área del cuadrado es: " , area_cuadrado)

#Área del circulo
elif (opcion == "B"):
    radio = float(input("Por favor ingrese el radio del circulo: "))
    area_circulo = 3.14 * (radio ** 2)
    print("El área del circulo es: " , area_circulo)

#Área del triangulo
elif (opcion == "C"):
    base = float(input("Por favor ingrese la base del triangulo: "))
    altura = float(input("Por favor ingrese la altura del triangulo: "))
    area_triangulo = (base * altura) / 2
    print("El área del triangulo es: " , area_triangulo)

else:
    print("Por favor ingrese una letra correcta")