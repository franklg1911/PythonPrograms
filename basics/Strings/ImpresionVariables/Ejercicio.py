#Escribe un programa que solicite al usuario ingresar su nombre, edad, y altura. Luego, imprime un mensaje que combine estos datos en una oración.

print("\nImpresion de mensaje\n")

nombre = input("Por favor ingrese su nombre: \n")
edad = int(input("Por favor ingresa tu edad: \n"))
altura = float(input("Por favor ingresa tu altura: \n"))

print(f"Tu nombre es {nombre} tienes una edad de {edad} y una altura de {altura}")
