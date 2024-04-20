import re # Importa el módulo de expresiones regulares

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)

operatorPattern =r'[=+\-\*\/!<>]' #Expresión regular para encontrar los símbolos de opeardores	
literalsPattern = r'["\']*[a-zA-Z0-9]["\']|[=]*[0-9]' #Expresión regular para encontrar los literales

text = "x = True xdasdf False"
x = re.findall(literalsPattern,text)
#print(x)


operatorParts = [] #Lista para almacenar las partes del texto que no contienen comillas
operatorOutsideQuotes = [] #Lista para almacenar las partes del texto que no contienen comillas

# for line in lineas:
#     #Itera sobre cada línea del texto
#     line_parts = re.split(r'["\']', line) #Guarda las partes de la línea eliminando las comillas
#     line_outside_quotes = line_parts[::2] #Elimina las partes que contenian comillas
#     operatorParts += line_parts #Agrega las partes a la lista de partes
#     operatorOutsideQuotes += line_outside_quotes #Agrega las partes a la lista de partes que no contienen comillas
#     matches = [re.findall(operatorPattern, part) for part in operatorOutsideQuotes] #Encuentra los símbolos de operadores en cada parte de las partes sin comillas

#matches = [match for match in matches if match] #Elimina las listas vacías
#operators =  [''.join(inner_list) for inner_list in matches] #Convierte la lista de listas en una lista de strings
#print(operators)

# for match in matches:
#     print(match)
#     for symbol in match:
#         print (match)

def highlight_operators(line,operatorPattern):
    #for operator in operators:
        # Escape the operator in case it contains special regex characters
        operatorPattern =r'(?!["\'])[=+\-\*\/!<>](?!["\'])'
        #escaped_operator = re.escape(operator)
        # Wrap the operator in a span with class "operator", only if it's not inside quotes
        line = re.sub(operatorPattern, r'<span class="operator">\g<0></span>', line)
        #line = re.sub(r'(?<![\'])' + escaped_operator + r'(?![^"]*")', r'<span class="operator">\g<0></span>', line)
        return line

#highlighted_lines = [highlight_operators(line, operators) for line in lineas]
highlighted_lines = [highlight_operators(line,operatorPattern) for line in lineas]

print(lineas)

with open('highlighted.html', 'w') as f:
    f.write('<html><head><style>.operator { color: red; }</style></head><body><pre><code>\n')
    f.write('\n'.join(highlighted_lines))
    f.write('\n</code></pre></body></html>')