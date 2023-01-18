import pandas as pd

from util.sql import merge
from datetime import datetime


def cargarProyecto(stg_connect,sor_connect):
    proyectoDict = {
        "id": [],
        "titulo": [],
        "codigoetl": [],
    }

    proyecto_tra_tabla = pd.read_sql(
        f"SELECT Id,Titulo,CodigoEtl FROM proyecto_tra ", stg_connect)

    if not proyecto_tra_tabla.empty:
        for id,titulo, codigoetl in zip(
                proyecto_tra_tabla["Id"],
                proyecto_tra_tabla["Titulo"],
                proyecto_tra_tabla["CodigoEtl"],

        ):
            proyectoDict["id"].append(id)
            proyectoDict["titulo"].append(titulo)
            proyectoDict["codigoetl"].append(codigoetl)


    if proyectoDict["id"]:
        proyectoDF_tra = pd.DataFrame(proyectoDict)
        merge(table_name='proyecto_sor', natural_key_cols=['id'], dataframe=proyectoDF_tra, db_context=sor_connect);
    stg_connect.dispose()
    stg_connect.dispose()