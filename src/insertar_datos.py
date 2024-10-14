""" 
Esta función es utilizada en el resto del código 
    para insertar datos a HUESPED

    Por ejemplo, importando en otro programa
        de la siguiente manera:
    
    import pyodbc
    from crear_conexion_bd import crear_conexion_bd
    from insertar_datos import insertar_huesped

"""
import pyodbc

def insertar_huesped(connection, DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, MAIL, 
                     DOMICILIO, CONDICION_IVA, TIPO_DE_CLIENTE, FNAC, OBSERVACIONES):
    cursor = connection.cursor()
    query = """
    INSERT INTO HUESPED (DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, MAIL, 
                        DOMICILIO, CONDICION_IVA, TIPO_DE_CLIENTE, FNAC, OBSERVACIONES)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        print(f"Ejecutando query: {query}")
        print(f"Con valores: {(DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, MAIL, DOMICILIO, CONDICION_IVA, TIPO_DE_CLIENTE, FNAC, OBSERVACIONES)}")
        
        cursor.execute(query, (DNI, CUIL, NOMBRE, APELLIDO, TELEFONO, MAIL, 
                               DOMICILIO, CONDICION_IVA, TIPO_DE_CLIENTE, FNAC, OBSERVACIONES))
        connection.commit()
        print("Inserción exitosa")
    except pyodbc.Error as e:
        print(f"Error al insertar datos: {str(e)}")
        raise
    finally:
        cursor.close()