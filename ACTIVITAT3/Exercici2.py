# Crear una tupla amb els mesos de l'any
mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", 
         "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

# Bucle per sol·licitar números fins que l'usuari introdueixi 0
while True:
    numero = int(input("Introdueix un número entre 0 i 12: "))
    
    if numero == 0:
        print("Programa finalitzat.")
        break
    elif 1 <= numero <= 12:
        #Aqui he utilitzat [numero-1] pero acceder al index ja que comença desdel 0. 
        print(f"El mes corresponent és {mesos[numero-1]}")
    else:
        print("Número fora de rang, intenta de nou.")