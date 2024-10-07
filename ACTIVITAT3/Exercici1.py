#Demanar a l'usuari un valor 
entrada = int(input("Introduiex un numero entre 10 i 100: "))
while entrada < 10 or entrada > 100:
    entrada = int(input("Por favor, introduce un número entre 10 y 100: "))

# Crear una tupla
tupla_numeros = tuple(range(1, entrada + 1))
print("Tupla de números:", tupla_numeros)