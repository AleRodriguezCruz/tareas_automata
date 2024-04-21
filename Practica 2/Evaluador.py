'''''
Evaluador de Archivos JSON.Este script en Python permite leer archivos JSON, 
verificar si son válidos según la sintaxis JSON y tokenizar los caracteres del archivo, agrupándolos según las reglas JSON
creado por ALEJANDRA RODRIGUEZ DE LA CRUZ 
No_Control:22760049
'''



# Función para leer el contenido de un archivo
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

# Función para tokenizar el contenido del archivo
def tokenizar_contenido(contenido):
    tokens = []
    token = ""
    for caracter in contenido:
        if caracter.isdigit():
            token += caracter
            if any(c.isalpha() for c in contenido[contenido.index(caracter)+1:]):
                tokens.append(float(token))
                token = ""
            else:
                tokens.append(int(token))
                token = ""
        elif caracter.isalpha():
            token += caracter
            tokens.append(token)
            token = ""
        elif caracter == " " or caracter == "\n":
            if token:
                tokens.append(token)
                token = ""
            tokens.append(caracter)
        else:
            if (token >= 48 and token <= 57) or token == ".":
                if token.isdigit():
                    if "." in contenido[contenido.index(caracter)+1:]:
                        tokens.append(float(token))
                    else:
                        tokens.append(int(token))
                else:
                    tokens.append(float(token))
            else:
                tokens.append(caracter)
    if token:
        tokens.append(token)
    return tokens

# Función para mostrar el contenido del archivo junto con sus tokens
def mostrar_contenido_tokens(contenido, tokens):
    for i, token in enumerate(tokens):
        if token == "\n":
            print(f'{token}={contenido[i]}')
        elif token == " ":
            print(f'{token}={contenido[i]}')
        else:
            print(f'{token}={token}')

# Función para escribir el contenido del archivo con sus tokens en un nuevo archivo
def escribir_documento(contenido, tokens):
    with open('salida.txt', 'w') as salida:
        for i, token in enumerate(tokens):
            if token == "\n":
                salida.write(f'{token}=[Enter]\n')
            elif token == " ":
                salida.write(f'{token}=[Espacio]\n')
            else:
                salida.write(f'{token}={token}\n')

# Función para verificar si el archivo es un JSON válido
def es_json(tokens):
    if tokens[0] != 123:  # Verifica si el primer token es el de la llave de apertura '{'
        print('El archivo no es un JSON válido.')
        exit()

# Función principal del programa
def main():
    contenido_archivo = leer_archivo('ejemplo.json')  # Lee el contenido del archivo 'ejemplo.json'
    tokens = tokenizar_contenido(contenido_archivo)   # Tokeniza el contenido del archivo
    
    es_json(tokens)  # Verifica si el archivo es un JSON válido
    
    mostrar_contenido_tokens(contenido_archivo, tokens)  # Muestra el contenido del archivo con sus tokens
    
    escribir_documento(contenido_archivo, tokens)  # Escribe el contenido del archivo con sus tokens en un nuevo archivo

    # Nuevas funciones para tokenizar y evaluar strings
    tokens_array = tokens
    tokens_string = []

    def tokenize_string(array):
        tokens = []
        agrupados = False
        for value in array:
            if (value >= 65 and value <= 90) or (value >= 97 and value <= 122):
                if not agrupados:
                    tokens.append(200)
                    agrupados = True
            else:
                agrupados = False
                tokens.append(value)
        return tokens

    def is_string(array):
        flag = True
        for value in array:
            if value == 34:
                flag = not flag
        if not flag:
            print("ERROR: las comillas no se cerraron")
            exit()

    tokenize_string(tokens_array)
    group_string = tokenize_string(tokens_array)
    print(group_string)
    print(is_string(tokens_array))

if __name__ == '__main__':
    main()
