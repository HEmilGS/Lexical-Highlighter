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
    puntuactionPattern = r'[\[\](){},:.\]]' #Patron de los operadores
    commentsPattern = r'#.*$'
    operatorPattern = r'[=+\-\*\/!<>]' #Patron de los operadores
    literalsPattern = r'(?<![#a-zA-Z_.])(("[^"]*")|(\'[^\']*\')|([0-9]*\.*[0-9]+)|(False)|(True))(?![#a-zA-Z_0-9])' #Patron de los literales
    keywordsPattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in keyword.kwlist) + r')\b'

    identifiersPattern = r'(?=^#*)(([a-zA-Z_]+)[0-9]*([a-zA-Z_]+))'
    #identifiersPattern = r'(?<![#"\'])([a-zA-Z_]+[a-zA-Z_0-9]*)'


    id2 = r'\b([a-zA-Z_]\w*)\b(?=\s*(<|=|!=)\s*([a-zA-Z_]\w*))'
    

    line = re.sub(commentsPattern,r'$COMMENTS1__\g<0>$COMMENTS2__',line)# Reemplaza los literales con el texto __LITERAL__ al inicio y al final incluyendo el mismo literal

    line = re.sub(literalsPattern,r'#LITERALa__\g<0>#LITERALb__',line)# Reemplaza los literales con el texto #LITERAL# al inicio y al final incluyendo el mismo literal
    
    line = re.sub(identifiersPattern, r'#IDENTIFIERa__\g<0>#IDENTIFIERb__', line)# Reemplaza los identificadores con las etiquetas span de html
    

    parts = re.split(r'("[^"]*"|\'[^\']*\'|^#.*\s)', line)# Separa la línea en partes, si encuentra unas comillas dobles o simples para encontrar los operadores que no estén dentro de las comillas
    for i in range(len(parts)):
        # Solo reemplaza en partes que no son cadenas ni comentarios
        if not parts[i].startswith(('"', "'", '#')):
            parts[i] = re.sub(operatorPattern, r'#OPERATORa__\g<0>#OPERATORb__', parts[i])
    line = ''.join(parts)
    line = re.sub(keywordsPattern, r'#KEYWORDa__\g<0>#KEYWORDb__', line)# Reemplaza las palabras reservadas con las etiquetas span de html

    parts = re.split(r'("[^"]*"|\'[^\']*\'|#)', line)# Separa la línea en partes, si encuentra unas comillas dobles o simples para encontrar los operadores que no estén 
    for i in range(len(parts)):
        # Solo reemplaza en partes que no son cadenas ni comentarios
        if not parts[i].startswith(('"', "'", '#')):
            parts[i] = re.sub(puntuactionPattern, r'__PUNTUACTION1__\g<0>__PUNTUACTION2__', parts[i])
    line = ''.join(parts)# Une las partes de la línea con las modificaciones y las partes de las comillas


    
    line = line.replace('__PUNTUACTION1__', '<span class="puntuaction">').replace('__PUNTUACTION2__', '</span>')#Reemplaza el texto __OPERATOR__ por las etiquetas span de html
    line = line.replace('$COMMENTS1__', '<span class="comments">').replace('$COMMENTS2__', '</span>')#Reemplaza el texto __LITERAL__ por las etiquetas span de html
    line = line.replace('#OPERATORa__', '<span class="operator">').replace('#OPERATORb__', '</span>')#Reemplaza el texto #OPERATOR# por las etiquetas span de html
    line = line.replace('#LITERALa__', '<span class="literals">').replace('#LITERALb__', '</span>')#Reemplaza el texto #LITERAL# por las etiquetas span de html
    line = line.replace('#IDENTIFIERa__', '<span class="identifier">').replace('#IDENTIFIERb__', '</span>')#Reemplaza el texto #IDENTIFIER# por las etiquetas span de html
    line = line.replace('#KEYWORDa__', '<span class="keyword">').replace('#KEYWORDb__', '</span>')#Reemplaza el texto #KEYWORD# por las etiquetas span de html
    return line

highlighted_lines = [highlight_items(line) for line in lineas] #Aplica la función highlight_items a cada línea del texto

#print('\n'.join(highlighted_lines)) #Imprime las líneas del texto

# with open('highlighted.html', 'w') as f:
#     f.write('<html>\n  <head>\n      <style>.operator { color: red; } .literals {color: orange;} .keyword { color: blue;} .identifier{color: pink;}</style>\n  </head>\n\n  <body>\n      <pre>\n        <code>\n')
#     f.write('\n'.join(highlighted_lines))
#     f.write('\n        </code>\n      </pre>\n  </body>\n</html>')

with open('highlighted.html', 'w') as f:
    firstPart = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>MacOS Console</title><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet"><style>body{background:rgb(45,45,45);background:linear-gradient(90deg,rgba(45,45,45,1) 0%,rgba(41,83,87,1) 62%,rgba(37,66,100,1) 100%);font-family:'Montserrat',sans-serif;color:#fff;margin:0;padding:0;}.console-window{width:80rem;height:30rem;background-color:#1e1e1e;border-radius:8px;box-shadow:0 0 2rem rgba(0,0,0,0.5);overflow:hidden;margin:10rem auto;padding:2rem;box-sizing:border-box;position:relative;}.title-bar{background-color:#2d2d2d;height:1.5rem;position:absolute;top:0;left:0;right:0;}.title-bar-controls{height:1.5rem;margin-left:0.5rem;display:flex;top:0;position:absolute;}.title-bar-control{width:1rem;height:1rem;border-radius:50%;background-color:#ff5f56;margin-right:0.5rem;margin-top:0.2rem;}.title-bar-control:nth-child(2){background-color:#ffbd2e;}.title-bar-control:last-child{background-color:#27c93f;}.console-content{overflow-y:auto;height:29rem;padding-right:0.5rem;padding-top:0.5rem;}.puntuaction{color:rgb(204,118,209);}.comments{color:rgb(116,152,93);}.operator { color: red; } .literals {color: orange;} .keyword { color: blue;} .identifier{color: black;}</style></head><body><pre><code><div class="console-window"><div class="title-bar"><div class="title-bar-controls"><div class="title-bar-control"></div><div class="title-bar-control"></div><div class="title-bar-control"></div></div></div><div class="console-content">"""

    secondPart = """    </div>
        </div>
    </code>
    </pre>
    </body>
    </html>"""

    f.write(firstPart)

    f.write('\n'.join(highlighted_lines))

    f.write(secondPart)