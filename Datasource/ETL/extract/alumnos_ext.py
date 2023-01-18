import pandas as pd

def extraerAlumnos(stg_connect,source_connect):
    alumnos_dict = {
        "idalumno": [],
        "nombre": [],
        "apellido": [],
        "genero": [],
        "cedula": [],
        "idcarrera": [],
    }

    # Reading the csv file
    alumnos_csv = pd.read_csv("csv/alumnos.csv")

    if not alumnos_csv.empty:
        for idalumno,nombre,apellido,genero,cedula,idcarrera in zip(
            alumnos_csv["IdAlumno"],
            alumnos_csv["Nombre"],
            alumnos_csv["Apellido"],
            alumnos_csv["Genero"],
            alumnos_csv["Cedula"],
            alumnos_csv["IdCarrera"]
        ):
            alumnos_dict["idalumno"].append(idalumno)
            alumnos_dict["nombre"].append(nombre)
            alumnos_dict["apellido"].append(apellido)
            alumnos_dict["genero"].append(genero)
            alumnos_dict["cedula"].append(cedula)
            alumnos_dict["idcarrera"].append(idcarrera)

    if alumnos_dict["idalumno"]:
        stg_connect.execute('TRUNCATE TABLE alumnos_ext')
        alumnosDF_ext = pd.DataFrame(alumnos_dict)
        alumnosDF_ext.to_sql('alumnos_ext', stg_connect, if_exists='append', index=False)
    stg_connect.dispose()
    source_connect.dispose()