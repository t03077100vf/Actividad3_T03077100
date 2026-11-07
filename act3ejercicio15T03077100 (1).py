print("Ejercicio 15: Bajas en el inventario")
print("Vanessa Fernández")
print("T03077100")

inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

while True:
    print()
    print("<3<3<3 INVENTARIO <3<3<3")
    for i in range(len(inventario)):
        print(i + 1, ".", inventario[i])
        
    numero = int(input("Número del producto a eliminar (0 para terminar): "))
    
    if numero == 0:
        break
    elif numero < 0:
        print("Ese número no existe")
    elif numero > len(inventario):
        print("Ese número no existe")
    else:
        elegido = inventario[numero - 1]
        confirmar = input("¿Seguro que quieres eliminar " + elegido + "? (s/n): ")
        
        if confirmar == "s":
            inventario.pop(numero - 1)
            print("", elegido, "fue eliminado")
        else:
            print("Baja cancelada")
            
    if len(inventario) == 0:
        print("El inventario quedó vacío")
        break

print()
print("Quedaron", len(inventario), "productos en el inventario")