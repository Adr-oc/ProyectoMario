from gen import *

class Nodo:
    def __init__(self, id):
        self.id = id
        self.aristas = []

    def agregar_arista(self, arista):
        self.aristas.append(arista)


class Arista:
    def __init__(self, id, nodo_origen, nodo_destino, direccion, capacidad, porcentaje_minimo=0):
        self.id = id
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.direccion = direccion
        self.capacidad = capacidad
        self.porcentaje_minimo = porcentaje_minimo
        
    def flujo_vehiculos(self, individuo):
        try:
            tiempo_paso = individuo[(self.nodo_origen.id, self.id, self.nodo_destino.id)]
            flujo = int(self.capacidad * tiempo_paso)
            return flujo
        except KeyError:
            # Manejar el caso cuando la clave no está presente en el individuo
            print(f"La clave ({self.nodo_origen.id}, {self.id}, {self.nodo_destino.id}) no está presente en el individuo.")
            return 0  # Retornar un valor por defecto o tomar alguna acción apropiada


class SistemaTransito:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def agregar_arista(self, arista):
        self.aristas.append(arista)

    def obtener_nodo(self, id):
        for nodo in self.nodos:
            if nodo.id == id:
                return nodo
        return None

    def obtener_arista(self, id):
        for arista in self.aristas:
            if arista.id == id:
                return arista
        return None