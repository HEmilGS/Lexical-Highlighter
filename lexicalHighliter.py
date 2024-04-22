import re # Importa el módulo de expresiones regulares

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)

def highlight_operators(line):
    operatorPattern = r'[=+\-\*\/!<>]' #Patron de los operadores
    literalsPattern = r'(("[^"]*")|(\'[^\']*\'))|([0-9]*\.*[0-9]+)' #Patron de los literales
    
    line = re.sub(literalsPattern,r'__LITERAL1__\g<0>__LITERAL2__',line)# Reemplaza los literales con el texto __LITERAL__ al inicio y al final incluyendo el mismo literal
    parts = re.split(r'("[^"]*"|\'[^\']*\')', line)# Separa la línea en partes, si encuentra unas comillas dobles o simples
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(operatorPattern, r'__OPERATOR1__\g<0>__OPERATOR2__', parts[i])# Reemplaza los operadores con el texto __OPERATOR__ al inicio y al final incluyendo el mismo operador
    line = ''.join(parts)# Une las partes de la línea con las modificaciones y las partes de las comillas
    line = line.replace('__OPERATOR1__', '<span class="operator">').replace('__OPERATOR2__', '</span>')#Reemplaza el texto __OPERATOR__ por las etiquetas span de html
    line = line.replace('__LITERAL1__', '<span class="literals">').replace('__LITERAL2__', '</span>')#Reemplaza el texto __LITERAL__ por las etiquetas span de html
    return line

highlighted_lines = [highlight_operators(line) for line in lineas] #Aplica la función highlight_operators a cada línea del texto

with open('highlighted.html', 'w') as f:
    f.write('<html><head><style>.operator { color: red; } .literals {color: blue;}</style></head><body><pre><code>\n')
    f.write('\n'.join(highlighted_lines))
    f.write('\n</code></pre></body></html>')