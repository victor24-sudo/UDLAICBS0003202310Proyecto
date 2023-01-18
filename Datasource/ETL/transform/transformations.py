from datetime import datetime

def join_2_strings(string1,string2):
    return f"{string1} {string2}"

def obt_gender(gen):
    if gen == 'M':
        return 'Masculino'
    elif gen == 'F':
        return 'Femenino'
    else:
        return 'NO DEFINIDO'