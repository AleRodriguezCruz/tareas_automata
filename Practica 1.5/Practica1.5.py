import json

# Función para asignar tokens Unicode a los caracteres del contenido, asignando 58 a los dos puntos ':'
def tokenizar_contenido(contenido):
    tokens = {}
    for caracter in contenido:
        if caracter == ':':
            tokens[caracter] = 58  # Asignar el valor 58 a los dos puntos ':'
        else:
            valor = ord(caracter)
            tokens[caracter] = valor
    return tokens

# Leer el contenido del archivo JSON
with open('ejemplo.json') as file:
    data = json.load(file)
    contenido = json.dumps(data)

# Asignar tokens a cada carácter del contenido JSON
tokens = tokenizar_contenido(contenido)

# Construir el archivo de salida 
with open('resultado.txt', 'w') as file:
    for char in contenido:
        if char == ' ':
            file.write('(Espacio) : 32\n')
        elif char == '\n':
            file.write('(Enter) : 10\n')
        else:
            file.write(f'"{char}" : {tokens[char]}\n')

print("Proceso completado. Los datos del archivo JSON se han guardado en resultado.txt ")
