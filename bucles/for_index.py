# Enumerate

# Ejemplo 1

# list_name = ['apple', 'banana', 'cherry']

# for index, value in enumerate(list_name):
#     print(f"Index: {index}, Value: {value}")


# Definimos una lista de strings con nombres de frutas
# Usamos un bucle 'for' junto con 'enumerate' para obtener 
# tanto la posición (index) como el elemento (value) de la lista
# Imprimimos los datos usando un f-string para dar formato a la salida
#================================================================================================================================#

# Ejemplo 2

# ciudades = ["Barcelona", "Bilbao", "Sevilla", "Bilbao", "Valencia", "Bilbao"]
# objetivo = "Bilbao"
# posiciones = []

# for i, ciudad in enumerate(ciudades):
#     if ciudad == objetivo:
#         posiciones.append(i)

# print(f"La ciudad '{objetivo}' se encontró en los índices: {posiciones}")

# Usamos enumerate para obtener el índice (i) y el valor (ciudad) al mismo tiempo

#=================================================================================================================================#
#=================================================================================================================================#

#range(len(list)

#Ejemplo 1

# frutas = ['manzana', 'banana', 'cereza']

# for i in range(len(frutas)):

#      print (f"Índice:{i}, Fruta: {frutas[i]}")

# Definimos una lista que contiene nombres de frutas (strings)
# Iniciamos un bucle que recorre un rango de números desde 0 hasta el largo de la lista
# len(frutas) nos da 3, por lo que range(3) genera los índices: 0, 1 y 2
#===================================================================================================================================#

# Ejemplo 2
# Escenario: Imagina que tienes una lista con las temperaturas máximas de una semana. Queremos crear una "alerta" cada vez que la temperatura de un día sea mayor que la del día anterior (un incremento térmico).



# temperaturas = [22, 25, 24, 28, 30, 29, 31]
# # Dias:         0   1   2   3   4   5   6

# print("--- Reporte de Incrementos ---")

# for i in range(1, len(temperaturas)):
#     temp_actual = temperaturas[i]
#     temp_anterior = temperaturas[i - 1]
    
#     if temp_actual > temp_anterior:
#         diferencia = temp_actual - temp_anterior
#         print(f"Día {i}: ¡Subió la temperatura! ({temp_actual}°C). Aumentó {diferencia}°C respecto al día anterior.")

#  Usamos range(len()) empezando desde el índice 1
#  porque el primer día (índice 0) no tiene un día anterior para comparar.

#============================================================================================================================================#
#============================================================================================================================================#