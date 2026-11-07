print("Ejercicio 1: Inicia sesión en Roblox")
print("Vanessa Fernández")
print("T03077100")
print()

usuario_correcto = "gamer17"
contrasena_correcta = "roblox123"

sesion_iniciada = False

while sesion_iniciada == False:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    if usuario == usuario_correcto:
        if contrasena == contrasena_correcta:
            print("¡Bienvenido,", usuario, "!")
            sesion_iniciada = True
        else:
            print("La contraseña es incorrecta")
    else:
        print("Ese usuario no existe")

print("Cargando tus juegos...")