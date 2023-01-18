import pandas as pd


def extraerPOA(stg_connect,source_connect):
    # definicion del diccionario
    poaDict = {
        "idpoa": [],
        "idcarrera": [],
        "iddocente": [],
        "idproyecto": [],
        "periodo": [],
        "trimestre1": [],
        "trimestre2": [],
        "trimestre3": [],
        "trimestre4": [],
    }

    # Reading the ext table
    poa_ext_tabla = pd.read_sql(
        f"SELECT IdPoa, IdCarrera, IdDocente, IdProyecto, Periodo, Trimestre1, Trimestre2, Trimestre3, Trimestre4 FROM poa" , source_connect)

    if not poa_ext_tabla.empty:
        for idpoa,idcarrera,iddocente,idproyecto,periodo,trimestre1,trimestre2,trimestre3,trimestre4 in zip(
                poa_ext_tabla["IdPoa"],
                poa_ext_tabla["IdCarrera"],
                poa_ext_tabla["IdDocente"],
                poa_ext_tabla["IdProyecto"],
                poa_ext_tabla["Periodo"],
                poa_ext_tabla["Trimestre1"],
                poa_ext_tabla["Trimestre2"],
                poa_ext_tabla["Trimestre3"],
                poa_ext_tabla["Trimestre4"]
        ):
            poaDict["idpoa"].append(idpoa)
            poaDict["idcarrera"].append(idcarrera)
            poaDict["iddocente"].append(iddocente)
            poaDict["idproyecto"].append(idproyecto)
            poaDict["periodo"].append(periodo)
            poaDict["trimestre1"].append(trimestre1)
            poaDict["trimestre2"].append(trimestre2)
            poaDict["trimestre3"].append(trimestre3)
            poaDict["trimestre4"].append(trimestre4)

    if poaDict["idpoa"]:
        stg_connect.execute('TRUNCATE TABLE poa_ext')
        poaDF_ext = pd.DataFrame(poaDict)
        poaDF_ext.to_sql('poa_ext', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()
    stg_connect.dispose()