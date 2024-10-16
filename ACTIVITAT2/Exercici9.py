# 1. Solicitar al usuario que introduzca dos palabras
entrada = input("Introduce dos palabras separadas por espacio: ")

# 2. Dividir la entrada en dos palabras
palabras = entrada.split()

# 3. Verificar la cantidad de las palabras
if len(palabras) == 2:
    palabra1, palabra2 = palabras  
    
    
    #   intercambiar las letras y concatenar con el resto de la palabra
    nueva_palabra1 = palabra2[:2] + palabra1[2:]
    nueva_palabra2 = palabra1[:2] + palabra2[2:]
    
    print(f"{nueva_palabra1} {nueva_palabra2}")
else:
    print("Por favor, introduce exactamente dos palabras.")