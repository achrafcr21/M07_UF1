import random

def joc_endevinar_numero():
    # Generar un número aleatori entre 1 i 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    encertat = False

    print("He pensat en un número entre l'1 i el 100. Intenta endevinar-lo!")

    while not encertat:
        # Demanar a l'usuari que entri un número
        entrada = input("Introdueix un número: ")
        try:
            suposicio = int(entrada)
            intentos += 1

            if suposicio < numero_secreto:
                print("El número és més gran. Torna-ho a intentar.")
            elif suposicio > numero_secreto:
                print("El número és més petit. Torna-ho a intentar.")
            else:
                print(f"Has encertat! El número era {numero_secreto}.")
                print(f"Has necessitat {intentos} intents.")
                encertat = True
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")

# Cridar la funció per començar el joc
joc_endevinar_numero()