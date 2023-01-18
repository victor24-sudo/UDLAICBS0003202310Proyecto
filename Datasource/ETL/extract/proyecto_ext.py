import pandas as pd


def extraerProyecto(stg_connect,source_connect):
    # definicion del diccionario
    proyectoDict = {
        "idProyecto": [],
        "titulo": [],
    }

    # Reading the ext table
    proyecto_ext_tabla = pd.read_sql(
        f"SELECT IdProyecto,Titulo FROM proyecto" , source_connect)

    if not proyecto_ext_tabla.empty:
        for idproyecto, titulo in zip(
                proyecto_ext_tabla["IdProyecto"],
                proyecto_ext_tabla["Titulo"]
        ):
            proyectoDict["idProyecto"].append(idproyecto )
            proyectoDict["titulo"].append(titulo)

    if proyectoDict["idProyecto"]:
        stg_connect.execute('TRUNCATE TABLE proyecto_ext')
        proyectoDF_ext = pd.DataFrame(proyectoDict)
        proyectoDF_ext.to_sql('proyecto_ext', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()
    stg_connect.dispose()