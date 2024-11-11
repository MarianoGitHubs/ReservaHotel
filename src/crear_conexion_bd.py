""" 
Esta función es utilizada en el resto del código 
    para establecer la conexión con la base de datos 

    Por ejemplo, importando en otro programa
        de la siguiente manera:
    
    from crear_conexion_bd import crear_conexion_bd
    
"""

import pyodbc

# Función para conectar a la base de datos
def conectar_bd(server, database, usuario, contrasena):
    try:
        connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={usuario};'
            f'PWD={contrasena};'
        )
        
        connection = pyodbc.connect(connection_string)
        print('Conexión Exitosa a la base de datos')
        return connection
    except pyodbc.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
