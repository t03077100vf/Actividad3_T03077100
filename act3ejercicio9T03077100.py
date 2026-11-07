print("Ejercicio 9: Torneo de videojuegos")
print("Vanessa Fernández")
print("T03077100")
print()

juego = input("¿De qué juego es el torneo? ")
cantidad = int(input("¿Cuántos jugadores hay? "))

total_puntos = 0
finalistas = 0

mejor_nombre = ""
mejor_puntos = -1

for jugador in range(1, cantidad + 1):
    print()
    print(" Jugador", jugador)
    nombre = input("Gamertag: ")
    puntos = int(input("Puntos: "))
    
    total_puntos = total_puntos + puntos
    
    if puntos >= 100:
        print("<3", nombre, "pasa a la final")
        finalistas = finalistas + 1
    else:
        print("<3", nombre, "sigue practicando")
        
    if puntos > mejor_puntos:
        mejor_puntos = puntos
        mejor_nombre = nombre

print()
print("<3<3<3 RESULTADOS DEL TORNEO DE", juego, "<3<3<3")
print("Puntos de todos los jugadores:", total_puntos)
print("Finalistas:", finalistas)
print("🏆 Ganador:", mejor_nombre, "con", mejor_puntos, "puntos")