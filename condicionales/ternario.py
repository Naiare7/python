
# Ideal para mostrar mensajes personalizados en interfaces de usuario o aplicaciones web.
usuario_premium = True

mensaje = "Acceso total concedido" if usuario_premium else "Acceso limitado"
print(mensaje)


#_______________________________________________________________________________________________________#


# Puedes usarlo para realizar operaciones matemáticas rápidas basadas en una condición.
# Si la compra es mayor a 100, aplica 10% de descuento, si no, 0.
total_compra = 150
descuento = 0.10 if total_compra > 100 else 0.0

pago_final = total_compra * (1 - descuento)
print(f"Total a pagar: ${pago_final}") # Resultado: $135.0


#_______________________________________________________________________________________________________#


# Un uso muy inteligente es para gramática automática en tus programas.
# Si cantidad es 1, usa "ítem", si es distinto, "ítems"
items = ["manzana"]
cantidad = len(items)

etiqueta = "ítem" if cantidad == 1 else "ítems"

print(f"Tienes {cantidad} {etiqueta} en el carrito.")
# Resultado: Tienes 1 ítem en el carrito.


#_______________________________________________________________________________________________________#


# No necesitas crear una variable intermedia; puedes usar el ternario directamente donde lo necesites.
temperatura = 12
print(f"El motor está {'CALIENTE' if temperatura > 90 else 'FRÍO'}.")


#_______________________________________________________________________________________________________#


# Este método evalúa ambos valores antes de elegir uno, mientras que el ternario normal con if solo evalúa el que corresponde (es más eficiente)
edad = 20
estado = ("Menor", "Adulto")[edad >= 18]

print(f"Eres un {estado}.")