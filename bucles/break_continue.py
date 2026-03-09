#BREAK
# Ejemplo 1:

# Itera hasta 10, pero interrumpe el bucle cuando i es igual a 5 usando break.

# for i in range(10):
#     if i ==5:
#        break 
#     print (i)

#=============================================================================================================================#

#Ejemplo 2:

# Iteramos sobre los números del 2 al 9
# Intentamos encontrar un divisor (x) para el número actual (n)
# Si el residuo es 0, n no es primo
# Imprime la descomposición y detiene la búsqueda para este n

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0: 
#             print(f"{n} equals {x} * {n//x}")
#             break

#=============================================================================================================================#
#=============================================================================================================================#

#CONTINUE
#Ejemplo 1:

# Iniciamos un bucle que va desde el 0 hasta el 4 (el 5 no se incluye)
# Verificamos si el valor actual de 'i' es igual a 2
# 'continue' detiene la ejecución de lo que queda de código DENTRO del bucle
# y salta inmediatamente a la siguiente vuelta (donde i vale 3)
# Imprime el valor de 'i' solo si no se ejecutó el 'continue'


# for i in range (5):
#      if i == 2:
#       continue
#      print(i)

#=============================================================================================================================#

#Ejemplo 2:

# Iteramos sobre un rango de números del 2 al 9 (el 10 no se incluye)
# Verificamos si el resto de dividir el número por 2 es cero (es par)
# 'continue' salta el resto del código en este ciclo y pasa al siguiente n
# Si el número no es par, el código llega hasta aquí

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Encontré un número par {num}")
#         continue
#     print(f"Encontré un número impar {num}")

