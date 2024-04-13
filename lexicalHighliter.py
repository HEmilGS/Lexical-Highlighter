import re

# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Itera sobre cada línea del archivo
    for linea in archivo:
        # Imprime cada línea
        print(linea)


text = 'x =++ "a+b" - 3 * 4 /'
literal_pattern = r'[(=)*(+)*(\-)*(\*)*(/)*(!)*(<)*(>)*][(\")*(\")*(\')*(\')*][(=)*(+)*(\-)*(/)*(!)*(<)*(>)*]'

pattern2 =r'[=+\-\*\/!<>]'
parts = re.split(r'["\']', text)
outside_quotes = parts[::2]
#([(\")*(\')*])

matches = [re.findall(pattern2, part) for part in outside_quotes]

print(parts)
print(outside_quotes)
print(matches)

for match in matches:
    for symbol in match:
        print (symbol)

#print(gmail_addresses)