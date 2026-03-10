# ==========================================
# ESTRUCTURAS CONDICIONALES: if, elif, else
# ==========================================



# EJERCICIO: Recomendador de Ropa según la Temperatura
temperatura = 18

print(f"La temperatura actual es de {temperatura}°C.")

if temperatura < 10:
    print("Recomendación: Usa un abrigo pesado, hace mucho frío.")
elif temperatura < 20:
    print("Recomendación: Una chaqueta ligera será suficiente.")
elif temperatura < 30:
    print("Recomendación: Hace buen tiempo, usa una camiseta.")
else:
    print("Recomendación: Hace mucho calor, ¡busca una sombra y bebe agua!")

# ---------------------------------------------------------
# OTRO EJEMPLO SENCILLO: Control de Luces
luz_encendida = True

if luz_encendida:
    print("\nLa habitación está iluminada.")
else:
    print("\nLa habitación está a oscuras.")
