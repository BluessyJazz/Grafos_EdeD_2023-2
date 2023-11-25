from grafo import Grafo

grafo = Grafo()
grafo.cargar_desde_csv('datos/Datos vias Colombia.csv')
print("\nGrafo Cargado")
print("\nGrafo:\n")
grafo.mostrar_grafo()

ciudad1, ciudad2 = input("\nIngrese la ciudad de origen: "), input("Ingrese la ciudad de destino: ")

grafo.ciudades_conectadas(ciudad1, ciudad2)