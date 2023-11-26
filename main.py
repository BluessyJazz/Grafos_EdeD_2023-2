from grafo import Grafo

grafo = Grafo()
grafo.cargar_desde_csv('datos/Datos vias Colombia.csv')
print("\nGrafo Cargado")
print("\nGrafo:\n")
grafo.mostrar_grafo()

ciudad1, ciudad2 = input("\nIngrese la ciudad de origen: "), input("Ingrese la ciudad de destino: ")

grafo.ciudades_conectadas(ciudad1, ciudad2)
grafo.mostrar_nodo(ciudad1)
grafo.mostrar_nodo(ciudad2)
grafo.calcular_distancia(ciudad1, ciudad2)
grafo.calcular_tiempo(ciudad1, ciudad2) 
# grafo.dijkstra(ciudad1, ciudad2)
