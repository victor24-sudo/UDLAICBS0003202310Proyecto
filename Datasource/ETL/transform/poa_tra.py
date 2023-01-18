import pandas as pd


def trasPOA(stg_connect,codigo):
    # definicion del diccionario
    poaDict = {
        "id": [],
        "idcarrera": [],
        "iddocente": [],
        "idproyecto": [],
        "periodo": [],
        "trimestre1": [],
        "trimestre2": [],
        "trimestre3": [],
        "trimestre4": [],
        "codigoetl": [],
    }

    # Reading the ext table
    poa_ext_tabla = pd.read_sql(
        f"SELECT IdPOA, IdCarrera, IdDocente, IdProyecto, Periodo, Trimestre1, Trimestre2, Trimestre3, Trimestre4 FROM poa_ext" , stg_connect)

    if not poa_ext_tabla.empty:
        for idpoa,idcarrera,iddocente,idproyecto,periodo,trimestre1,trimestre2,trimestre3,trimestre4 in zip(
                poa_ext_tabla["IdPOA"],
                poa_ext_tabla["IdCarrera"],
                poa_ext_tabla["IdDocente"],
                poa_ext_tabla["IdProyecto"],
                poa_ext_tabla["Periodo"],
                poa_ext_tabla["Trimestre1"],
                poa_ext_tabla["Trimestre2"],
                poa_ext_tabla["Trimestre3"],
                poa_ext_tabla["Trimestre4"]
        ):
            poaDict["id"].append(idpoa)
            poaDict["idcarrera"].append(idcarrera)
            poaDict["iddocente"].append(iddocente)
            poaDict["idproyecto"].append(idproyecto)
            poaDict["periodo"].append(periodo)
            poaDict["trimestre1"].append(trimestre1)
            poaDict["trimestre2"].append(trimestre2)
            poaDict["trimestre3"].append(trimestre3)
            poaDict["trimestre4"].append(trimestre4)
            poaDict["codigoetl"].append(codigo)

    if poaDict["id"]:
        poaDF_ext = pd.DataFrame(poaDict)
        poaDF_ext.to_sql('poa_tra', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()