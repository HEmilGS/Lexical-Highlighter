import re
import keyword
# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archiv:
    # Itera sobre cada línea del archivo
    for linea in archiv:
        # Imprime cada línea
        print(linea)



#Identifiers and keywords REGEX patterns

def is_identifier(word):
    identifiers_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    match = re.match(identifiers_pattern,word)
    print(match)
    return match

def is_keyword(word):   
    keywords_pattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in keyword.kwlist) +r')\b'
    match = re.match(keywords_pattern, word)
    print(match)
    return match

x = "for i in index: "
is_identifier(x)
is_keyword(x)

