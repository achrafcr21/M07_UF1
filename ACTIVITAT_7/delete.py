from connection import db_connection

def delete_portatil():
    # demanar al usuari el id 
    portatil_id = int(input("Introdueix el id del portatil que vols eliminar: "))

    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Consulta para eliminar el registro con el ID proporcionado
            sql = "DELETE FROM portatils WHERE portatil_id = %s"
            cursor.execute(sql, (portatil_id,))
            conn.commit()
            
            print("Registre eliminat.")
        
        except Exception as error:
            print("Error al eliminar el registre:", error)
        
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()
