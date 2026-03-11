# ==========================================
# EL BUCLE WHILE (Control por Condición)
# ==========================================


# EJERCICIO: El depósito de agua
# Llenamos un depósito de 10 litros de 2 en 2.

# capacidad_maxima = 10  # capacidad en litros
# litros_actuales = 0    # cantidad inicial

# print(f"Estado inicial: {litros_actuales} litros.")  # mostrar estado

# while litros_actuales < capacidad_maxima:
#     litros_actuales += 2  # añadimos 2 litros por iteración
#     print(f"Llenando... Ahora hay {litros_actuales} litros.")  # mostrar progreso

# print("¡El depósito está lleno!")  # aviso final

# ---------------------------------------------------------
# # Palabra mágica
# # Bucle que pide al usuario hasta acertar la palabra secreta.

# palabra_secreta = "python"  # palabra objetivo
# intento = ""                 # variable para almacenar el intento

# print("\n--- Juego de la Palabra Secreta ---")
# while intento.lower() != palabra_secreta:
#     intento = input("Adivina la palabra secreta: ")  # pedimos intento
#     if intento.lower() != palabra_secreta:
#         print("Casi... ¡inténtalo de nuevo!")  # pista en caso de fallo

# print("¡Felicidades! Adivinaste la palabra.")  # mensaje de éxito
