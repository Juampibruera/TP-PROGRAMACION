# Trabajo Práctico I - Programación II


import os

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolucion")
    print("3 - Registrar nuevo libro")
    print("4 - Elimiar ejemplar")
    print("5 - Mostrar ejemplares perstados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            ejemplares_prestados()
            print(ejemplares_prestados)
        elif int(opt) == 2:
            devolver_ejemplar_libro()
            print(devolver_ejemplar_libro)
        elif int(opt) == 3:
            registrar_nuevo_libro()
            print(registrar_nuevo_libro)
        elif int(opt) == 4:
            eliminar_ejemplar_libro()
            print(eliminar_ejemplar_libro)
        elif int(opt) == 5:
            ejemplares_prestados()
            print(ejemplares_prestados)
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")

    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")
