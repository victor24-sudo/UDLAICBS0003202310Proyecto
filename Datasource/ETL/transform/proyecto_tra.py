import pandas as pd


def trasProyecto(stg_connect,codigo):
    # definicion del diccionario
    proyectoDict = {
        "id": [],
        "titulo": [],
        "codigoetl": [],
    }

    # Reading the ext table
    proyecto_ext_tabla = pd.read_sql(
        f"SELECT IdProyecto,Titulo FROM proyecto_ext" , stg_connect)

    if not proyecto_ext_tabla.empty:
        for idproyecto, titulo in zip(
                proyecto_ext_tabla["IdProyecto"],
                proyecto_ext_tabla["Titulo"]

        ):
            proyectoDict["id"].append(idproyecto)
            proyectoDict["titulo"].append(titulo)
            proyectoDict["codigoetl"].append(codigo)

    if proyectoDict["id"]:
        proyectoDF_ext = pd.DataFrame(proyectoDict)
        proyectoDF_ext.to_sql('proyecto_tra', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()