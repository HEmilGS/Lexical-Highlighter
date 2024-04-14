import re # Importa el módulo de expresiones regulares

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)


operatorPattern =r'[=+\-\*\/!<>]' #Expresión regular para encontrar los símbolos de opeardores	
literalsPattern = r'["True"]*["False"]*["None"]*' #Expresión regular para encontrar los literales

text = "x = True xdasdf False"
x = re.findall(literalsPattern,text)
print(x)


operatorParts = [] #Lista para almacenar las partes del texto que no contienen comillas
operatorOutsideQuotes = [] #Lista para almacenar las partes del texto que no contienen comillas

for line in lineas:
    #Itera sobre cada línea del texto
    line_parts = re.split(r'["\']', line) #Guarda las partes de la línea eliminando las comillas
    line_outside_quotes = line_parts[::2] #Elimina las partes que contenian comillas
    operatorParts += line_parts #Agrega las partes a la lista de partes
    operatorOutsideQuotes += line_outside_quotes #Agrega las partes a la lista de partes que no contienen comillas
    matches = [re.findall(operatorPattern, part) for part in operatorOutsideQuotes] #Encuentra los símbolos de operadores en cada parte de las partes sin comillas

print(operatorParts)

for match in matches:
    for symbol in match:
        print (symbol)