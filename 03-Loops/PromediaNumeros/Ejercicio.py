"""
 
   ___ ___  ___  __  __ ___ ___ ___ ___  
  | _ \ _ \/ _ \|  \/  | __|   \_ _/ _ \ 
  |  _/   / (_) | |\/| | _|| |) | | (_) |
  |_| |_|_\\___/|_|  |_|___|___/___\___/ 
                                         
 
"""

#El programa pedira numeros para promediarlos , para salir ingresa -1
contador = 0
suma = 0
numero = 0

#Ciclo infinito
while True:
    numero = int(input("Escribe un numero para suma, (Ingresa '-1' para salir): "))

    if (numero == -1):
        #Si el usuario ingresa "-1" ejecuta "break" para salir del ciclo
        break
    #Si el usuario ingresa numeros naturales la variable "suma" ejecuta la instruccion mientras que la variable "contador" sigue acumulando la cuenta de los numeros ingresados
    suma+= numero
    contador+=1

#Si el contador acumulado es mayor a "0" entonces se calcula el promedio
if (contador > 0):
    promedio = suma / contador
    print("La suma de los numeros es: " , suma)
    print("El total de los numeros introducidos es : " , contador)
    print("El promedio de los numeros ingresados es : " , promedio)
else:
    print("No se ingresaron numeros validos")
