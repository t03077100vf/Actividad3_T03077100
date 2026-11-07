print("Ejercicio 13: Mis juegos favoritos")
print("Vanessa Fernández")
print("T03077100")
print()

juegos = ["Minecraft", "Roblox", "Fortnite", "FIFA", "Among Us"]

print("Mi juego número 1:", juegos[0])

print("El último de mi lista:", juegos[-1])

print("El tercero:", juegos[2])

print("Tengo", len(juegos), "juegos favoritos")

print()
print("<3<3<3 MIS FAVORITOS <3<3<3")
for i in range(len(juegos)):
    print(i + 1, ".", juegos[i])

numero = int(input("Escribe un número del 1 al 5: "))

print("Elegiste:", juegos[numero - 1])