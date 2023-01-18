import pandas as pd

from ETL.transform.transformations import *



def trasAlumnos(stg_connect,codigo):
    # definicion del diccionario
    alumnos_dict = {
        "id": [],
        "nombrecompleto": [],
        "genero": [],
        "cedula": [],
        "idcarrera": [],
        "codigoetl": []
    }

    # Reading the ext table
    alumnos_ext_tabla = pd.read_sql(
        f"SELECT IdAlumno, Nombre, Apellido, Genero, Cedula, IdCarrera from alumnos_ext" , stg_connect)

    if not alumnos_ext_tabla.empty:
        for idalumno,nombre,apellido,genero,cedula,idcarrera in zip(
                alumnos_ext_tabla["IdAlumno"],
                alumnos_ext_tabla["Nombre"],
                alumnos_ext_tabla["Apellido"],
                alumnos_ext_tabla["Genero"],
                alumnos_ext_tabla["Cedula"],
                alumnos_ext_tabla["IdCarrera"]
        ):
            alumnos_dict["id"].append(idalumno)
            alumnos_dict["nombrecompleto"].append(join_2_strings(nombre,apellido))
            alumnos_dict["genero"].append(obt_gender(genero))
            alumnos_dict["cedula"].append(cedula)
            alumnos_dict["idcarrera"].append(idcarrera)
            alumnos_dict["codigoetl"].append(codigo)

    if alumnos_dict["id"]:
        alumnosDF_ext = pd.DataFrame(alumnos_dict)
        alumnosDF_ext.to_sql('alumnos_tra', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()