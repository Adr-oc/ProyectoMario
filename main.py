from clases import *
from gen import *
from vista import *

def main():
    # Crear nodos
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)
    nodo6 = Nodo(6)

    sistema = SistemaTransito()

    # Agregar nodos al sistema
    sistema.agregar_nodo(nodo1)
    sistema.agregar_nodo(nodo2)
    sistema.agregar_nodo(nodo3)
    sistema.agregar_nodo(nodo4)
    sistema.agregar_nodo(nodo5)
    sistema.agregar_nodo(nodo6)

    # Crear aristas y agregarlas al sistema y a los nodos correspondientes
    arista1 = Arista(1, nodo1, nodo2, "bidireccional", 50, porcentaje_minimo=0.2)
    sistema.agregar_arista(arista1)
    nodo1.agregar_arista(arista1)
    nodo2.agregar_arista(arista1)

    arista2 = Arista(2, nodo1, nodo3, "bidireccional", 30, porcentaje_minimo=0.1)
    sistema.agregar_arista(arista2)
    nodo1.agregar_arista(arista2)
    nodo3.agregar_arista(arista2)

    arista3 = Arista(3, nodo2, nodo4, "bidireccional", 40)
    sistema.agregar_arista(arista3)
    nodo2.agregar_arista(arista3)
    nodo4.agregar_arista(arista3)

    arista4 = Arista(4, nodo3, nodo5, "bidireccional", 20)
    sistema.agregar_arista(arista4)
    nodo3.agregar_arista(arista4)
    nodo5.agregar_arista(arista4)

    arista5 = Arista(5, nodo4, nodo6, "bidireccional", 60)
    sistema.agregar_arista(arista5)
    nodo4.agregar_arista(arista5)
    nodo6.agregar_arista(arista5)

    arista6 = Arista(6, nodo5, nodo6, "bidireccional", 70)
    sistema.agregar_arista(arista6)
    nodo5.agregar_arista(arista6)
    nodo6.agregar_arista(arista6)

    # Crear el nodo de salida
    nodo7 = Nodo(7)
    sistema.agregar_nodo(nodo7)

    # Crear las aristas de salida y agregarlas al sistema y a los nodos correspondientes
    arista7 = Arista(7, nodo5, nodo7, "unidireccional", 80)
    sistema.agregar_arista(arista7)
    nodo5.agregar_arista(arista7)
    nodo7.agregar_arista(arista7)

    arista8 = Arista(8, nodo6, nodo7, "unidireccional", 90)
    sistema.agregar_arista(arista8)
    nodo6.agregar_arista(arista8)
    nodo7.agregar_arista(arista8)

    tamaño_poblacion = 100
    num_generaciones = 100
    tamaño_torneo = 5
    probabilidad_mutacion = 0.1
    num_iteraciones = 10

    mejor_individuo = algoritmo_genetico(sistema, tamaño_poblacion, num_generaciones, tamaño_torneo, probabilidad_mutacion, num_iteraciones)
    visualizar_sistema(sistema, mejor_individuo, num_generaciones, mejor_individuo['fitness'])

if __name__ == "__main__":
    main()