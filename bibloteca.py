import libro as l
import cod_generator
from cod_generator import generar  # Importa la función generar desde cod_generator

libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def registrar_nuevo_libro():
    cod = input("Ingrese el codigo del libro que quiere ver los ejemplares prestados: ")
    for libro in libros:
        if libro["cod"] == cod and libro["cant_ej_pr"] >= 1:
            print(f"Los ejemplares prestados son: {libro['cant_ej_pr']}")
            return None
    print("El código ingresado no existe")
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    autor = input("Ingrese el autor del libro: ") #Se le pide al usuario el autor del libro que se quiere ingresar
    titulo = input("Ingrese el título del libro: ") #Se le pide al usuario el título del libro que se quiere ingresar
    cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: ")) #Se le pide al usuario la cantidad de libros que quiere ingresar
    cod = generar() #Genera el codigo instantaneamente
    libros.append({ #Agrega el nuevo libro al diccionario libros[]
        "Autor": autor,
        "Titulo": titulo,
        "cant_ej_ad": cant_ej_ad,
        "cod": cod
    })
    print(f"Libro registrado con éxito. Código: {cod}")
    return None

def eliminar_ejemplar_libro():
    cod=(input("Ingrese el código del libro el cual quiere eliminar: ")) #Le pide al usuario que le ingrese el código del libro que quiere ingresar
    
    for libro in libros: #Se inicializa el 'for' para que busque en el diccionario los libros
        if libro["cod"] == cod and libro["cant_ej_ad"] > 0: #Si esta el código en el diccionario y hay mas o igual de 1 libro , se elimina el libro
            libros.remove(libro) #Se elimina el libro del diccionario
            print("Eliminado exitosamente") 
            return
    print("Eliminación fallida. Por favor, ingrese un código valido exitosamente")
    return None

def prestar_ejemplar_libro():
    cod= (input("Ingresar el código del libro que quiere gestionar: "))
    
    for libro in libros:
        if libros["cod"] in libros:
            print("Codigo")
        else: 
            print("No hay tal ejemplar")
    return None

def devolver_ejemplar_libro():
    Cod = (input("Ingresar el código del libro")) #Le pide al usuario que le ingrese el código del libro que quiere ingresar
    
    for libro in libros: #Se inicializa el 'for' para que busque en el diccionario los libros
        if libros["Codigo"] == Cod and libros["Cant_prestados"] >= 0: #Si no hay código repetido y hay mas o igual de 0 libro prestado, se devuelve el libro
            libros["Cant_prestados"] += 1 #Se sumenta la cantidad de prestados en el libro devuelto
            print("Devolución exitosa")
            return
    print("Devolución fallida. Por favor, ingrese un código válido nuevamente") #Si ya hay algun libro con el código ingresado o con la cantidad de prestados menor o igual a 0, da error
    return None

def nuevo_libro():
   libro: nuevo_libro()
   return libros
    return None
