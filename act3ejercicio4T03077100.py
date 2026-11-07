print("Ejercicio 4: La caja registradora de la cafetería")
print("Vanessa Fernández")
print("T03077100")
print()

total = 0
productos = 0

termina = False

while termina == False:
    print("<3<3<3 Nuevo producto <3<3<3")
    nombre = input("Producto (escribe fin para cobrar): ")
    
    if nombre == "fin":
        termina = True
    else:
        precio = int(input("Precio de " + nombre + ": $"))
        cantidad = int(input("¿Cuántos quiere? "))
        
        subtotal = precio * cantidad
        
        total = total + subtotal
        productos = productos + cantidad
        
        print("", cantidad, nombre, "=", "$", subtotal)
        print("Llevas $", total)

print()
print("<3<3<3 TICKET <3<3<3")
print("Productos:", productos)
print("Total: $", total)

if total >= 200:
    total = total - 20
    print("Descuento de $20 aplicado")
    print("Total con descuento: $", total)

pago = int(input("¿Con cuánto pagas? $"))

while pago < total:
    print("No alcanza. Faltan $", total - pago)
    pago = int(input("¿Con cuánto pagas? $"))

cambio = pago - total
print("Pago recibido. Tu cambio es: $", cambio)
print("¡Gracias por tu compra!")