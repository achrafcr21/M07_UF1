# Demanar a l'usuari que introdueixi un valor en euros
valor_base = float(input("Introdueix un valor en €: "))

# Utilitzar un array per definir els valors valids de Iva
iva_valids = [4, 10, 21]


iva = None

# l'IVA introduït és vàlid
while iva not in iva_valids:
    iva = int(input("Introdueix l'IVA a aplicar-hi (4, 10 o 21%): "))
    if iva not in iva_valids:
        print("IVA no vàlid. introdueix un dels percentatges vàlids: 4%, 10% o 21%.")

# valor final amb l'IVA afegit
valor_final = valor_base * (1 + iva / 100)

print(f"Valor base: {valor_base}€")
print(f"Percentatge d'IVA aplicat: {iva}%")
print(f"Valor final amb IVA: {valor_final}€")