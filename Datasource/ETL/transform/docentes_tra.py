import pandas as pd

from ETL.transform.transformations import *



def trasDocentes(stg_connect,codigo):
    # definicion del diccionario
    docenteDict = {
        "id": [],
        "nombrecompleto": [],
        "cedula": [],
        "genero": [],
        "telefono": [],
        "antiguedad": [],
        "codigoetl": []
    }

    # Reading the ext table
    docente_ext_tabla = pd.read_sql(
        f"SELECT IdDocente,Nombre,Apellido,Cedula,Genero,Telefono,Antiguedad FROM docente_ext" , stg_connect)

    if not docente_ext_tabla.empty:
        for iddocente,nombre,apellido,cedula,genero,telefono,antiguedad in zip(
                docente_ext_tabla["IdDocente"],
                docente_ext_tabla["Nombre"],
                docente_ext_tabla["Apellido"],
                docente_ext_tabla["Cedula"],
                docente_ext_tabla["Genero"],
                docente_ext_tabla["Telefono"],
                docente_ext_tabla["Antiguedad"],
        ):
            docenteDict["id"].append(iddocente)
            docenteDict["nombrecompleto"].append(join_2_strings(nombre,apellido))
            docenteDict["cedula"].append(cedula)
            docenteDict["genero"].append(obt_gender(genero))
            docenteDict["telefono"].append(telefono)
            docenteDict["antiguedad"].append(antiguedad)
            docenteDict["codigoetl"].append(codigo)

    if docenteDict["id"]:
        docentesDF_ext = pd.DataFrame(docenteDict)
        docentesDF_ext.to_sql('docente_tra', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()