# Crea una función maximo_de_tres(a, b, c) que reciba tres números y devuelva el mayor de ellos.

def maximo_numero(a,b,c):

    if (a >= b and a >= c):
        return a

    elif (b >= a and b >= c):
        return b

    else:
        return c

# Entrada de datos
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Llamar a la función
mayor = maximo_numero(num1, num2, num3)
print(f"El mayor de los tres números es : {mayor}")

    
