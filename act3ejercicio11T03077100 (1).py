print("Ejercicio 11: Buscador de la tienda de sneakers")
print("Vanessa Fernández")
print("T03077100")
print()

inventario = ["Air Max", "Jordan 1", "Converse", "Samba", "New Balance 550"]

busquedas = 0
encontrados = 0

while True:
    print()
    buscado = input("¿Qué modelo buscas? (escribe salir para terminar): ")
    
    if buscado == "salir":
        break
        
    busquedas = busquedas + 1
    
    for modelo in inventario:
        if modelo == buscado:
            print("¡Sí tenemos", modelo, "!")
            encontrados = encontrados + 1
            break
    else:
        print("No tenemos", buscado)
        print("Te recomendamos estos modelos:")
        for modelo in inventario:
            print("  •", modelo)

print()
print("<3<3<3 RESUMEN <3<3<3")
print("Búsquedas:", busquedas)
print("Encontrados:", encontrados)
print("👋 ¡Gracias por visitar la tienda!")