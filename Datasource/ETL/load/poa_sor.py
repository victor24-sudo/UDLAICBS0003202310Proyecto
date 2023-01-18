import pandas as pd

from util.sql import merge



def cargarPOA(stg_connect,sor_connect):
    poa_dict = {
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

    poa_tra_tabla = pd.read_sql(
        f"SELECT Id, IdCarrera, IdDocente, IdProyecto, Periodo, Trimestre1, Trimestre2, Trimestre3, Trimestre4,CodigoEtl FROM poa_tra ", stg_connect)

    if not poa_tra_tabla.empty:
        for id,idcarrera,iddocente,idproyecto, periodo,trimestre1,trimestre2,trimestre3,trimestre4, codigoetl in zip(
                poa_tra_tabla["Id"],
                poa_tra_tabla["IdCarrera"],
                poa_tra_tabla["IdDocente"],
                poa_tra_tabla["IdProyecto"],
                poa_tra_tabla["Periodo"],
                poa_tra_tabla["Trimestre1"],
                poa_tra_tabla["Trimestre2"],
                poa_tra_tabla["Trimestre3"],
                poa_tra_tabla["Trimestre4"],
                poa_tra_tabla["CodigoEtl"],
        ):
            poa_dict["id"].append(id)
            poa_dict["idcarrera"].append(idcarrera)
            poa_dict["iddocente"].append(iddocente)
            poa_dict["idproyecto"].append(idproyecto)
            poa_dict["periodo"].append(periodo)
            poa_dict["trimestre1"].append(trimestre1)
            poa_dict["trimestre2"].append(trimestre2)
            poa_dict["trimestre3"].append(trimestre3)
            poa_dict["trimestre4"].append(trimestre4)
            poa_dict["codigoetl"].append(codigoetl)

    if poa_dict["id"]:
        sor_connect.execute('SET FOREIGN_KEY_CHECKS = 0')
        poaDF_tra = pd.DataFrame(poa_dict)
        merge(table_name='poa_sor', natural_key_cols=['id'], dataframe=poaDF_tra, db_context=sor_connect);
        sor_connect.execute('SET FOREIGN_KEY_CHECKS = 1')
    stg_connect.dispose()
    stg_connect.dispose()