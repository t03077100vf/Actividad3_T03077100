print("Ejercicio 14: Altas en el inventario")
print("Vanessa Fernández")
print("T03077100")
print()

inventario = []

termina = False

while termina == False:
    nuevo = input("Producto a agregar (escribe fin para terminar): ")
    
    if nuevo == "fin":
        termina = True
    elif nuevo == "":
        print("El producto no puede estar vacío")
    elif nuevo in inventario:
        print("", nuevo, "ya está en el inventario")
    else:
        inventario.append(nuevo)
        print("Agregado. Llevas", len(inventario), "productos")

print()
print("<3<3<3 INVENTARIO <3<3<3")

if len(inventario) == 0:
    print("No agregaste productos")
else:
    for i in range(len(inventario)):
        print(i + 1, ".", inventario[i])