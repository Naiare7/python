#TRY

#Ejemplo 1

# try:                                # Intenta ejecutar este bloque de código
#   print(x)
# except:                             # Si ocurre un error en el bloque anterior (ej. 'x' no está definida),
#   print("An exception occurred")      #se ejecuta este bloque para evitar que el programa se detenga.
  

#========================================================================================================================================#

# Ejemplo 2

# try:
#     numero = 10 / 0           
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
#     # En este caso, dividir por cero generará un ZeroDivisionError
# try:
#     x = 1/0
# except NameError:
#      print("You have a variable that is not defined.")    
   

# except TypeError:                                           
#     print("You are comparing values of different type")     

    

# except:
#     print(f"Something else went wrong")                     
    
# El bloque "except" genérico captura cualquier otro error no especificado arriba.
                                                              
    
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
#     archivo = open("datos.txt", "r")
# except FileNotFoundError:
#     print("Error: El archivo no existe.")

# else:
#     contenido = archivo.read()
#     print("Contenido leído con éxito.")
#     archivo.close()

# Solo ponemos la operación que puede fallar (abrir el archivo)
# Esto solo corre si el archivo se abrió correctamente
#=====================================================================================================================#
#=====================================================================================================================#

# FINALLY

# Ejemplo 1

# try:
#     print("1. Intentando realizar una operación...")
#     numero = 10 / 0  # Esto causará un error
# except ZeroDivisionError:
#     print("2. ¡Error! No se puede dividir por cero.")
# finally:
#     # Este bloque se ejecuta pase lo que pase
#     print("3. Finalizado: Limpieza ejecutada.")

# 1. El programa entra aquí primero e intenta ejecutar el código
# 2. Esta línea genera un error (división por cero) y salta de inmediato al 'except'
# 3. Como ocurrió un error de división por cero, este bloque lo captura
# 4. Sin importar si hubo error o no, este bloque se ejecuta OBLIGATORIAMENTE,se usa para tareas de limpieza (como cerrar archivos o liberar memoria)

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




