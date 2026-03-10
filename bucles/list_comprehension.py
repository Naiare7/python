# ==========================================
# LIST COMPREHENSION
# ==========================================


# EJERCICIO: Filtrar nombres cortos
# Queremos una lista con los nombres que tienen 4 letras o menos.

nombres = ["Ana", "Roberto", "Luz", "Catalina", "Juan", "Pedro"]

# FORMA TRADICIONAL (Para juniors que vienen de otros lenguajes)
nombres_cortos_tradicional = []
for nombre in nombres:
    if len(nombre) <= 4:
        nombres_cortos_tradicional.append(nombre)

# FORMA CON LIST COMPREHENSION
nombres_cortos_pythonico = [nombre for nombre in nombres if len(nombre) <= 4]

print("Lista original:", nombres)
print("Nombres cortos (Tradicional):", nombres_cortos_tradicional)
print("Nombres cortos (Pythónico):", nombres_cortos_pythonico)

# ---------------------------------------------------------
# OTRO EJERCICIO: Convertir a Mayúsculas
# De una lista, queremos solo las palabras que empiecen por 'J' en mayúsculas.

frutas = ["manzana", "jamón", "pera", "jícama", "uva"]

solo_j_mayus = [f.upper() for f in frutas if f.startswith('j')]

print("\nFrutas que empiezan con J en mayúsculas:", solo_j_mayus)
