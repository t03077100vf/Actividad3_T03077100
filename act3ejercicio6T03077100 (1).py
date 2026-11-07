print("Ejercicio 6: Validar los datos de una alta")
print("Vanessa Fernández")
print("T03077100")
print()

nombre = input("Nombre del producto: ")
while nombre == "":
    print("El nombre no puede estar vacío")
    nombre = input("Nombre del producto: ")

precio = int(input("Precio: $"))
while precio <= 0:
    print("El precio debe ser mayor que 0")
    precio = int(input("Precio: $"))

piezas = int(input("Piezas en bodega: "))
while piezas < 0:
    print("Las piezas no pueden ser negativas")
    piezas = int(input("Piezas en bodega: "))

categoria = ""
categoria_valida = False

while categoria_valida == False:
    print("Categorías: 1. Tenis 2. Ropa 3. Accesorios")
    opcion = input("Elige la categoría: ")
    
    if opcion == "1":
        categoria = "Tenis"
        categoria_valida = True
    elif opcion == "2":
        categoria = "Ropa"
        categoria_valida = True
    elif opcion == "3":
        categoria = "Accesorios"
        categoria_valida = True
    else:
        print("Esa categoría no existe")

print()
print("<3<3<3 FICHA DEL PRODUCTO <3<3<3")
print("Nombre:", nombre)
print("Precio: $", precio)
print("Piezas:", piezas)
print("Categoría:", categoria)

respuesta_valida = False

while respuesta_valida == False:
    guardar = input("¿Guardar? (s/n): ")
    
    if guardar == "s":
        print("Producto guardado")
        respuesta_valida = True
    elif guardar == "n":
        print("Alta cancelada")
        respuesta_valida = True
    else:
        print("Escribe solo s o n")