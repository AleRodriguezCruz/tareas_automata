import json

# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as file:
    # Inicializa un diccionario vacío
    diccionario = {}
    # Inicializa un diccionario para almacenar las claves que cumplen con ambas condiciones
    evaluador = {}
    
    # Variable para indicar si se ha encontrado el valor '34'
    encontrado = False
    
    # Lee cada línea del archivo
    for line in file:
        # Verifica si la línea tiene el formato esperado (clave y valor separados por un espacio)
        if ' ' in line.strip():
            split_line = line.strip().split(' ')
            
            # Verifica si se han generado más de dos valores al dividir la línea
            if len(split_line) == 2:
                key, value = split_line
                
                # Agrega la clave al diccionario original
                diccionario[key] = value
                
                # Evalúa si el valor es igual a '34'
                if value == '34':
                    encontrado = True
                    break  # Sale del bucle al encontrar '34'
                
                # Evalúa si el valor está en el rango de 65 a 90 o de 97 a 122
                if (65 <= ord(value) <= 90) or (97 <= ord(value) <= 122):
                    evaluador[key] = value
            else:
                print("Error: Formato incorrecto en la línea:", line)
        else:
            print("Error: Formato incorrecto en la línea:", line)

# Imprime el diccionario resultante
print("Diccionario original:")
print(diccionario)

# Imprime el diccionario de claves que cumplen con las condiciones adicionales
print("Diccionario evaluador:")
print(evaluador)

if encontrado:
    print("Se encontró el valor '34'. Proceso detenido.")
else:
    print("No se encontró el valor '34'. Proceso completado.")
