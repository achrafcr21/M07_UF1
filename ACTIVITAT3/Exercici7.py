# Crear un diccionari buit
contactes = {}

while True:
    # Preguntar a l'usuari si vol afegir un contacte
    resposta = input("Vols afegir un contacte? (sí/no): ")
    if resposta.lower() != "sí":
        break

    # Demanar el nom i l'edat
    nom = input("Introdueix el nom del contacte: ")
    if nom in contactes:
        print("Aquest nom ja existeix. No s'ha afegit el contacte.")
    else:
        edat = input("Introdueix l'edat del contacte: ")
        try:
            # Assegurar-se que l'edat és un número enter
            edat = int(edat)
            contactes[nom] = edat
        except ValueError:
            print("No has introduït una edat vàlida. No s'ha afegit el contacte.")

# Mostrar tots els contactes
print("\nLlista de contactes:")
for nom, edat in contactes.items():
    print(f"Nom: {nom}, Edat: {edat}")