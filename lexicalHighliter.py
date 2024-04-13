import re # Importa el módulo de expresiones regulares

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)
        print(linea)


pattern2 =r'[=+\-\*\/!<>]' #Expresión regular para encontrar los símbolos de opeardores	

parts = [] #Lista para almacenar las partes del texto que no contienen comillas
outside_quotes = [] #Lista para almacenar las partes del texto que no contienen comillas

for line in lineas:
    #Itera sobre cada línea del texto
    line_parts = re.split(r'["\']', line) #Guarda las partes de la línea eliminando las comillas
    line_outside_quotes = line_parts[::2] #Elimina las partes que contenian comillas
    parts += line_parts #Agrega las partes a la lista de partes
    outside_quotes += line_outside_quotes #Agrega las partes a la lista de partes que no contienen comillas
    matches = [re.findall(pattern2, part) for part in outside_quotes] #Encuentra los símbolos de operadores en las partes que no contienen comillas

print(parts)
print(outside_quotes)
print(matches)

for match in matches:
    for symbol in match:
        print (symbol)