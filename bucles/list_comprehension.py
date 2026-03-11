"""
Ejemplos de uso de list comprehensions (comprensiones de lista).

Este archivo muestra varios patrones comunes:
- Filtrar elementos según una condición (nombres cortos).
- Transformar elementos aplicando una función (convertir a mayúsculas).

Los ejemplos muestran la versión "tradicional" con bucles y la
versión pythónica usando list comprehension, que es más concisa.
"""


# EJERCICIO 1: Filtrar nombres cortos (longitud <= 4)
# Definimos una lista de ejemplo con varios nombres.

nombres = ["Ana", "Roberto", "Luz", "Catalina", "Juan", "Pedro"]

# --- Forma tradicional usando bucles y append ---
# Recorremos cada nombre, comprobamos la condición y añadimos manualmente.
nombres_cortos_tradicional = []
for nombre in nombres:
    # Si el nombre tiene 4 o menos caracteres, lo guardamos
    if len(nombre) <= 4:
        nombres_cortos_tradicional.append(nombre)


# --- Forma pythónica usando list comprehension ---
# Sintaxis: [expresión for item in iterable if condición]
# Aquí la expresión es el propio `nombre` (sin transformar).
nombres_cortos_pythonico = [nombre for nombre in nombres if len(nombre) <= 4]


print("Lista original:", nombres)
print("Nombres cortos (Tradicional):", nombres_cortos_tradicional)
print("Nombres cortos (Pythónico):", nombres_cortos_pythonico)


# ---------------------------------------------------------
# EJEMPLO 2: Convertir a mayúsculas solo las frutas que empiezan por 'j'
# Creamos otra lista de ejemplo con palabras en minúscula.
# frutas = ["manzana", "jamón", "pera", "jícama", "uva"]

# Usamos list comprehension para filtrar (startswith) y transformar (upper)
# Observaciones:
# - `f.startswith('j')` comprueba la primera letra literal 'j' (minúscula).
# - `f.upper()` devuelve la versión en mayúsculas de la cadena.
# solo_j_mayus = [f.upper() for f in frutas if f.startswith('j')]

# print("\nFrutas que empiezan con J en mayúsculas:", solo_j_mayus)
