#Entrada per a les paraules
entradaParaules = input("Introduiex entre 1 i 3 paraules: ")

#Per separar la cadena que ens indica el usuari, es separaràn per espai en blanc
paraules = entradaParaules.split()
#verificar la quantitat de paraules insertades
if len(paraules)>=1 and len(paraules) <= 3:
    for paraula in paraules:
        #logitud de la paraula 
        longitud = len(paraula)
        primer_caracter = paraula[0]
        ultim_caracter = paraula[-1]
        print("Paraula indicada: ", paraula)
        print("Longitud de paraula: ", longitud)
        print("Primer caracter: ", primer_caracter)
        print("Ultim caracter: ", ultim_caracter)
else:
    print("La quantitat de paraules insertades fora de rango!")

