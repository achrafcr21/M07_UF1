# Pas 1: Demanar a l'usuari que introdueixi 10 números separats per espais
entrada = input("Introdueix 10 números separats per espais: ")

# Pas 2: Convertir l'entrada en una llista de números enters
numeros = [int(num) for num in entrada.split()]

# Pas 3: Calcular la suma dels números
suma_total = sum(numeros)

# Pas 4: Calcular la mitjana dels números
mitjana = suma_total / len(numeros)

# Pas 5: Afegir la suma i la mitjana a la llista
numeros.append(suma_total)
numeros.append(mitjana)

# Pas 6: Mostrar els resultats
print("Números de l’usuari:", numeros[:-2])
print("Suma total:", suma_total)
print("Mitjana:", mitjana)