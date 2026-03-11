# ==========================================
# ESTRUCTURAS CONDICIONALES: if, elif, else
# ==========================================



# EJERCICIO: Recomendador de Ropa según la Temperatura
temperatura = 18  # temperatura en grados Celsius

print(f"La temperatura actual es de {temperatura}°C.")  # mostramos la temperatura

if temperatura < 10:
    # menos de 10°C -> muy frío
    print("Recomendación: Usa un abrigo pesado, hace mucho frío.")
elif temperatura < 20:
    # entre 10 y 19°C -> fresco
    print("Recomendación: Una chaqueta ligera será suficiente.")
elif temperatura < 30:
    # entre 20 y 29°C -> templado
    print("Recomendación: Hace buen tiempo, usa una camiseta.")
else:
    # 30°C o más -> calor
    print("Recomendación: Hace mucho calor, ¡busca una sombra y bebe agua!")

# ---------------------------------------------------------
# # OTRO EJEMPLO SENCILLO: Control de Luces
# luz_encendida = True  # estado booleano de la luz

# if luz_encendida:
#     # si la luz está encendida
#     print("\nLa habitación está iluminada.")
# else:
#     # si la luz está apagada
#     print("\nLa habitación está a oscuras.")
