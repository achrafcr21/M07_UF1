numero1 = float(input("Introdueix el primer número: "))
numero2 = float(input("Introdueix el segon número: "))

# Demanar a l'usuari que esculli l'operació matemàtica a realitzar
print("Tria l'operació a realitzar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicació")
print("4. Divisió")
operacio = input("Introdueix 1, 2, 3 o 4 : ")

# Executar l'operació seleccionada i mostrar el resultat
if operacio == '1':
    resultat = numero1 + numero2
    print("El resultat de la suma és:", resultat)
elif operacio == '2':
    resultat = numero1 - numero2
    print("El resultat de la resta és:", resultat)
elif operacio == '3':
    resultat = numero1 * numero2
    print("El resultat de la multiplicació és:", resultat)
elif operacio == '4':
        resultat = numero1 / numero2
        print("El resultat de la divisió és:", resultat)
else:
    print("No has seleccionat una operació vàlida.")