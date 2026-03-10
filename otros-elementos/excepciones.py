#TRY

#Ejemplo 1

# try:                                # Intenta ejecutar este bloque de código
#   print(x)
# except:                             # Si ocurre un error en el bloque anterior (ej. 'x' no está definida),
#   print("An exception occurred")      #se ejecuta este bloque para evitar que   el programa se detenga.
#   

#========================================================================================================================================#

# Ejemplo 2

# try:
#     numero = 10 / 0           # Esto va a fallar
#     print("¡Hecho!")          # Esta línea nunca se ejecutará
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

#=========================================================================================================================================#

# Ejemplo 2

 # Intento de realizar una operación aritmética
    # En este caso, dividir por cero generará un ZeroDivisionError
# try:
#     x = 1/0
# except NameError:
#      print("You have a variable that is not defined.")    # Se ejecuta si intentas usar una variable que no ha sido declarada
   

# except TypeError:                                           # Se ejecuta si realizas una operación con tipos de datos incompatibles
#     print("You are comparing values of different type")     # (Ejemplo: sumar un número con una cadena de texto)

    

# except:
#     print(f"Something else went wrong")                     # El bloque "except" genérico captura cualquier otro error no especificado arriba.
                                                            # En este script, aquí es donde entrará el error de "división por cero"
                                                            # ya que no definiste un bloque específico para ZeroDivisionError.
    
#===========================================================================================================================================#

# ELSE

# Ejemplo 1

# try:
#   print("Hello")                    # Intenta ejecutar este código
# except:
#   print("Something went wrong")     # Se ejecuta si ocurre un error en el bloque try
# else:
#   print("Nothing went wrong")       # Se ejecuta solo si NO hubo errores

# Ejemplo 2

# try:
#     # Solo ponemos la operación que puede fallar (abrir el archivo)
#     archivo = open("datos.txt", "r")
# except FileNotFoundError:
#     print("Error: El archivo no existe.")
# else:
#     # Esto solo corre si el archivo se abrió correctamente
#     contenido = archivo.read()
#     print("Contenido leído con éxito.")
#     archivo.close()

#=====================================================================================================================#
#=====================================================================================================================#

# FINALLY

# Ejemplo 1

# try:
#   f = open("demofile.txt")              # Intenta abrir el archivo. Por defecto es modo lectura ('r')
#   try:
#     f.write("Lorum Ipsum")              # Intenta escribir. Esto fallará porque el archivo no se abrió en modo escritura ('w' o 'a')
#   except:                               # Se ejecuta si hay un error al intentar escribir
#     print("Something went wrong when writing to the file")
#   finally:                              
#     f.close()                           # Se asegura de cerrar el archivo siempre, ocurra o no un error
# except:                                 # Se ejecuta si el archivo no existe o no se pudo abrir
#   print("Something went wrong when opening the file")


#=====================================================================================================================#

# Ejemplo 2

# try:
#     with open("demofile.txt", "r") as f:
#         f.write("Lorum Ipsum") 
# except Exception as e:
#     print(f"¡Error capturado!: {e}")

# Intentamos abrir el archivo "demofile.txt" en modo lectura ("r" de read)
# El uso de 'with' asegura que el archivo se cierre automáticamente al terminar
# Esta línea provocará un error (io.UnsupportedOperation) porque el modo "r" no permite la función write()
# Aquí se captura el error resultante para que el programa no se detenga bruscamente
# Se imprime el mensaje descriptivo del error (ej: "not writable")

#=====================================================================================================================#
#=====================================================================================================================#