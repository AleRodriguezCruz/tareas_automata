import json

# Función para leer los valores del archivo tokens.txt
def leer_archivo_tokens(ruta_del_archivo):
    valores_simbolos = {}
    with open(ruta_del_archivo, encoding='utf-8') as f:
        for linea in f:
            campos = linea.strip().split(" ")
            if len(campos) > 1:
                clave, valor = campos[:2]
                try:
                    int_valor = int(valor)
                    valores_simbolos[clave] = int_valor
                except ValueError:
                    valores_simbolos[clave] = valor
    return valores_simbolos

# Leer los valores del archivo tokens.txt
valores_simbolos = leer_archivo_tokens('tokens.txt')

# Convertir el archivo JSON a un diccionario
with open('ejemplo.json') as file:
    data = json.load(file)

# Construir el archivo de salida en el formato deseado con códigos ASCII para caracteres especiales
with open('resultado.txt', 'w') as file:
    file.write('{" : 123\n')
    file.write('"":34\n')
    
    for key, value in data.items():
        for char in key:  # Procesar cada carácter de la clave
            if char == ' ':
                file.write('(Espacio) : 32\n')
            elif char == '\n':
                file.write('(Enter) : 10\n')
            else:
                file.write(f'"{char}" : {ord(char)}\n')
        
        file.write('"":34\n')

        if isinstance(value, str):
            for char in value:  # Procesar cada carácter del valor si es una cadena
                if char == ' ':
                    file.write('(Espacio) : 32\n')
                elif char == '\n':
                    file.write('(Enter) : 10\n')
                else:
                    file.write(f'"{char}" : {ord(char)}\n')

        file.write('"":34\n')

    file.write('"}" : 125\n')

print("Proceso completado. Los datos del archivo JSON se han guardado en resultado.txt ")
