import pandas as pd


def trasCarrera(stg_connect,codigo):
    # definicion del diccionario
    carreraDict = {
        "id": [],
        "nombre": [],
        "numsemestres": [],
        "codigoetl": [],
    }

    # Reading the ext table
    carrera_ext_tabla = pd.read_sql(
        f"SELECT IdCarrera, Nombre, NumSemestres from carrera_ext" , stg_connect)

    if not carrera_ext_tabla.empty:
        for idcarrera,nombre,numsemestres in zip(
                carrera_ext_tabla["IdCarrera"],
                carrera_ext_tabla["Nombre"],
                carrera_ext_tabla["NumSemestres"]
        ):
            carreraDict["id"].append(idcarrera )
            carreraDict["nombre"].append(nombre)
            carreraDict["numsemestres"].append(numsemestres)
            carreraDict["codigoetl"].append(codigo)

    if carreraDict["id"]:
        carreraDF_ext = pd.DataFrame(carreraDict)
        carreraDF_ext.to_sql('carrera_tra', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()