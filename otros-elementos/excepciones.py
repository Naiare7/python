#TRY

#Ejemplo 1

# try:                                # Intenta ejecutar este bloque de código
#   print(x)
# except:                             # Si ocurre un error en el bloque anterior (ej. 'x' no está definida),
#                                     #se ejecuta este bloque para evitar que   el programa se detenga.
#   print("An exception occurred")

#========================================================================================================================================#

# Ejemplo 2

# try:
#     numero = 10 / 0  # Esto va a fallar
#     print("¡Hecho!") # Esta línea nunca se ejecutará
# except:
#     print("Oye, no puedes dividir por cero.")

#no se puede dividir entre 0.

#=======================================================================================================================================#
#=========================================================================================================================================#

#EXCEPT

# Ejemplo 1

# x = "hello"

# try:
#   x > 3
# except NameError:
#   print("You have a variable that is not defined.")
# except TypeError:
#   print("You are comparing values of different type")


# Ejemplo 2

 # Intento de realizar una operación aritmética
    # En este caso, dividir por cero generará un ZeroDivisionError
try:
    x = 1/0
except NameError:
     print("You have a variable that is not defined.")    # Se ejecuta si intentas usar una variable que no ha sido declarada
   

except TypeError:                                           # Se ejecuta si realizas una operación con tipos de datos incompatibles
                                                            # (Ejemplo: sumar un número con una cadena de texto)

    print("You are comparing values of different type")

except Exception as e:
    # El bloque "except" genérico captura cualquier otro error no especificado arriba.
    # En este script, aquí es donde entrará el error de "división por cero"
    # ya que no definiste un bloque específico para ZeroDivisionError.
    print(f"Something else went wrong: {e}")
