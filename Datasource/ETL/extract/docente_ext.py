import pandas as pd


def extraerDocente(stg_connect,source_connect):
    # definicion del diccionario
    docenteDict = {
        "idDocente": [],
        "nombre": [],
        "apellido": [],
        "cedula": [],
        "genero": [],
        "telefono": [],
        "antiguedad": []
    }

    # Reading the ext table
    docente_ext_tabla = pd.read_sql(
        f"SELECT IdDocente,Nombre,Apellido,Cedula,Genero,Telefono,Antiguedad FROM docente" , source_connect)

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
            docenteDict["idDocente"].append(iddocente )
            docenteDict["nombre"].append(nombre)
            docenteDict["apellido"].append(apellido)
            docenteDict["cedula"].append(cedula)
            docenteDict["genero"].append(genero)
            docenteDict["telefono"].append(telefono)
            docenteDict["antiguedad"].append(antiguedad)

    if docenteDict["idDocente"]:
        stg_connect.execute('TRUNCATE TABLE docente_ext')
        docenteDF_ext = pd.DataFrame(docenteDict)
        docenteDF_ext.to_sql('docente_ext', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()
    stg_connect.dispose()