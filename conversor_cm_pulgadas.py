 # Paso 1: Solicitar al usuario las medidas de las piezas del mueble en cm.
medida_en_cm = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cm): "))

# Paso 2: Convertir las medidas de cm a pulgadas.

medida_en_pulgadas = medida_en_cm / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario.

print("Las medidas de la pieza ingresada son: ",medida_en_pulgadas)