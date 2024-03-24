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
    for caracter in contenido:
        if caracter == '\n':
            print(f'{tokens[caracter]}=[Enter]')
        elif caracter == ' ':
            print(f'{tokens[caracter]}=[Espacio]')
        else:
            print(f'{tokens[caracter]}={caracter}')

# Función para escribir el contenido del archivo con sus tokens en un nuevo archivo
def escribir_documento(contenido, tokens):
    with open('salida.txt', 'w') as salida:
        for caracter in contenido:
            if caracter == '\n':
                salida.write(f'{tokens[caracter]}=[ENTER]\n')
            elif caracter == ' ':
                salida.write(f'{tokens[caracter]}=[ESPACIO]\n')
            else:
                salida.write(f'{tokens[caracter]}={caracter}\n')

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
        if (token >= 65 and token <= 90) or (token >= 97 and token <= 122):
            if not en_cadena:
                tokens_agrupados.append(200)  # Añade un token especial para indicar inicio de cadena
                en_cadena = True
        else:
            en_cadena = False
            tokens_agrupados.append(token)
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
        return True  # Si el flag es False, hay comillas sin cerrar

# Función principal del programa
def main():
    contenido_archivo = leer_archivo('ejemplo.json')  # Lee el contenido del archivo 'ejemplo.json'
    tokens = tokenizar_contenido(contenido_archivo)   # Tokeniza el contenido del archivo
    
    es_json(tokens)  # Verifica si el archivo es un JSON válido
    
    tokenizar_cadena(tokens)  # Agrupa los tokens de las cadenas de caracteres
    
    mostrar_contenido_tokens(contenido_archivo, {caracter: ord(caracter) for caracter in contenido_archivo})  # Muestra el contenido del archivo con sus tokens
    
    escribir_documento(contenido_archivo, {caracter: ord(caracter) for caracter in contenido_archivo})  # Escribe el contenido del archivo con sus tokens en un nuevo archivo
    
    tokens_agrupados = tokenizar_cadena(tokens)  # Obtiene los tokens agrupados de las cadenas de caracteres
    
    print(f'Tokens: {tokens}')  # Imprime los tokens originales
    
    print(tokens_agrupados)  # Imprime los tokens agrupados

    if not es_cadena(tokens):  # Verifica si todas las comillas están cerradas correctamente si no no es un string
        print("ERROR: Las comillas no se cerraron correctamente")

if __name__ == '__main__':
    main()
