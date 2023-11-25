from grafo import Grafo

grafo = Grafo()
grafo.cargar_desde_csv('datos/Datos vias Colombia.csv')
print("\nGrafo Cargado")
print("\nGrafo:\n")
grafo.mostrar_grafo()
print("\nLista de Adyacencia:\n")
grafo.mostrar_adyacencia()
print("\nLista de Adyacencia de forma estética:\n")
grafo.mostrar_adyacenciapp()