#Versió 1: Usant Dues Llistes
# Llista d'assignatures
assignatures = ["Matemàtiques", "Física", "Química", "Història", "Llengua", "Anglès"]

# Llista buida per emmagatzemar les notes
notes = []

# Demanar a l'usuari que introdueixi les notes per cada assignatura
for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    notes.append(nota)

# Mostrar les notes amb el nom de l'assignatura
for assignatura, nota in zip(assignatures, notes):
    print(f"A {assignatura} ha tret {nota}.")


#Versió 2: Usant un Diccionari
    
# Diccionari buit per les assignatures i les notes
resultats = {}

# Llista d'assignatures
assignatures = ["Matemàtiques", "Física", "Química", "Història", "Llengua", "Anglès"]

# Demanar a l'usuari que introdueixi les notes per cada assignatura
for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    resultats[assignatura] = nota

# Mostrar les notes amb el nom de l'assignatura
for assignatura, nota in resultats.items():
    print(f"A {assignatura} ha tret {nota}.")