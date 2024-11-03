from create import create_portatil
from read import mostrar_portatils  # Assegura't que aquesta funció llegeixi correctament des de la taula portatils
from update import update_portatil
from delete import delete_portatil

def main_menu():
    print("Gestió de Portàtils - CRUD")
    print("1. Crear un nou portàtil")
    print("2. Llegir tots els portàtils")
    print("3. Actualitzar un portàtil")
    print("4. Eliminar un portàtil")
    print("5. Sortir")
    
    # Selecció de l'opció (sense verificació)
    opcio = int(input("Tria una opció (1-5): "))
    return opcio

def main():
    while True:
        opcio = main_menu()
        
        if opcio == 1:
            print("\n--- Crear un nou portàtil ---")
            portatil_id = int(input("ID del portàtil: "))
            marca = input("Marca del portàtil: ")
            model = input("Model del portàtil: ")
            color = input("Color del portàtil: ")
            memoria = int(input("Memòria del portàtil (GB): "))
            pes = int(input("Pes del portàtil (g): "))
            create_portatil(portatil_id, marca, model, color, memoria, pes)
        
        elif opcio == 2:
            print("\n--- Llegir tots els portàtils ---")
            mostrar_portatils()  # Cridem a la funció que hem creat abans en l'arxiu read
        
        elif opcio == 3:
            print("\n--- Actualitzar un portàtil ---")
            portatil_id = int(input("ID del portàtil que vols actualitzar: "))
            marca = input("Nova marca (deixa en blanc per no canviar): ") or None
            model = input("Nou model (deixa en blanc per no canviar): ") or None
            color = input("Nou color (deixa en blanc per no canviar): ") or None
            memoria = input("Nova memòria (GB) (deixa en blanc per no canviar): ")
            memoria = int(memoria) if memoria else None
            pes = input("Nou pes (g) (deixa en blanc per no canviar): ")
            pes = int(pes) if pes else None
            update_portatil(portatil_id, marca, model, color, memoria, pes)
        
        elif opcio == 4:
            print("\n--- Eliminar un portàtil ---")
            delete_portatil()
        
        elif opcio == 5:
            print("Sortint del programa.")
            break
        
        else:
            print("Opció no vàlida. Intenta novament.")
        



if __name__ == "__main__":
    main()