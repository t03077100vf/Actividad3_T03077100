print("Ejercicio 7: Boletos para el concierto")
print("Vanessa Fernández")
print("T03077100")
print()

artista = input("¿De quién es el concierto? ")
cantidad = int(input("¿Cuántos boletos quieres? "))

for boleto in range(1, cantidad + 1):
    asistente = input("Nombre del asistente " + str(boleto) + ": ")
    
    print("Boleto", boleto, "de", cantidad)
    print("", artista, "- Asistente:", asistente)

print("Se generaron", cantidad, "boletos. ¡Disfruten el concierto!")