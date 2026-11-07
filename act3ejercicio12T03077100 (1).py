print("Ejercicio 12: Alta de productos con folio")
print("Vanessa Fernández")
print("T03077100")
print()

cuantos = int(input("¿Cuántos productos vas a dar de alta? "))

valor_total = 0

for numero in range(1, cuantos + 1):
    folio = "SNK" + str(numero)
    
    print()
    print("📦 Producto con folio", folio)
    nombre = input("Nombre: ")
    
    precio = int(input("Precio: $"))
    while precio <= 0:
        print("El precio debe ser mayor que 0")
        precio = int(input("Precio: $"))
        
    piezas = int(input("Piezas en bodega: "))
    
    valor = precio * piezas
    valor_total = valor_total + valor
    
    print("Alta exitosa")
    print("Folio:", folio, "• Nombre:", nombre)
    print("Precio: $", precio, "• Piezas:", piezas, "• Valor: $", valor)

