entrada = input("Introdueix números del 1 al 10 separats per un espai: ")
#Aquesta linea fa varies coses, divideix la cadena de entrada en una lista de cadenas, despres convirteix les cadnes a enters i crea la lista de enters
numeros_lista = [int(num) for num in entrada.split()]

mi_tupla = tuple(sorted(numeros_lista))

print(mi_tupla)