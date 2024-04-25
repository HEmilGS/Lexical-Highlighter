# import re

# def isComment(linea):
#     coincidencias = re.findall(r'#.*$', linea)
#     return coincidencias

# def isPunctuation(linea):
#     patron = r'["\[\]{},:.\]]'
#     coincidencias = re.findall(patron, linea)
#     return coincidencias

# linea = "ejemplo #línea con comentarios"
# coincidencias = isComment(linea)
# for coincidencia in coincidencias:
#     print(coincidencia)

# linea = 'Esto es un ejemplo con caracteres especiales: ", [], {}.'
# coincidencias = isPunctuation(linea)
# print(coincidencias)


import re # Importa el módulo de expresiones regulares

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)

def highlight_items(line):
    puntuactionPattern = r'["\[\](){},:.\]]' #Patron de los operadores
    commentsPattern = r'#.*$'
    
    line = re.sub(commentsPattern,r'__COMMENTS1__\g<0>__COMMENTS2__',line)# Reemplaza los literales con el texto __LITERAL__ al inicio y al final incluyendo el mismo literal


    parts = re.split(r'("[^"]*"|\'[^\']*\')', line)# Separa la línea en partes, si encuentra unas comillas dobles o simples para encontrar los operadores que no estén dentro de las comillas
    for i in range(0, len(parts), 2):# Itera sobre las partes de la línea
        parts[i] = re.sub(puntuactionPattern, r'__PUNTUACTION1__\g<0>__PUNTUACTION2__', parts[i])# Reemplaza los operadores con el texto __OPERATOR__ al inicio y al final incluyendo el mismo operador
    line = ''.join(parts)# Une las partes de la línea con las modificaciones y las partes de las comillas
    line = line.replace('__PUNTUACTION1__', '<span class="puntuaction">').replace('__PUNTUACTION2__', '</span>')#Reemplaza el texto __OPERATOR__ por las etiquetas span de html
    line = line.replace('__COMMENTS1__', '<span class="comments">').replace('__COMMENTS2__', '</span>')#Reemplaza el texto __LITERAL__ por las etiquetas span de html
    
    return line

highlighted_lines = [highlight_items(line) for line in lineas] #Aplica la función highlight_items a cada línea del texto

with open('highlighted.html', 'w') as f:
    f.write('<html>\n  <head>\n      <style>.operator { color: red; } .literals {color: blue;} .puntuaction {color: purple;} .comments {color: green;c}</style>\n  </head>\n\n  <body>\n      <pre>\n        <code>\n')
    f.write('\n'.join(highlighted_lines))
    f.write('\n        </code>\n      </pre>\n  </body>\n</html>')



