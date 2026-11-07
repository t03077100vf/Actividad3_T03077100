print("Ejercicio 2: Menú de la Cafetería Cute")
print("Vanessa Fernández")
print("T03077100")

while True:
    print()
    print("<3<3<3 ☕ CAFETERÍA CUTE <3<3<3")
    print("1. Ver bebidas")
    print("2. Ver postres")
    print("3. Ver horario")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("🥤 Frappé de cajeta ..... $65")
        print("🍵 Matcha latte ......... $70")
        print("🍓 Smoothie de fresa .... $55")
    elif opcion == "2":
        print("🍪 Galleta red velvet .... $35")
        print("🧁 Cupcake de Oreo ....... $40")
        print("🍩 Dona glaseada ......... $30")
    elif opcion == "3":
        print("🕒 Lunes a viernes: 7:00 a 20:00")
        print("🕒 Sábados: 9:00 a 14:00")
    elif opcion == "4":
        print("👋 ¡Gracias por visitarnos!")
        break
    else:
        print("❌ Opción no válida, elige del 1 al 4")