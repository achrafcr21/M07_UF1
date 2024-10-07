# Paso 1: Solicitar una frase al usuario y eliminar espacios
frase = input("Introdueix una frase: ")
frase_sense_espais= frase.replace(" ", "")

frase_en_tupla= tuple(frase_sense_espais)

print(f"Frase en tuple sense espais: {frase_en_tupla}")

#frase sense carcters repititius

caracteres_vistos= set()
frase_sense_repititius= ""

for car in frase_en_tupla:
    if car not in caracteres_vistos:
        caracteres_vistos.add(car)
        frase_sense_repititius += car
print("Frase sense caracters repititius: ", frase_sense_repititius)