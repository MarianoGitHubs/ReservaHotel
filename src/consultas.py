import pyodbc
from crear_conexion_bd import crear_conexion_bd

cursor = conexion.cursos()
cursor.execute("Select * from HUESPED;")

HUESPED = cursor.fetchone()

while HUESPED:
    print(HUESPED[0])
    HUESPED = cursor.fetchone()
    
    
cursor.close()
conexion.close()