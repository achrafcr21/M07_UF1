# Definir la llista
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# 1. Imprimir el segon element
print("El segon element és:", areas_pis[1])

# 2. Imprimir l'últim element
print("L'últim element és:", areas_pis[-1])

# 3. Imprimir l'àrea de la terrassa
index_terrassa = areas_pis.index("Terrassa") + 1
print("L'àrea de la Terrassa és:", areas_pis[index_terrassa])

# 4. Imprimir del primer al tercer element
print("Del primer al tercer element:", areas_pis[0:4])

# 5. Imprimir del tercer element a l'últim
print("Del tercer element a l'últim:", areas_pis[2:])

# 6. Total de l'àrea de les dues habitacions
index_hab1 = areas_pis.index("Habitació1") + 1
index_hab2 = areas_pis.index("Habitació2") + 1
total_habitacions = areas_pis[index_hab1] + areas_pis[index_hab2]
print("Total de l'àrea de les dues habitacions:", total_habitacions)

# 7. Modificar l'àrea del lavabo
index_lavabo = areas_pis.index("Lavabo") + 1
areas_pis[index_lavabo] = 8.50
print("Nova llista amb l'àrea del lavabo modificada:", areas_pis)

# 8. Afegir l'àrea de pati interior
areas_pis.extend(["Pati interior", 2.78])
print("Llista amb pati interior afegit:", areas_pis)

# 9. Total de l'àrea del pis
total_area = sum(area for area in areas_pis if isinstance(area, (int, float)))
print("Total de l'àrea del pis:", total_area)