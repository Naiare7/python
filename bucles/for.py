
# Aquí, articulo es una variable temporal que toma el valor de cada elemento en cada vuelta del bucle.
compras = ["pan", "leche", "huevos"]

for articulo in compras:
    print(f"Debo comprar: {articulo}")


# print("\n#_______________________________________________________________________________________________________#\n")

# En Python, un texto es una secuencia de caracteres, por lo que puedes recorrerlo letra por letra.
# palabra = "Python"

# for letra in palabra:
#     print(letra.upper())


# print("\n#_______________________________________________________________________________________________________#\n")

# Cuando trabajas con diccionarios (clave: valor), puedes recorrer ambos al mismo tiempo usando .items().
# precios = {"manzana": 1.5, "banana": 0.8, "coco": 2.0}

# for fruta, precio in precios.items():
#     print(f"La {fruta} cuesta {precio} euros.")


# print("\n#_______________________________________________________________________________________________________#\n")

# Si solo pasas un número, Python asume que empiezas en 0 y quieres llegar justo antes de ese número.
# for i in range(3):
#     print(f"Vuelta número: {i}")


# print("\n#_______________________________________________________________________________________________________#\n")

# Útil cuando no quieres empezar desde cero. Recuerda: el primer número se incluye, el último no.
# for n in range(5, 9):
#     print(n)


# print("\n#_______________________________________________________________________________________________________#\n")

# El tercer parámetro es el paso o incremento. Por defecto es 1, pero puedes cambiarlo para ir de dos en dos, de diez en diez, etc.
# for par in range(2, 11, 2):
#     print(par)


# print("\n#_______________________________________________________________________________________________________#\n")

# Para ir hacia atrás, el "paso" debe ser un número negativo.
# for segundo in range(5, 0, -1):
#     print(f"T-minus {segundo}...")

# print("¡Despegue! 🚀")


# print("\n#_______________________________________________________________________________________________________#\n")

# Este es un patrón clásico cuando necesitas el índice (la posición) de los elementos de una lista mientras los recorres.
# frutas = ["Manzana", "Pera", "Mango"]

# for i in range(len(frutas)):
#     print(f"Índice {i}: {frutas[i]}")