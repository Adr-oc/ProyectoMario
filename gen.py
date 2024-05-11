import random

def generar_individuo(sistema):
    individuo = {}
    
    for nodo in sistema.nodos:
        aristas_salientes = [arista for arista in nodo.aristas if arista.nodo_origen == nodo]
        
        # Asignar porcentajes mínimos de paso
        porcentajes_minimos = [arista.porcentaje_minimo for arista in aristas_salientes]
        porcentaje_restante = 1 - sum(porcentajes_minimos)
        
        # Generar porcentajes aleatorios para el resto del flujo
        porcentajes_aleatorios = [random.random() for _ in range(len(aristas_salientes))]
        porcentajes_aleatorios = [p / sum(porcentajes_aleatorios) * porcentaje_restante for p in porcentajes_aleatorios]
        
        # Combinar porcentajes mínimos y aleatorios
        porcentajes = [p_min + p_rand for p_min, p_rand in zip(porcentajes_minimos, porcentajes_aleatorios)]
        
        # Asignar porcentajes a las aristas salientes
        for arista, porcentaje in zip(aristas_salientes, porcentajes):
            individuo[(nodo.id, arista.id, arista.nodo_destino.id)] = porcentaje
    
    return individuo


def evaluar_fitness(individuo, sistema, num_iteraciones):
    fitness = 0
    
    for _ in range(num_iteraciones):
        for arista in sistema.aristas:
            if arista.nodo_destino.id in [6, 7]:  # Nodos de salida
                vehiculos_salida = arista.flujo_vehiculos(individuo)
                fitness += vehiculos_salida
    
    return fitness

def seleccion_torneo(poblacion, tamaño_torneo):
    seleccionados = []
    for _ in range(len(poblacion)):
        torneo = random.sample(poblacion, tamaño_torneo)
        seleccionado = max(torneo, key=lambda x: x['fitness'])
        seleccionados.append(seleccionado)
    return seleccionados

def cruzar(padre1, padre2):
    if len(padre1) <= 1:
        return padre1, padre2
    
    # Cruce de un punto
    punto_cruce = random.randint(1, len(padre1) - 1)
    hijo1 = {**padre1.copy(), **{k: v for k, v in padre2.items() if k not in padre1}}
    hijo2 = {**padre2.copy(), **{k: v for k, v in padre1.items() if k not in padre2}}
    return hijo1, hijo2

def mutar(individuo, probabilidad_mutacion):
    # Mutación de un gen uniforme
    for key in individuo:
        if random.random() < probabilidad_mutacion:
            individuo[key] = random.random()
    return individuo


def algoritmo_genetico(sistema, tamaño_poblacion, num_generaciones, tamaño_torneo, probabilidad_mutacion, num_iteraciones):
    poblacion = [generar_individuo(sistema) for _ in range(tamaño_poblacion)]
    
    for generacion in range(num_generaciones):
        for individuo in poblacion:
            individuo['fitness'] = evaluar_fitness(individuo, sistema, num_iteraciones)
        
        poblacion.sort(key=lambda x: x['fitness'], reverse=True)
        mejor_fitness = poblacion[0]['fitness']
        
        print(f"Generación: {generacion+1}/{num_generaciones}, Mejor Fitness: {mejor_fitness}")
        
        padres = seleccion_torneo(poblacion, tamaño_torneo)
        
        nueva_poblacion = []
        for i in range(0, len(padres), 2):
            padre1, padre2 = padres[i], padres[i+1]
            hijo1, hijo2 = cruzar(padre1, padre2)
            hijo1 = mutar(hijo1, probabilidad_mutacion)
            hijo2 = mutar(hijo2, probabilidad_mutacion)
            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion
    
    mejor_individuo = max(poblacion, key=lambda x: x['fitness'])
    return mejor_individuo