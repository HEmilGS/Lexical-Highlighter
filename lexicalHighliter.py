import re

def isComment(linea):
    coincidencias = re.findall(r'#.*$', linea)
    return coincidencias




def isPunctuation(linea):
    patron = r'["\[\]{},:.\]]'
    coincidencias = re.findall(patron, linea)
    return coincidencias


linea = "ejemplo #línea con comentarios"
coincidencias = isComment(linea)
for coincidencia in coincidencias:
    print(coincidencia)



linea = 'Esto es un ejemplo con caracteres especiales: ", [], {}.'
coincidencias = isPunctuation(linea)
print(coincidencias)

