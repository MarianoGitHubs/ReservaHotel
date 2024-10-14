""" 
Esta función es utilizada en el resto del código 
    para establecer la conexión con la base de datos 

    Por ejemplo, importando en otro programa
        de la siguiente manera:
    
    from crear_conexion_bd import crear_conexion_bd
    
"""

import pyodbc

       
def crear_conexion_bd(server='TSSIT01', database='reservahotel', usuario='Soporte', contrasena='Instituto_2023'):
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
        print(f"Detalles del error: {str(e)}")
        return None
