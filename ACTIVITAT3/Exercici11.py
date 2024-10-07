#Crear el diccionari de divises amb els seus símbols
divises = {
    "Euro": "€",
    "Dòlar americà": "$",
    "Lliura esterlina": "£",
    "Ien japonès": "¥",
    "Franc suís": "CHF",
    "Dòlar canadenc": "CAD"
}

#Demanar a l'usuari que introdueixi una divisa
divisa_solicitada = input("Introdueix el nom de la divisa: ")

#Buscar la divisa en el diccionari i mostrar el resultat
if divisa_solicitada in divises:
    print(f"El símbol de {divisa_solicitada} és {divises[divisa_solicitada]}.")
else:
    print("Divisa no disponible en el diccionari.")