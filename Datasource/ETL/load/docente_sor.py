import pandas as pd

from ETL.transform.transformations import join_2_strings, obt_gender
from util.sql import merge
from datetime import datetime


def cargarDocente(stg_connect,sor_connect):
    docenteDict = {
        "id": [],
        "nombrecompleto": [],
        "cedula": [],
        "genero": [],
        "telefono": [],
        "antiguedad": [],
        "codigoetl": []
    }

    docente_tra_tabla = pd.read_sql(
        f"SELECT Id,NombreCompleto,Cedula,Genero,Telefono, Antiguedad, CodigoEtl FROM docente_tra ", stg_connect)

    if not docente_tra_tabla.empty:
        for id,nombrecompleto,cedula,genero,telefono,antiguedad, codigoetl in zip(
                docente_tra_tabla["Id"],
                docente_tra_tabla["NombreCompleto"],
                docente_tra_tabla["Cedula"],
                docente_tra_tabla["Genero"],
                docente_tra_tabla["Telefono"],
                docente_tra_tabla["Antiguedad"],
                docente_tra_tabla["CodigoEtl"],

        ):
            docenteDict["id"].append(id)
            docenteDict["nombrecompleto"].append(nombrecompleto)
            docenteDict["cedula"].append(cedula)
            docenteDict["genero"].append(genero)
            docenteDict["telefono"].append(telefono)
            docenteDict["antiguedad"].append(antiguedad)
            docenteDict["codigoetl"].append(codigoetl)

    if docenteDict["id"]:
        docenteDF_tra = pd.DataFrame(docenteDict)
        merge(table_name='docente_sor', natural_key_cols=['id'], dataframe=docenteDF_tra, db_context=sor_connect);
    stg_connect.dispose()
    stg_connect.dispose()