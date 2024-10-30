from connection import db_connection


query =  '''create table portatils(
                portatil_id int PRIMARY KEY,
                marca_portatil VARCHAR(255) NOT NULL,
                model_portatil VARCHAR(255) NOT NULL,
                color_portatil VARCHAR(255) NOT NULL,
                memoria_portatil INT NOT NULL,
                pes_portatil int NOT NULL

)'''

print(query)

db_connection.execute(query)