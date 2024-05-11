import networkx as nx
import matplotlib.pyplot as plt
from clases import *

def visualizar_sistema(sistema, mejor_individuo, generacion, mejor_fitness):

    plt.title(f"Generación: {generacion}, Mejor Fitness: {mejor_fitness}")

    G = nx.DiGraph()

    for nodo in sistema.nodos:
        G.add_node(nodo.id)

    for arista in sistema.aristas:
        capacidad = arista.capacidad
        flujo = arista.flujo_vehiculos(mejor_individuo)
        G.add_edge(arista.nodo_origen.id, arista.nodo_destino.id, capacidad=capacidad, flujo=flujo)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)
    nx.draw_networkx_labels(G, pos)

    capacidades = nx.get_edge_attributes(G, 'capacidad')
    flujos = nx.get_edge_attributes(G, 'flujo')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=capacidades)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=flujos, label_pos=0.3)



    plt.axis('off')
    plt.show()