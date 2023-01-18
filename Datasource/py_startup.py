import traceback
import configparser
from seed import *
import pandas
from util import db_connection
parser = configparser.ConfigParser()
from ETL.extract.docente_ext import extraerDocente
from ETL.extract.carrera_ext import extraerCarrera
from ETL.extract.proyecto_ext import extraerProyecto
from ETL.extract.poa_ext import extraerPOA
from ETL.extract.alumnos_ext import extraerAlumnos
from ETL.transform.carreras_tra import trasCarrera
from ETL.transform.proyecto_tra import trasProyecto
from ETL.transform.alumnos_tra import trasAlumnos
from ETL.transform.docentes_tra import trasDocentes
from ETL.transform.poa_tra import trasPOA
from ETL.load.carrera_sor import  cargarCarrera
from ETL.load.proyecto_sor import cargarProyecto
from ETL.load.docente_sor import cargarDocente
from ETL.load.alumnos_sor import cargarAlumnos
from ETL.load.poa_sor import cargarPOA


parser.read(".properties")




try:

    db_sectionName = "DbConnection"
    db_name1 = parser.get(db_sectionName, "Source")
    source_connect = db_connection.connect(db_name1)
    db_name2 = parser.get(db_sectionName, "Stg")
    stg_connect = db_connection.connect(db_name2)
    db_name3 = parser.get(db_sectionName, "Sor")
    sor_connect = db_connection.connect(db_name3)

    def CodigoEtl():
        colummns_dict = {
            "usuario": [],
        }

        colummns_dict["usuario"].append("Victor")

        df_process = pandas.DataFrame(colummns_dict)
        df_process.to_sql('codigo_etl', stg_connect, if_exists='append', index=False)

        table_process = pandas.read_sql('SELECT ID FROM codigo_etl ORDER by ID DESC LIMIT 1', stg_connect)

        id = table_process['ID'][0]

        return id

    try:

        #cargarDataAleatoria(source_connect)


        etl = CodigoEtl()

        ##-----------Extraer-----------------------##

        #extraerDocente(stg_connect, source_connect)

        #extraerCarrera(stg_connect, source_connect)
        #extraerProyecto(stg_connect, source_connect)
        #extraerPOA(stg_connect, source_connect)
        #extraerAlumnos(stg_connect, source_connect)

        print ("Terminé el extrac")

        ##-------------Transformar-----------------##

        #trasCarrera(stg_connect,etl)
        #trasProyecto(stg_connect,etl)
        #trasAlumnos(stg_connect, etl)
        #trasDocentes(stg_connect, etl)
        #trasPOA(stg_connect, etl)

        print("Terminé el Transform")

        ##-------------Cargar-----------------------##

        #cargarProyecto(stg_connect, sor_connect)
        #cargarCarrera(stg_connect,sor_connect)
        #cargarDocente(stg_connect,sor_connect)
        #cargarPOA(stg_connect,sor_connect)

        print("Terminé el Load")

    except:
        traceback.print_exc()

except:
    traceback.print_exc()
finally:
    pass






