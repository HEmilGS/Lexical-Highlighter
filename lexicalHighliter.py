import re # Importa el módulo de expresiones regulares
import keyword # Importa el módulo de palabras reservadas de Python

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)

def highlight_items(line):
    operatorPattern = r'[=+\-\*\/!<>]' #Patron de los operadores
    literalsPattern = r'(("[^"]*")|(\'[^\']*\'))|([0-9]*\.*[0-9]+)|(False)|(True)' #Patron de los literales
    identifiersPattern = r'(?<=\b[a-zA-Z_]\w*\b\s*=|\b=\s*)|([a-zA-Z_]\w*)\b'
    keywordsPattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in keyword.kwlist) + r')\b'
    
    # line = re.sub(literalsPattern,r'__LITERAL1__\g<0>__LITERAL2__',line)# Reemplaza los literales con el texto __LITERAL__ al inicio y al final incluyendo el mismo literal
    # line = re.sub(keywordsPattern, r'__KEYWORD1__\g<0>__KEYWORD2__', line)# Reemplaza las palabras reservadas con las etiquetas span de html
    line = re.sub(identifiersPattern, r'__IDENTIFIER1__\g<0>__INDENTIFIER2__', line)# Reemplaza los identificadores con las etiquetas span de html

    # parts = re.split(r'("[^"]*"|\'[^\']*\')', line)# Separa la línea en partes, si encuentra unas comillas dobles o simples para encontrar los operadores que no estén dentro de las comillas
    # for i in range(0, len(parts),2):# Itera sobre las partes de la línea
    #     parts[i] = re.sub(operatorPattern, r'__OPERATOR1__\g<0>__OPERATOR2__', parts[i])# Reemplaza los operadores con el texto __OPERATOR__ al inicio y al final incluyendo el mismo operador
    # line = ''.join(parts)# Une las partes de la línea con las modificaciones y las partes de las comillas
    
    line = line.replace('__IDENTIFIER1__', '<span class="identifier">').replace('__INDENTIFIER2__', '</span>')#Reemplaza el texto __IDENTIFIER__ por las etiquetas span de html
    # line = line.replace('__KEYWORD1__', '<span class="keyword">').replace('__KEYWORD2__', '</span>')#Reemplaza el texto __KEYWORD__ por las etiquetas span de html
    # line = line.replace('__OPERATOR1__', '<span class="operator">').replace('__OPERATOR2__', '</span>')#Reemplaza el texto __OPERATOR__ por las etiquetas span de html
    # line = line.replace('__LITERAL1__', '<span class="literals">').replace('__LITERAL2__', '</span>')#Reemplaza el texto __LITERAL__ por las etiquetas span de html
    return line

highlighted_lines = [highlight_items(line) for line in lineas] #Aplica la función highlight_items a cada línea del texto

with open('highlighted.html', 'w') as f:
    f.write('<html>\n  <head>\n      <style>.operator { color: red; } .literals {color: orange;} .keyword { color: blue;} .identifier{color: green;}</style>\n  </head>\n\n  <body>\n      <pre>\n        <code>\n')
    f.write('\n'.join(highlighted_lines))
    f.write('\n        </code>\n      </pre>\n  </body>\n</html>')