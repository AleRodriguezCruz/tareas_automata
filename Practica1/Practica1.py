import json
import re

# Función para validar que la entrada contenga solo letras
def solo_letras(texto):
    return bool(re.match("^[a-zA-Z]*$", texto))

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Validar la entrada del usuario
while not solo_letras(nombre):
    print("Por favor, ingrese solo letras.")
    nombre = input("Ingrese su nombre: ")
# Crea un diccionario con los datos ingresados por el usuario
datos = {
    "nombre": nombre,
}

# Escribe los datos en un archivo JSON
with open('ejemplo.json', 'w') as archivo_json:
    json.dump(datos, archivo_json, indent=4)

# Abre el archivo JSON
with open('ejemplo.json', 'r') as f:
    # Carga el contenido del archivo en un objeto JSON
    data = json.load(f)

# Imprime los caracteres del objeto JSON en vertical y con espacios
print("{")
print("[ENTER]")
for key, value in data.items():
    print('"')
    if key == "nombre":
        for char in str(key):
            print(char)
        print("[ESPACIO]")
        print('"')
        print(":")
        print('"')
        for char in str(value):
            if char == " ":
                print("[ESPACIO]")
            else:
                print(char)
        print('"')
        print("[ENTER]")
    else:
        for char in str(value):
            if char == " ":
                print("[ESPACIO]")
            else:
                print(char)
        print("[ENTER]")
print("}")
