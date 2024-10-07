import string

#  Crear llista amb l'abecedari
abecedari = list(string.ascii_lowercase)

# Eliminar lletres en posicions múltiples de 3 
abecedari = [lletra for i, lletra in enumerate(abecedari) if (i + 1) % 3 != 0]

# Convertir la llista en una tupla
tupla_abecedari = tuple(abecedari)

# Mostrar la llista i la tupla
print("Llista:", abecedari)
print("Tupla:", tupla_abecedari)