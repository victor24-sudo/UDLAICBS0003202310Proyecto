import random

import pandas as pd
from Faker import *
import openpyxl

NUMERO_DOCENTES=30
NUMERO_POA=60

# # ----------------------------------------------------------Cargar Docentes----------------------------------------------------------
def cargarProfesores(stg_conn):

    
    # definicion del diccionario
    profesoresDict = {
        "nombre": [],
        "apellido": [],
        "cedula": [],
        "genero": [],
        "telefono": [],
        "antiguedad": [],
    }
    # Agregar datos al diccionario
    for i in range(NUMERO_DOCENTES):
        genero = obtenerGenero();
        profesoresDict["nombre"].append(obtenerNombre(genero))
        profesoresDict["apellido"].append(obtenerApellido())
        profesoresDict["cedula"].append(obtenerCedula())
        profesoresDict["genero"].append(genero)
        profesoresDict["telefono"].append(obtenerTelefono())
        profesoresDict["antiguedad"].append(obtenerNumDocente())
    # trasnformar de un diccionario a un df
    stg_conn.execute('SET FOREIGN_KEY_CHECKS = 0')
    stg_conn.execute('TRUNCATE TABLE docente')
    profesoresDF = pd.DataFrame(profesoresDict)
    profesoresDF.to_sql('docente', stg_conn, if_exists='append', index=False)

# # ----------------------------------------------------------Cargar POA----------------------------------------------------------
def cargarPOA(stg_conn):
    # definicion del diccionario

    POADict = {
        "idcarrera": [],
        "iddocente": [],
        "idproyecto": [],
        "periodo": [],
        "trimestre1": [],
        "trimestre2": [],
        "trimestre3": [],
        "trimestre4": []
    }
    # Agregar datos al diccionario
    for i in range(NUMERO_DOCENTES):
        POADict["idcarrera"].append(obtenerNumCarrera())
        POADict["iddocente"].append(obtenerNumDocente())
        POADict["idproyecto"].append(obtenerNumPry())
        POADict["periodo"].append(obtenerPeriodo())
        POADict["trimestre1"].append(obtenerTrim1())
        POADict["trimestre2"].append(obtenerTrim2())
        POADict["trimestre3"].append(obtenerTrim3())
        POADict["trimestre4"].append(obtenerTrim4())
    # trasnformar de un diccionario a un df
    stg_conn.execute('SET FOREIGN_KEY_CHECKS = 0')
    stg_conn.execute('TRUNCATE TABLE poa')
    POADF = pd.DataFrame(POADict)
    POADF.to_sql('poa', stg_conn, if_exists='append', index=False)

##-------------------------------------------------------CARGAR CSV---------------------------------------------

def cargarAlumnos():
    # definicion del diccionario

    AlumnosDict = {
        "Nombre": [],
        "Apellido": [],
        "Genero": [],
        "Cedula": [],
        "IdCarrera": []
    }
    # Agregar datos al diccionario
    for i in range(NUMERO_POA):
        genero = obtenerGenero();
        AlumnosDict["Nombre"].append(obtenerNombre(genero))
        AlumnosDict["Apellido"].append(obtenerApellido())
        AlumnosDict["Genero"].append(genero)
        AlumnosDict["Cedula"].append(obtenerCedula())
        AlumnosDict["IdCarrera"].append(obtenerNumCarrera())
    # trasnformar de un diccionario a un df
    # crear el objeto ExcelWriter
    df = pd.DataFrame(AlumnosDict)
    escrito = pd.ExcelWriter('nuevo-excel.xlsx')
    # escribir el DataFrame en excel
    df.to_excel(escrito)
    # guardar el excel
    escrito.save()
    print('El DataFrame se ha escrito con éxito en el archivo de Excel.')

def cargarDataAleatoria(stg_conn):
    cargarProfesores(stg_conn),
    cargarPOA(stg_conn),
    cargarAlumnos()





