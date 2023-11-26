# Instalar pandas e importarla como pd  (pip install pandas)    
import pandas as pd
import pprint
import heapq

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

    def mostrar_nodo(self, ciudad):
        """
        Muestra la información de un nodo del grafo.

        Parámetros:
        - ciudad: Ciudad del nodo.
        """
        if ciudad not in self.grafo:
            print(f"\nLa ciudad de {ciudad} no existe en el grafo")
            return None
        else:
            vecinos = self.obtener_vecinos(ciudad)
            print(f"\nCiudad: {ciudad}")
            print(f"Conexiones: {vecinos}")

    def obtener_vecinos(self, nodo):
        if nodo in self.grafo:
            return self.grafo[nodo]
        else:
            return None

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

    # Justificación de la implementación de Dijkstra
    '''
    - Se usará el método de Dijkstra para encontrar la ruta más corta entre dos ciudades
        ya que es eficiente y efectivo para grafos ponderados con pesos no negativos.
    - No se usa Bellman-Ford porque es más lento que Dijkstra aunque es más versátil ya que puede manejar pesos negativos.
    - Floyd-Warshall no es eficiente para grafos grandes. Su complejidad es O(V^3) donde V es el número de vértices.
        se puede usar para encontrar la ruta más corta entre todos los pares de vértices. 
        Solo necesitamos encontrar la ruta más corta entre dos ciudades.
    - Johnson es útil para grafos dispersos. Pero no es tan eficiente como Dijkstra.
    '''

    def dijkstra(self, inicio, fin, peso):
        """
        Aplica el algoritmo de Dijkstra para encontrar el camino más corto desde el nodo de inicio hasta el nodo de destino en el grafo.

        Args:
            inicio: El nodo de inicio del camino.
            fin: El nodo de destino del camino.
            peso: La función para obtener el peso de las aristas. Puede ser obtener_distancia o obtener_tiempo.

        Returns:
            Una tupla que contiene el camino más corto desde el nodo de inicio hasta el nodo de destino y el peso total del camino.
            Si no hay un camino válido, retorna None.
        """
        cola = [(0, inicio)]  # Cola de prioridad para almacenar los nodos a visitar
        visitados = set()  # Conjunto de nodos visitados
        pesos = {inicio: 0}  # Diccionario para almacenar las distancias mínimas desde el nodo de inicio
        previos = {inicio: None}  # Diccionario para almacenar los nodos previos en el camino más corto

        while cola:
            (dist, actual) = heapq.heappop(cola)  # Obtener el nodo actual de la cola de prioridad
            if actual not in visitados:
                visitados.add(actual)  # Marcar el nodo actual como visitado
                if actual == fin:
                    camino = []
                    peso_total = dist
                    while previos[actual] is not None:
                        camino.insert(0, actual)  # Insertar el nodo actual al inicio del camino
                        actual = previos[actual]  # Actualizar el nodo actual al nodo previo
                    camino.insert(0, inicio)  # Insertar el nodo de inicio al inicio del camino
                    return camino, peso_total  # Retornar el camino más corto y el peso total encontrado


                # Recorrer los nodos adyacentes al nodo actual
                vecinos = self.obtener_vecinos(actual)
                if vecinos is not None:
                    for vecino in vecinos:
                        if peso == "km":
                            peso_actual = self.obtener_distancia(actual, vecino)
                        elif peso == "tiempo":
                            peso_actual = self.obtener_tiempo(actual, vecino)
                        # Calcular el peso acumulado desde el nodo de inicio hasta el nodo vecino
                        peso_acumulado = dist + peso_actual
                        # Actualizar el peso mínimo si es menor al peso almacenado previamente
                        if vecino not in pesos or peso_acumulado < pesos[vecino]:
                            pesos[vecino] = peso_acumulado
                            previos[vecino] = actual
                            heapq.heappush(cola, (peso_acumulado, vecino))

        return None  # Si no se encuentra un camino válido, retornar None
    
    def obtener_tiempo(self, ciudad1, ciudad2):
        """
        Obtiene el tiempo de viaje entre dos ciudades.

        Parámetros:
        - ciudad1: Ciudad de origen.
        - ciudad2: Ciudad de destino.

        Returns:
        El tiempo de viaje entre las ciudades. Si no existe una conexión entre las ciudades, retorna None.
        """
        if ciudad1 in self.grafo and ciudad2 in self.grafo[ciudad1]:
            return self.grafo[ciudad1][ciudad2][1]
        else:
            return None

    def obtener_distancia(self, ciudad1, ciudad2):
        """
        Obtiene la distancia entre dos ciudades.

        Parámetros:
        - ciudad1: Ciudad de origen.
        - ciudad2: Ciudad de destino.

        Returns:
        La distancia entre las ciudades. Si no existe una conexión entre las ciudades, retorna None.
        """
        if ciudad1 in self.grafo and ciudad2 in self.grafo[ciudad1]:
            return self.grafo[ciudad1][ciudad2][0]
        else:
            return None
        
    def calcular_distancia(self, ciudad1, ciudad2):
        camino = self.dijkstra(ciudad1, ciudad2, 'km')
        

        if camino is not None:
            distancia = self.obtener_distancia(ciudad1, ciudad2)
            print(f"\nEl camino más corto entre {ciudad1} y {ciudad2} es: {camino[0]}\nLa distancia es: {camino[1]} km")
        else:
            print(f"\nNo existe un camino válido entre {ciudad1} y {ciudad2}")

    def calcular_tiempo(self, ciudad1, ciudad2):
        camino = self.dijkstra(ciudad1, ciudad2, 'tiempo')
        if camino is not None:
            tiempo = self.obtener_tiempo(ciudad1, ciudad2)
            print(f"\nEl camino más corto entre {ciudad1} y {ciudad2} es: {camino[0]}\nEl tiempo es: {camino[1]} horas")
        else:
            print(f"\nNo existe un camino válido entre {ciudad1} y {ciudad2}")

        
