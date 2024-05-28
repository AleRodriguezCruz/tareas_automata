import json


def leer_archivo(nombre_archivo):
    """Reads a JSON file and returns the parsed data."""
    try:
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' no tiene un formato JSON válido.")
        return None


def tokenizar_contenido(contenido):
    """Converts the JSON content to a list of ASCII character codes."""
    return [ord(char) for char in contenido]


def es_fecha(tokens, i, formato="DD/MM/YYYY"):
    """Checks if a sequence of tokens represents a valid date in the specified format."""
    if i + len(formato) < len(tokens):
        try:
            for j, char in enumerate(formato):
                if not (tokens[i + j] >= 48 and tokens[i + j] <= 57):
                    return False
                if j < len(formato) - 1 and tokens[i + j + 1] != char:
                    return False
            return True
        except IndexError:
            return False
    return False


def es_decimal(tokens, i):
    """Checks if a sequence of tokens represents a valid decimal number."""
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


def tokenizar_cadena(tokens, contenido_archivo):
    """Processes the character codes and identifies data types within the JSON content."""
    tokens_agrupados = []
    i = 0
    in_string = False
    while i < len(tokens):
        if tokens[i] == 34:  # Comillas dobles
            if in_string:
                in_string = False
                tokens_agrupados.append(200)  # Token para cadena de texto
            else:
                in_string = True
        elif in_string and ((tokens[i] >= 65 and tokens[i] <= 90) or (tokens[i] >= 97 and tokens[i] <= 122) or tokens[i] in [33, 92]):
            tokens_agrupados.append(200)

        elif (tokens[i] >= 48 and tokens[i] <= 57) and (i == 0 or tokens[i - 1] != 46):  # Verificar que no haya punto
            tokens_agrupados.append(201)  # Token para número entero
            while i < len(tokens) and (tokens[i] >= 48 and tokens[i] <= 57):
                i += 1
            if i < len(tokens) and tokens[i] == 44:  # Verificar si hay una coma después
                tokens_agrupados.append(44)  # Token para coma
                i += 1
            i -= 1
        elif es_decimal(tokens, i):
            j = i
            while j < len(tokens) and (tokens[j] >= 48 and tokens[j] <= 57):
                j += 1
            if j > i + 1 and tokens[i] == 48:
                print(
                    "Error: Número decimal con ceros a la izquierda del punto decimal."
                )
                return None
            elif j > i + 1 and tokens[j - 1] == 46:
                print(
                    "Error: Número decimal con punto adicional al final."
                )
                return None
            else:
                tokens_agrupados.append(202)  # Token para número decimal
        elif es_fecha(tokens,
