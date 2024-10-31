from connection import db_connection

def update_portatil(portatil_id, marca=None, model=None, color=None, memoria=None, pes=None):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Consultas de actualización para cada campo
            if marca:
                cursor.execute("UPDATE portatils SET marca_portatil = %s WHERE portatil_id = %s", (marca, portatil_id))
            if model:
                cursor.execute("UPDATE portatils SET model_portatil = %s WHERE portatil_id = %s", (model, portatil_id))
            if color:
                cursor.execute("UPDATE portatils SET color_portatil = %s WHERE portatil_id = %s", (color, portatil_id))
            if memoria:
                cursor.execute("UPDATE portatils SET memoria_portatil = %s WHERE portatil_id = %s", (memoria, portatil_id))
            if pes:
                cursor.execute("UPDATE portatils SET pes_portatil = %s WHERE portatil_id = %s", (pes, portatil_id))
            
            conn.commit()
            print("Registre actualitzat correctament.")
        
        except Exception as error:
            print("Error al actualitzar registre:", error)
        
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()