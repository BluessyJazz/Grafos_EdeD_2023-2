from grafo import Grafo

def mostrar_menu():
    print("\nMenú de opciones:")
    print("\033[1;34m1. Mostrar grafo\033[0m")
    print("\033[1;34m2. Ver ciudades conectadas\033[0m")
    print("\033[1;34m3. Mostrar información de un nodo\033[0m")
    print("\033[1;34m4. Calcular distancia entre ciudades\033[0m")
    print("\033[1;34m5. Calcular ruta más rápida entre ciudades\033[0m")
    print("\033[1;34m6. Salir\033[0m")

def opciones(opcion, grafo):
    if opcion == 1:
        print("\nGrafo:\n")
        grafo.mostrar_grafo()
    elif opcion == 2:
        ciudad1 = input("\033[1;35m\nIngrese la ciudad de origen: \033[0m").capitalize()
        ciudad2 = input("\033[1;35mIngrese la ciudad de destino: \033[0m").capitalize()
        grafo.ciudades_conectadas(ciudad1, ciudad2)
    elif opcion == 3:
        ciudad = input("\033[1;35m\nIngrese el nombre de la ciudad: \033[0m").capitalize()
        grafo.mostrar_nodo(ciudad)
    elif opcion == 4:
        ciudad1 = input("\033[1;35m\nIngrese la ciudad de origen: \033[0m").capitalize()
        ciudad2 = input("\033[1;35mIngrese la ciudad de destino: \033[0m").capitalize()
        grafo.calcular_distancia(ciudad1, ciudad2)
    elif opcion == 5:
        ciudad1 = input("\033[1;35m\nIngrese la ciudad de origen: \033[0m").capitalize()
        ciudad2 = input("\033[1;35mIngrese la ciudad de destino: \033[0m").capitalize()
        grafo.calcular_tiempo(ciudad1, ciudad2)
    elif opcion == 6:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

grafo = Grafo()
archivo_csv = "datos/Datos vias Colombia.csv"
grafo.cargar_desde_csv(archivo_csv)

while True:
    try:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        opciones(opcion, grafo)
    except ValueError:
        print("Error: Ingrese un número válido.")