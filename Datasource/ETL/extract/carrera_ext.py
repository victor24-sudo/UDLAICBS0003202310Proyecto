import pandas as pd


def extraerCarrera(stg_connect,source_connect):
    # definicion del diccionario
    carreraDict = {
        "idcarrera": [],
        "nombre": [],
        "numsemestres": []
    }

    # Reading the ext table
    carrera_ext_tabla = pd.read_sql(
        f"SELECT IdCarrera, Nombre, NumSemestres from carrera" , source_connect)

    if not carrera_ext_tabla.empty:
        for idcarrera,nombre,numsemestres in zip(
                carrera_ext_tabla["IdCarrera"],
                carrera_ext_tabla["Nombre"],
                carrera_ext_tabla["NumSemestres"]
        ):
            carreraDict["idcarrera"].append(idcarrera )
            carreraDict["nombre"].append(nombre)
            carreraDict["numsemestres"].append(numsemestres)

    if carreraDict["idcarrera"]:
        stg_connect.execute('TRUNCATE TABLE carrera_ext')
        docenteDF_ext = pd.DataFrame(carreraDict)
        docenteDF_ext.to_sql('carrera_ext', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()
    stg_connect.dispose()