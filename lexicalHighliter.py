import re # Importa el módulo de expresiones regulares

lineas = [] #Lista para almacenar las líneas del texto
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        lineas.append(linea)

def highlight_operators(line):
    operatorPattern = r'[=+\-\*\/!<>]'
    literalsPattern = r'(("[^"]*")|(\'[^\']*\'))|([0-9]*\.*[0-9]+)*'
    line = re.sub(literalsPattern, r'<span class="literals">\g<0></span>', line)
    parts = re.split(r'("[^"]*"|\'[^\']*\')', line)

    # for i in range(0, len(parts), 2):  # Only apply to every other segment
    #     print(parts[i])
    #     print("salto de lineaxd")
    #     parts[i] = re.sub(operatorPattern, r'<span class="operator">\g<0></span>', parts[i])
    line = ''.join(parts)
    #print(line)
    return line

highlighted_lines = [highlight_operators(line) for line in lineas]

print(lineas)

with open('highlighted.html', 'w') as f:
    f.write('<html><head><style>.operator { color: red; } .literals {color: blue;}</style></head><body><pre><code>\n')
    f.write('\n'.join(highlighted_lines))
    f.write('\n</code></pre></body></html>')