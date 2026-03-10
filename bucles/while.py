# ==========================================
# EL BUCLE WHILE (Control por Condición)
# ==========================================



# EJERCICIO: El depósito de agua
# Tenemos un depósito de 10 litros y lo vamos llenando de 2 en 2.

capacidad_maxima = 10
litros_actuales = 0

print(f"Estado inicial: {litros_actuales} litros.")

while litros_actuales < capacidad_maxima:
    litros_actuales += 2
    print(f"Llenando... Ahora hay {litros_actuales} litros.")

print("¡El depósito está lleno!")

# ---------------------------------------------------------
# Palabra mágica
# El programa se repite hasta que el usuario adivine la palabra.

palabra_secreta = "python"
intento = ""

print("\n--- Juego de la Palabra Secreta ---")
while intento.lower() != palabra_secreta:
    intento = input("Adivina la palabra secreta: ")
    if intento.lower() != palabra_secreta:
        print("Casi... ¡inténtalo de nuevo!")

print("¡Felicidades! Adivinaste la palabra.")
