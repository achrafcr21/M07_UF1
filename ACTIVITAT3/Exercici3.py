#Demanar a l'usuari un numero
numero = int(input("Introduiex un numero del 1 al 10: "))
lista_resultats=[]
#Verificar el rang
if 1<= numero <= 10: 
    for i in range(1,11):
        resultat= numero * i
        lista_resultats.append(resultat)
else:
    print("Numero fora del rang")

print(f"Taula de multiplicació del numero {numero}: {lista_resultats}")