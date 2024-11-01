# Crear un Algoritmo que permita hallar la solución a una ecuación de segundo grado. Los datos del problema son los coeficientes a, b y c. Se desea calcular los valores de x que hacen cierta la ecuación.

# Consideraciones:

# - En este programa se debe considerar la división por cero que tiene lugar cuando a vale 0 haciendo entonces al denominador, 2a, nulo. Cuando a vale 0 la ecuación no es de segundo grado, sino de primer grado.

# - Otra consideración que debemos tomar en cuenta es que el discriminante (b2- 4ac) no debe ser negativo, de ser negativo la ecuación no tiene soluciones reales.

# Se deben tomar en cuenta los siguientes escenarios:

# 1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.

# Si b es DIFERENTE de 0 (b! = 0) la ecuación no tiene solución.

# Se b es IGUAL a 0 (b == 0) se produce la división por cero, y la ecuación tiene infinitas soluciones.

# ___

# ► Variables

# a: Coeficiente principal.

# b: Coeficiente secundario.

# c: Término Independiente.

# x1: Incógnita 1.

# x2: Incógnita 2.

# discriminante: Discriminante de la ecuación.

print("\nEcuación de segundo grado\n")

#Importamos el módulo "math" para utilizar la función "sqrt"
import math

#Solicitamos al usuario los 3 valores
a = float(input("Ingresar el valor de a (coeficiente de x^2): "))
b = float(input("Ingresar el valor de b (coeficiente de x): "))
c = float(input("Ingresar el valor de c (término independiente): "))

#Evaluar los posibles casos
if (a == 0):
    print("No es una ecuación de segundo grado porque es igual a 0.")    

else: 
    discriminante = b**2 - 4*a*c 

    if (discriminante > 0) : #Dos soluciones reales y diferentes
        x1 = (-b + math.sqrt(discriminante)) / (2* a)
        x2 = (-b - math.sqrt(discriminante)) / (2* a)
        print(f"La ecuación tiene dos soluciones reales diferente: x1 = {x1:.2f} y x2 = {x2:.2f}")
    
    elif (discriminante == 0): #Existe una solución única
        x = -b / (2 * a)
        print(f"La ecuación solamente tiene una solución única: x = {x:.2f2}")
    
    else: # No existe soluciones reales
        print("La ecuación no tiene soluciones reales")