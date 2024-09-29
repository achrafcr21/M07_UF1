# Demanar a l'usuari que introdueixi un número
numero = int(input("Introdueix un número: "))

# Mostrar la taula de multiplicar per aquest número
print(f"Taula de multiplicar del {numero}:")
for i in range(1, 11):  # De l'1 al 10
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")