import os
import biblioteca

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")  # Limpiar pantalla
    if opt.isnumeric():
        if opt == "1":
            biblioteca.ejemplares_prestados()
        elif opt == "2":
            biblioteca.devolver_ejemplar_libro()
        elif opt == "3":
            biblioteca.registrar_nuevo_libro()
        elif opt == "4":
            biblioteca.eliminar_ejemplar_libro()
        elif opt == "5":
            biblioteca.mostrar_ejemplares_prestados()  # Supongo que esta función existe en tu módulo biblioteca
        elif opt == "6":
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")

    input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!.")
