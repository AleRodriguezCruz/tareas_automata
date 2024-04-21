#Evaluador de Archivos JSON.Este script en Python permite leer archivos JSON, 
#verificar si son válidos según la sintaxis JSON y tokenizar los caracteres del archivo, agrupándolos según las reglas JSON
#creado por ALEJANDRA RODRIGUEZ DE LA CRUZ 
#No_Control:22760049

# Función para leer el contenido de un archivo
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

# Función para tokenizar el contenido del archivo
def tokenizar_contenido(contenido):
    lista_tokens = [ord(caracter) for caracter in contenido]  # Convierte cada carácter del contenido en su valor ASCII
    return lista_tokens

# Función para mostrar el contenido del archivo junto con sus tokens
def mostrar_contenido_tokens(contenido, tokens):
    for i, caracter in enumerate(contenido):
        if caracter == '\n':
            print(f'{tokens[i]}=[Enter]')
        elif caracter == ' ':
            print(f'{tokens[i]}=[Espacio]')
        else:
            print(f'{tokens[i]}={caracter}')

# Función para escribir el contenido del archivo con sus tokens en un nuevo archivo
def escribir_documento(contenido, tokens):
    with open('salida.txt', 'w') as salida:
        for i, caracter in enumerate(contenido):
            if caracter == '\n':
                salida.write(f'{tokens[i]}=[ENTER]\n')
            elif caracter == ' ':
                salida.write(f'{tokens[i]}=[ESPACIO]\n')
            else:
                salida.write(f'{tokens[i]}={caracter}\n')

# Función para verificar si el archivo es un JSON válido
def es_json(tokens):
    if tokens[0] != 123:  # Verifica si el primer token es el de la llave de apertura '{'
        print('El archivo no es un JSON válido.')
        exit()

# Función para agrupar los tokens de las cadenas de caracteres en un solo token
def tokenizar_cadena(tokens):
    tokens_agrupados = []
    en_cadena = False
    for token in tokens:
        if (token >= 65 and token <= 90) or (token >= 97 and token <= 122) or (token >= 48 and token <= 57):
            if not en_cadena:
                tokens_agrupados.append(200)  # Añade un token especial para indicar inicio de cadena
                en_cadena = True
        else:
            if en_cadena:
                tokens_agrupados.append(201)  # Añade un token especial para indicar fin de cadena
                en_cadena = False
            tokens_agrupados.append(token)
    if en_cadena:  # Si la cadena termina al final de los tokens
        tokens_agrupados.append(201)  # Añade un token especial para indicar fin de cadena
    return tokens_agrupados

# Función para verificar si todas las comillas en el archivo están cerradas correctamente
def es_cadena(tokens):
    flag = True 
    for token in tokens:
        if token == 34:  # Verifica si el token corresponde a una comilla doble '"'
            flag = not flag  # Cambia el valor del flag cada vez que encuentra una comilla doble
    if flag:
        return True  # Si el flag es True al final, todas las comillas están cerradas correctamente
    else:
        return False  # Si el flag es False, hay comillas sin cerrar

# Función para evaluar el parámetro de edad
def evaluar_edad(tokens):
    edad_encontrada = False
    for token in tokens:
        if token == 34:  # Verifica si el token corresponde a una comilla doble '"'
            if edad_encontrada:
                return True
            edad_encontrada = False
        elif token >= 48 and token <= 57:  # Verifica si el token es un dígito
            if edad_encontrada:
                return False
            edad_encontrada = True
    return False

# Función principal del programa
def main():
    contenido_archivo = leer_archivo('ejemplo.json')  # Lee el contenido del archivo 'ejemplo.json'
    tokens = tokenizar_contenido(contenido_archivo)   # Tokeniza el contenido del archivo
    
    es_json(tokens)  # Verifica si el archivo es un JSON válido
    
    tokenizar_cadena(tokens)  # Agrupa los tokens de las cadenas de caracteres
    
    lista_tokens = [ord(caracter) for caracter in contenido_archivo]  # Convierte cada carácter del contenido en su valor ASCII
    
    mostrar_contenido_tokens(contenido_archivo, lista_tokens)  # Muestra el contenido del archivo con sus tokens
    
    escribir_documento(contenido_archivo, lista_tokens)  # Escribe el contenido del archivo con sus tokens en un nuevo archivo
    
    tokens_agrupados = tokenizar_cadena(tokens)  # Obtiene los tokens agrupados de las cadenas de caracteres
    
    print(f'Tokens: {tokens}')  # Imprime los tokens originales
    
    print(tokens_agrupados)  # Imprime los tokens agrupados

    if not es_cadena(tokens):  # Verifica si todas las comillas están cerradas correctamente si no no es un string
        print("ERROR: Las comillas no se cerraron correctamente")

    # Evalúa el parámetro de edad
    if evaluar_edad(tokens):
        print("ERROR: El parámetro de edad no está en el formato correcto")

if __name__ == '__main__':
    main()
