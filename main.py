# Importando bibliotecas
import networkx as nx0
from pyvis.network import Network
import matplotlib.pyplot as plt

# Criando grafo
grafo = nx0.Graph()

# Adicionando nós
grafo.add_node(0)
grafo.add_node(1)
grafo.add_node(2)
grafo.add_node(3)
grafo.add_node(4)
grafo.add_node(5)
grafo.add_node(6)
grafo.add_node(7)

# Adicionando arestas
grafo.add_edge(0, 1, weight=24)
grafo.add_edge(0, 2, weight=4 )
grafo.add_edge(1, 3, weight=23)
grafo.add_edge(1, 4, weight=18)
grafo.add_edge(1, 5, weight=9 )
grafo.add_edge(2, 3, weight=6 )
grafo.add_edge(2, 6, weight=16)
grafo.add_edge(3, 4, weight=5 )
grafo.add_edge(3, 6, weight=8 )
grafo.add_edge(4, 5, weight=11)
grafo.add_edge(4, 6, weight=10)
grafo.add_edge(4, 7, weight=14)
grafo.add_edge(5, 7, weight=7 )
grafo.add_edge(6, 7, weight=21)

# Aplicando Algoritmo de Prim (para obtenção da Árvore Geradora Mínima (MST))
movimento_sem_terra = nx0.tree.minimum_spanning_edges(grafo, algorithm="prim", data=False)
arestas_mst = list(movimento_sem_terra)
