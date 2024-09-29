# Demanar a l'usuari que introdueixi un número
numero = int(input("Introdueix un número: "))

# Inicialitzar la suma
suma = 0

# Iterar des de l'1 fins al número introduït
for i in range(1, numero + 1):
    suma += i

# Mostrar el resultat
print(f"La suma de tots els números des de l'1 fins a {numero} és {suma}")