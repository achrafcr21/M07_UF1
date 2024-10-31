from connection import db_connection

def mostrar_portatils():
    conn = db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            #query per obtenir tots els registres de la taula portatils
            cursor.execute("SELECT * FROM portatil")
            
            # utilitzem fetchall per obtenir tots els resultats de la consulta
            rows = cursor.fetchall()
            
            # Mostrar cada registro en la pantalla
            print("Registros en la tabla portatils:")
            for row in rows:
                print(row)
        
        except Exception as error:
            print("Error al llegir els registres:", error)
        
        finally:
            #tancar el cursor y la conexión
            cursor.close()
            conn.close()

# Llamar a la función para leer y mostrar los registros
mostrar_portatils()