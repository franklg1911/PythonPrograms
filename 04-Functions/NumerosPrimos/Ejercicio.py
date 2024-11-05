# Crea un programa que pida un número al usuario y utilice un bucle for para determinar si es primo.

print("\nNumeros primos\n")

#Función para determinar si un número es primo

def num_primo (num):
    if num <=1 :
        return False #Los números menores a 1 o iguales no son primos
    
    for i in range(2, num): # Generamos una secuencia de números del 2 hasta el num (-1) , comprobaremos los números que estan entre 2 y -1
        if (num % i == 0): # Verificamos si "num" es divisible por "i" esto se hace con la operación "%" que devuelve el residuo de la división de "num" por "i"
            return False
    
    return True # Si no encontramos ningun divisor , es primo

numero = int(input("Ingresa un número: "))

if num_primo(numero):
    print(f"{numero} es un númeo primo")

else:
    print(f"{numero} no es número primo")

