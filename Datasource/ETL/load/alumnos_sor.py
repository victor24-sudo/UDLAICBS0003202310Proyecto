import pandas as pd

from util.sql import merge



def cargarAlumnos(stg_connect,sor_connect):
    alumnos_dict = {
        "id": [],
        "nombrecompleto": [],
        "genero": [],
        "cedula": [],
        "codigoetl": []
    }

    alumnos_tra_tabla = pd.read_sql(
        f"SELECT Id, NombreCompleto, Genero, Cedula, CodigoEtl from alumnos_tra ", stg_connect)

    if not alumnos_tra_tabla.empty:
        for id,nombrecompleto,genero,cedula, codigoetl in zip(
                alumnos_tra_tabla["Id"],
                alumnos_tra_tabla["NombreCompleto"],
                alumnos_tra_tabla["Genero"],
                alumnos_tra_tabla["Cedula"],
                alumnos_tra_tabla["CodigoEtl"],
        ):
            alumnos_dict["id"].append(id)
            alumnos_dict["nombrecompleto"].append(nombrecompleto)
            alumnos_dict["genero"].append(genero)
            alumnos_dict["cedula"].append(cedula)
            alumnos_dict["codigoetl"].append(codigoetl)

    if alumnos_dict["id"]:
        alumnosDF_tra = pd.DataFrame(alumnos_dict)
        merge(table_name='alumnos_sor', natural_key_cols=['id'], dataframe=alumnosDF_tra, db_context=sor_connect);
    stg_connect.dispose()
    stg_connect.dispose()