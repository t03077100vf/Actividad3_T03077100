print("Ejercicio 8: Revisa tu gamertag")
print("Vanessa Fernández")
print("T03077100")
print()

gamertag = input("Escribe tu gamertag: ")

vocales = 0
numeros = 0
caracteres = 0

for letra in gamertag:
    print("🔤", letra)
    
    caracteres = caracteres + 1
    
    if letra in "aeiouAEIOU":
        vocales = vocales + 1
        
    if letra in "0123456789":
        numeros = numeros + 1

print("<3<3<3 RESUMEN <3<3<3")
print("Caracteres:", caracteres)
print("Vocales:", vocales)
print("Números:", numeros)

if numeros == 0:
    print("Consejo: agrégale un número para que sea único")
else:
    print("¡Buen gamertag!")