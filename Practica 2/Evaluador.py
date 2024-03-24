#Evaluador de Archivos JSON.Este script en Python permite leer archivos JSON, 
#verificar si son válidos según la sintaxis JSON y tokenizar los caracteres del archivo, agrupándolos según las reglas JSON
#creado por ALEJANDRA RODRIGUEZ DE LA CRUZ 
#No_Control:22760049

# Función para leer el contenido de un archivo
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# Función para tokenizar el contenido del archivo
def tokenize_content(content):
    tokens_list = [ord(char) for char in content]  # Convierte cada carácter del contenido en su valor ASCII
    return tokens_list

# Función para mostrar el contenido del archivo junto con sus tokens
def show_content_tokens(content, tokens):
    for char in content:
        if char == '\n':
            print(f'{tokens[char]}=[Enter]')
        elif char == ' ':
            print(f'{tokens[char]}=[SPACE]')
        else:
            print(f'{tokens[char]}={char}')

# Función para escribir el contenido del archivo con sus tokens en un nuevo archivo
def write_document(content, tokens):
    with open('salida.txt', 'w') as output:
        for char in content:
            if char == '\n':
                output.write(f'{tokens[char]}=[ENTER]\n')
            elif char == ' ':
                output.write(f'{tokens[char]}=[SPACE]\n')
            else:
                output.write(f'{tokens[char]}={char}\n')

# Función para verificar si el archivo es un JSON válido
def is_json(tokens):
    if tokens[0] != 123:  # Verifica si el primer token es el de la llave de apertura '{'
        print('El archivo no es un JSON válido.')
        exit()

# Función para agrupar los tokens de las cadenas de caracteres en un solo token
def tokenize_string(tokens):
    grouped_tokens = []
    in_string = False
    for token in tokens:
        if (token >= 65 and token <= 90) or (token >= 97 and token <= 122):
            if not in_string:
                grouped_tokens.append(200)  # Añade un token especial para indicar inicio de cadena
                in_string = True
        else:
            in_string = False
            grouped_tokens.append(token)
    return grouped_tokens

# Función para verificar si todas las comillas en el archivo están cerradas correctamente
def is_string(tokens):
    flag = True 
    for token in tokens:
        if token == 34:  # Verifica si el token corresponde a una comilla doble '"'
            flag = not flag  # Cambia el valor del flag cada vez que encuentra una comilla doble
    if flag:
        return True  # Si el flag es True al final, todas las comillas están cerradas correctamente
    else:
        return True  # Si el flag es False, hay comillas sin cerrar

# Función principal del programa
def main():
    file_content = read_file('ejemplo.json')  # Lee el contenido del archivo 'ejemplo.json'
    tokens = tokenize_content(file_content)   # Tokeniza el contenido del archivo
    
    is_json(tokens)  # Verifica si el archivo es un JSON válido
    
    tokenize_string(tokens)  # Agrupa los tokens de las cadenas de caracteres
    
    show_content_tokens(file_content, {char: ord(char) for char in file_content})  # Muestra el contenido del archivo con sus tokens
    
    write_document(file_content, {char: ord(char) for char in file_content})  # Escribe el contenido del archivo con sus tokens en un nuevo archivo
    
    grouped_tokens = tokenize_string(tokens)  # Obtiene los tokens agrupados de las cadenas de caracteres
    
    print(f'Tokens: {tokens}')  # Imprime los tokens originales
    
    print(grouped_tokens)  # Imprime los tokens agrupados

    if not is_string(tokens):  # Verifica si todas las comillas están cerradas correctamente si no no es un string
        print("ERROR: Las comillas no se cerraron correctamente")

if __name__ == '__main__':
    main()
