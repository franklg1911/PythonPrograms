# Crea una función calcular_iva(precio, porcentaje=18) que tome un precio y calcule el IVA aplicando el porcentaje dado (18% por defecto). Permite al usuario ingresar un precio y llama a la función para mostrar el precio con IVA incluido.

print("\nCalculadora de IVA\n")

def calcular_iva (precio, porcentaje=18):

    # Calcular IVA
    iva = precio * (porcentaje / 100)

    # Calcular el precio total con IVA
    precio_total = precio + iva
    return precio_total

# Entrada de datos
precio_ingresado = float(input("Ingresa el precio: "))

# Llamar a la función y mostrar el resultado
precio_con_iva = calcular_iva(precio_ingresado)
print(f"El precio con IVA incluido es: {precio_con_iva:.2f}")