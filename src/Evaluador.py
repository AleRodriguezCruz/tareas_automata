#Evaluador de Archivos JSON.Este script en Python permite leer archivos JSON, 
#verificar si son válidos según la sintaxis JSON y tokenizar los caracteres del archivo, agrupándolos según las reglas JSON
#creado por ALEJANDRA RODRIGUEZ DE LA CRUZ 
#No_Control:22760049

import json

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

def tokenizar_contenido(contenido):
    return [ord(char) for char in contenido]

def es_fecha(tokens, i):
    if i + 9 < len(tokens):
        return (tokens[i] >= 48 and tokens[i] <= 57 and
                tokens[i+1] >= 48 and tokens[i+1] <= 57 and
                tokens[i+2] >= 48 and tokens[i+2] <= 57 and
                tokens[i+3] >= 48 and tokens[i+3] <= 57 and
                tokens[i+4] == 45 and
                tokens[i+5] >= 48 and tokens[i+5] <= 57 and
                tokens[i+6] >= 48 and tokens[i+6] <= 57 and
                tokens[i+7] == 45 and
                tokens[i+8] >= 48 and tokens[i+8] <= 57 and
                tokens[i+9] >= 48 and tokens[i+9] <= 57)
    return False

def es_decimal(tokens, i):
    if i + 2 < len(tokens) and tokens[i] >= 48 and tokens[i] <= 57:
        for j in range(i + 1, len(tokens)):
            if tokens[j] == 46:
                if j + 1 < len(tokens) and tokens[j + 1] >= 48 and tokens[j + 1] <= 57:
                    return True
                else:
                    return False
            elif not (tokens[j] >= 48 and tokens[j] <= 57):
                return False
    return False

def tokenizar_cadena(tokens):
    tokens_agrupados = []
    i = 0
    while i < len(tokens):
        if (tokens[i] >= 65 and tokens[i] <= 90) or (tokens[i] >= 97 and tokens[i] <= 122):
            tokens_agrupados.append(200)
        elif (tokens[i] >= 48 and tokens[i] <= 57):
            if es_fecha(tokens, i):
                tokens_agrupados.append(300)
                i += 9
            elif es_decimal(tokens, i):
                tokens_agrupados.append(202)
                while i < len(tokens) and ((tokens[i] >= 48 and tokens[i] <= 57) or tokens[i] == 46):
                    i += 1
                i -= 1
            else:
                tokens_agrupados.append(201)
        else:
            tokens_agrupados.append(tokens[i])
        i += 1
    return tokens_agrupados

def verificar_tipos(tokens):
    contiene_cadena = False
    contiene_numero_entero = False
    contiene_decimal = False
    contiene_fecha = False

    for token in tokens:
        if token == 200:
            contiene_cadena = True
        elif token == 201:
            contiene_numero_entero = True
        elif token == 202:
            contiene_decimal = True
        elif token == 300:
            contiene_fecha = True

    return contiene_cadena, contiene_numero_entero, contiene_decimal, contiene_fecha

def es_cadena(tokens):
    stack = []
    for token in tokens:
        if token == 34:  # comillas dobles
            if stack and stack[-1] == 34:
                stack.pop()
            else:
                stack.append(token)
    return not stack

def mostrar_contenido_tokens(contenido, tokens):
    for i, char in enumerate(contenido):
        print(f'{char}={tokens[i]}')

def escribir_documento(contenido, tokens):
    with open('output_tokens.txt', 'w') as archivo:
        for i, char in enumerate(contenido):
            archivo.write(f'{char}={tokens[i]}\n')

def main():
    contenido_archivo = leer_archivo('ejemplo.json')
    tokens = tokenizar_contenido(contenido_archivo)
    
    
    
    tokens_agrupados = tokenizar_cadena(tokens)
    
    mostrar_contenido_tokens(contenido_archivo, tokens)
    
    escribir_documento(contenido_archivo, tokens)
    
    print(f'Tokens originales: {tokens}')
    print(f'Tokens agrupados: {tokens_agrupados}')

    contiene_cadena, contiene_numero_entero, contiene_decimal, contiene_fecha = verificar_tipos(tokens_agrupados)

    if not es_cadena(tokens):
        print("ERROR: Las comillas no se cerraron correctamente")

    if contiene_cadena:
        print("El JSON contiene cadenas de texto.")
    if contiene_numero_entero:
        print("El JSON contiene números enteros.")
    if contiene_decimal:
        print("El JSON contiene números decimales.")
    if contiene_fecha:
        print("El JSON contiene fechas.")

if __name__ == '__main__':
    main()
