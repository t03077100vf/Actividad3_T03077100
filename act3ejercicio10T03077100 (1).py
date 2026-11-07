print("Ejercicio 10: Tu playlist en el camión")
print("Vanessa Fernández")
print("T03077100")
print()

playlist = ["Flowers", "Calm Down", "Ella Baila Sola", "Anti-Hero", "Tití Me Preguntó", "Daylight"]

print("<3<3<3 MI PLAYLIST <3<3<3")
numero = 1
for cancion in playlist:
    print(numero, ".", cancion)
    numero = numero + 1

saltar = input("¿Qué canción quieres saltar? ")
parada = input("¿En qué canción llegas a tu parada? ")

escuchadas = 0

for cancion in playlist:
    
    if cancion == saltar:
        print("⏭Saltando", cancion)
        continue
        
    print("Escuchando", cancion)
    escuchadas = escuchadas + 1
    
    if cancion == parada:
        print("¡Llegaste a tu parada!")
        # break: dejamos de escuchar
        break
else:
    print("Escuchaste toda la playlist")

print("Canciones escuchadas:", escuchadas)