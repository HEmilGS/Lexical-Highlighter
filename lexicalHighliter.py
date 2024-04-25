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


    parts = re.split(r'("[^"]*"|\'[^\']*\'|#\S+)', line)# Separa la línea en partes, si encuentra unas comillas dobles o simples para encontrar los operadores que no estén dentro de las comillas
    for i in range(0, len(parts), 2):# Itera sobre las partes de la línea
        parts[i] = re.sub(puntuactionPattern, r'__PUNTUACTION1__\g<0>__PUNTUACTION2__', parts[i])# Reemplaza los operadores con el texto __OPERATOR__ al inicio y al final incluyendo el mismo operador
    line = ''.join(parts)# Une las partes de la línea con las modificaciones y las partes de las comillas
    line = line.replace('__PUNTUACTION1__', '<span class="puntuaction">').replace('__PUNTUACTION2__', '</span>')#Reemplaza el texto __OPERATOR__ por las etiquetas span de html
    line = line.replace('__COMMENTS1__', '<span class="comments">').replace('__COMMENTS2__', '</span>')#Reemplaza el texto __LITERAL__ por las etiquetas span de html
    
    return line

highlighted_lines = [highlight_items(line) for line in lineas] #Aplica la función highlight_items a cada línea del texto

with open('highlighted.html', 'w') as f:
    firstPart = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Lexical highligther</title><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet"><style>body{background:rgb(45,45,45);background:linear-gradient(90deg,rgba(45,45,45,1) 0%,rgba(41,83,87,1) 62%,rgba(37,66,100,1) 100%);font-family:'Montserrat',sans-serif;color:#fff;margin:0;padding:0;}.console-window{width:80rem;height:30rem;background-color:#1e1e1e;border-radius:8px;box-shadow:0 0 2rem rgba(0,0,0,0.5);overflow:hidden;margin:10rem auto;padding:2rem;box-sizing:border-box;position:relative;}.title-bar{background-color:#2d2d2d;height:1.5rem;position:absolute;top:0;left:0;right:0;}.title-bar-controls{height:1.5rem;margin-left:0.5rem;display:flex;top:0;position:absolute;}.title-bar-control{width:1rem;height:1rem;border-radius:50%;background-color:#ff5f56;margin-right:0.5rem;margin-top:0.2rem;}.title-bar-control:nth-child(2){background-color:#ffbd2e;}.title-bar-control:last-child{background-color:#27c93f;}.console-content{overflow-y:auto;height:29rem;padding-right:0.5rem;padding-top:0.5rem;}.puntuaction{color:rgb(204,118,209);}.comments{color:rgb(116,152,93);}</style></head><body><pre><code><div class="console-window"><div class="title-bar"><div class="title-bar-controls"><div class="title-bar-control"></div><div class="title-bar-control"></div><div class="title-bar-control"></div></div></div><div class="console-content">"""

    secondPart = """  
        <h1></h1>
          </div>
        </div>
    </code>
    </pre>
    </body>
    </html>"""

    f.write(firstPart)

    f.write('\n'.join(highlighted_lines))

    f.write(secondPart)





