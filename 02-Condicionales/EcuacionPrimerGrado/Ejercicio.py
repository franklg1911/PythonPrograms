# Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado básica, de la forma: ax + b = 0
# El objetivo es despejar la x y validar los posibles datos para arrojar la respuesta.

# Al despejar la x tendremos que:
# x = -b/a

# Por lo tanto tendremos los siguientes escenarios:

# 1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.

# 2) Si a es IGUAL a 0 (a == 0) tendremos que:

# Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.

# Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones.

# ___

# ► Variables:

# a: Coeficiente principal.

# b: Término Independiente.

# x: Incógnita.

# ___

# ► Datos de Prueba.

# a) a = 2 y b = 6.

# b) a = 0 y b = 3.

# c) a = 0 y b = 0.

print("\nEcuación de primer grado\n")

#Solicitamos al usuario ingresar datos
a = float(input("Ingresar el valor de a: "))
b = float(input("Ingresar el valor de b: "))

#Evaluar posibles casos
#Case 1: a es diferente de 0
if (a != 0): 
    x = -b / a #Despejamos en "x"
    print(f"La solución de la ecuación es : x = {x}")

#Case 2: a es igual a 0
elif (a == 0):
    if (b != 0): #Subcaso 2.1 : b es diferente de 0
        print("La ecuación no tiene solución")

    else: #Subcaso 2.2 : b es igual a 0
        print("La ecuación tiene infinitas soluciones")