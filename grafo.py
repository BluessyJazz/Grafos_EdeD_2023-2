# Instalar pandas e importarla como pd  (pip install pandas)    
import pandas as pd

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, ciudad1, ciudad2, distancia, tiempo):
        if ciudad1 not in self.grafo:
            self.grafo[ciudad1] = {}
        self.grafo[ciudad1][ciudad2] = (distancia, tiempo)

    def cargar_desde_csv(self, ruta_archivo):
        datos = pd.read_csv(ruta_archivo, sep='\t')
        for _, fila in datos.iterrows():
            ciudad1, ciudad2, distancia, tiempo = fila
            self.agregar_arista(ciudad1, ciudad2, distancia, tiempo)

grafo = Grafo()
grafo.cargar_desde_csv('datos/Datos vias Colombia.csv')