from connection import db_connection

conn = db_connection()
def create_table():
    if conn:
        try:
            cursor = conn.cursor()
            
            # Crear la tabla
            sql = '''CREATE TABLE portatils(
                    portatil_id int PRIMARY KEY,
                    marca_portatil VARCHAR(255) NOT NULL,
                    model_portatil VARCHAR(255) NOT NULL,
                    color_portatil VARCHAR(255) NOT NULL,
                    memoria_portatil INT NOT NULL,
                    pes_portatil int NOT NULL
            )'''
            cursor.execute(sql)
            conn.commit()
            print("Taula creada amb exit.")
        except Exception as e:
            print("Error, No s'ha pogut crear la taula:", e)
        finally:

            cursor.close()
    
            conn.close()