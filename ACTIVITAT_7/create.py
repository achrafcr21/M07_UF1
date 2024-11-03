from connection import db_connection

def create_portatil(portatil_id, marca, model, color, memoria, pes):
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # query per insertar les dades
            sql = '''INSERT INTO portatils (portatil_id, marca_portatil, model_portatil, color_portatil, memoria_portatil, pes_portatil)
                     VALUES (%s, %s, %s, %s, %s, %s)'''
            values = (portatil_id, marca, model, color, memoria, pes)
            
            cursor.execute(sql, values)
            conn.commit()
            print("Registro creat correctament.")
        
        except Exception as error:
            print("Error al crear el registro:", error)
        
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            conn.close()