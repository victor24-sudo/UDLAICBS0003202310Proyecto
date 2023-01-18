from faker import Faker
import random
fake = Faker()

def obtenerGenero():
    genero= random.randint(0, 1)
    if genero == 0:
        return "M"
    else:
        return "F"

def obtenerNombre(genero:str):
    if genero == "M":
        return fake.first_name_male()
    else:
        return fake.first_name_female()

def obtenerApellido():
    return fake.last_name()


def obtenerTelefono():
    telefono = fake.ean(length=8,prefixes=('09', ))
    for i  in [1,2]:
        telefono = telefono+str(random.randint(0,9))
    return telefono;

def obtenerCedula():
    cedula = fake.ean(length=8,prefixes=('01','02','03','04','05','06','07',"08","09","10",'11','12','13','14','15','16','17',"18","19","20",'21','22','23','24','30' ))
    for i  in [1,2]:
        cedula = cedula+str(random.randint(0,9))
    return cedula;

def obtenerNumCarrera():
    num = random.randint(1, 36)
    return num

def obtenerNumDocente():
    doc = random.randint(1, 30)
    return doc

def obtenerNumPry():
    pry = random.randint(1, 14)
    return pry

def obtenerPeriodo():
    per = random.randint(2020, 2025)
    return per

def obtenerTrim1():
    tr1 = random.randint(0, 1)
    return tr1

def obtenerTrim2():
    tr2 = random.randint(0, 1)
    return tr2

def obtenerTrim3():
    tr3 = random.randint(0, 1)
    return tr3

def obtenerTrim4():
    tr4 = random.randint(0, 1)
    return tr4






