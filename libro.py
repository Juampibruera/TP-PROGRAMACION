# Crear un diccionario para cada libro
from cod_generator import generar

libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_ad': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

from cod_generator import generar

# Lista para almacenar los libros
libros = []

def nuevo_libro():
    codigo = generar()
    autor = input("Ingrese el autor del libro: ")
    titulo = input("Ingrese el título del libro: ")
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))
    
    if cant_ej_ad < 0:
        print("Cantidad de ejemplares inválida. Ingrese un número positivo.")
    else:
        libro = {
            "Autor": autor,
            "Titulo": titulo,
            "cant_ej_ad": cant_ej_ad,
            "Codigo": codigo
        }
        libros.append(libro)
        print(f"Libro registrado con éxito. Código: {codigo}")

def generar_codigo():
    codigo = generar()
    return codigo
