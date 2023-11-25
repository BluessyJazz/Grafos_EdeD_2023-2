# Instalar pandas e importarla como pd  (pip install pandas)    
import pandas as pd
import pprint

class Grafo:
    """
    Clase que representa un grafo.

    Por qué una lista de adyaencia y no una matriz de adyacencia?
    - La lista de adyacencia es más eficiente en términos de memoria.
    - La lista de adyacencia es más eficiente en términos de tiempo para grafos dispersos.
    - La lista de adyacencia es más fácil de implementar en la mayoría de los casos.

    Por qué un diccionario y no una lista?
    - Para poder agregar aristas de forma eficiente.
    - Para poder buscar aristas de forma eficiente.
    - Para poder eliminar aristas de forma eficiente.

    Es un grafo dirigido, ya que las aristas tienen una dirección.
    Es un grafo ponderado, ya que las aristas tienen un pesos.

    Atributos:
    - grafo: Diccionario que almacena las aristas del grafo.
    """

    def __init__(self):
        self.grafo = {}

    def __str__(self):
        return str(self.grafo)

    def agregar_arista(self, ciudad1, ciudad2, distancia, tiempo):
        """
        Agrega una arista al grafo.

        Parámetros:
        - ciudad1: Ciudad de origen.
        - ciudad2: Ciudad de destino.
        - distancia: Distancia entre las ciudades.
        - tiempo: Tiempo de viaje entre las ciudades.
        """
        if ciudad1 not in self.grafo:
            self.grafo[ciudad1] = {}
        self.grafo[ciudad1][ciudad2] = (distancia, tiempo)

    def cargar_desde_csv(self, ruta_archivo):
        """
        Carga las aristas del grafo desde un archivo CSV.

        Parámetros:
        - ruta_archivo: Ruta del archivo CSV.
        """
        datos = pd.read_csv(ruta_archivo, sep=',')
        for _, fila in datos.iterrows():
            ciudad1, ciudad2, distancia, tiempo = fila
            self.agregar_arista(ciudad1, ciudad2, distancia, tiempo)

    def mostrar_grafo(self):
        """
        Muestra la información del grafo como una lista de adyacencia.
        """
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.grafo)

    def ciudades_conectadas(self, ciudad1, ciudad2):
        """
        Determina si la ciudad A y B están conectadas por una única carretera.

        Parámetros:
        - ciudad1: Ciudad de origen.
        - ciudad2: Ciudad de destino.
        """
        if ciudad1 in self.grafo:
            if ciudad2 in self.grafo[ciudad1]:
                print(f"\nLas ciudades de {ciudad1} y {ciudad2} están conectadas por una única carretera")
            else:
                print(f"\nLas ciudades de {ciudad1} y {ciudad2} no están conectadas por una única carretera")
        else:
            print(f"\nLas ciudades de {ciudad1} y {ciudad2} no están conectadas por una única carretera")