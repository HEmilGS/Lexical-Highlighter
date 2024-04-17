import re

def isComment(linea):
    coincidencias = re.findall(r'//.*$', linea)
    return coincidencias

linea = "ejemplo //línea con comentarios"
coincidencias = isComment(linea)
for coincidencia in coincidencias:
    print(coincidencia)


