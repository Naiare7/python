# print("\n#==========================================EJEMPLO 1=============================================================#\n")
# Aquí, articulo es una variable temporal que toma el valor de cada elemento en cada vuelta del bucle.


persona = {"name": "Juan", "edad": 2, "ciudad": 12}

for x, y in persona.items():
    print(f"Debo comprar: {x}: {y}")

# print("\n#============================================EJEMPLO 2===========================================================#\n")

# En Python, un texto es una secuencia de caracteres, por lo que puedes recorrerlo letra por letra.
# palabra = "Python"

# for letra in palabra:
#     print(letra.upper())


# print("\n#=============================================EJEMPLO 3==========================================================#\n")

# Cuando trabajas con diccionarios (clave: valor), puedes recorrer ambos al mismo tiempo usando .items().
# precios = {"manzana": 1.5, "banana": 0.8, "coco": 2.0}

# for fruta, precio in precios.items():
#     print(f"La {fruta} cuesta {precio} euros.")


# print("\n#=============================================EJEMPLO 4==========================================================#\n")

precios = [100, 25, 150, 40, 500]
precios_con_descuento = []

# # Usamos el FOR para revisar cada precio uno por uno
for precio in precios:
    # Si el precio es mayor a 50, aplicamos el descuento
    if precio > 50:
        nuevo_precio = precio * 0.80
        print(f"Producto de ${precio} rebajado a: ${nuevo_precio}")
    else:
        nuevo_precio = precio
        print(f"Producto de ${precio} mantiene su precio.")
    
    # Guardamos el resultado en nuestra nueva lista
    precios_con_descuento.append(nuevo_precio)

print(f"\nLista final de precios: {precios_con_descuento}")


# print("\n#========================================FOR IN RANGE=========================================================#\n")

# Si solo pasas un número, Python asume que empiezas en 0 y quieres llegar justo antes de ese número.
for i in range(3):
    print(f"Vuelta número: {i}")


# print("\n#=========================================EJEMPLO 1==============================================================#\n")

# Útil cuando no quieres empezar desde cero. Recuerda: el primer número se incluye, el último no.
for n in range(5, 9):
    print(n)


# print("\n#=========================================EJEMPLO 2==============================================================#\n")

# El tercer parámetro es el paso o incremento. Por defecto es 1, pero puedes cambiarlo para ir de dos en dos, de diez en diez, etc.
for par in range(2, 11, 2):
    print(par)


# print("\n#=========================================EJEMPLO 3==============================================================#\n")

# Para ir hacia atrás, el "paso" debe ser un número negativo.
for segundo in range(5, 0, -1):
    print(f"T-minus {segundo}...")

print("¡Despegue! 🚀")


# print("\n#=========================================EJEMPLO 4==============================================================#\n")

# Este es un patrón clásico cuando necesitas el índice (la posición) de los elementos de una lista mientras los recorres.
frutas = ["Manzana", "Pera", "Mango"]

for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")


# print("\n#=========================================EJEMPLO 5==============================================================#\n")

password_correcta = "admin123"

# # Usamos range(1, 4) para que los intentos se cuenten como 1, 2 y 3
for intento in range(1, 4):
    print(f"--- Intento {intento} de 3 ---")
    password_ingresada = input("Introduce la contraseña: ")

    if password_ingresada == password_correcta:
        print("¡Acceso concedido! Bienvenido.")
        break  # Rompemos el bucle porque ya no necesitamos más intentos
    else:
        # Usamos un ternario para el mensaje de error
        if intento < 3:
            print("Contraseña incorrecta. Inténtalo de nuevo.\n")
        else:
            print("Acceso denegado. Tu cuenta ha sido bloqueada.")