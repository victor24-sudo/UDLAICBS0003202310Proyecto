import pandas as pd

from util.sql import merge
from datetime import datetime


def cargarCarrera(stg_connect,sor_connect):
    carreraDict = {
        "id": [],
        "nombre": [],
        "numsemestres": [],
        "codigoetl": []
    }

    carrera_tra_tabla = pd.read_sql(
        f"SELECT Id, Nombre, NumSemestres, CodigoEtl from Carrera_tra ", stg_connect)

    if not carrera_tra_tabla.empty:
        for id,nombre,numsemestres, codigoetl in zip(
                carrera_tra_tabla["Id"],
                carrera_tra_tabla["Nombre"],
                carrera_tra_tabla["NumSemestres"],
                carrera_tra_tabla["CodigoEtl"],

        ):
            carreraDict["id"].append(id)
            carreraDict["nombre"].append(nombre)
            carreraDict["numsemestres"].append(numsemestres)
            carreraDict["codigoetl"].append(codigoetl)

    if carreraDict["id"]:
        carreraDF_tra = pd.DataFrame(carreraDict)
        merge(table_name='carrera_sor', natural_key_cols=['id'], dataframe=carreraDF_tra, db_context=sor_connect);
    stg_connect.dispose()
    stg_connect.dispose()
