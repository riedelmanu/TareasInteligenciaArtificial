# Funcion objetivo 
def calcular_ataques(solucion):
    """Calcula el número de pares de reinas que se atacan"""
    ataques = 0
    for i in range(7):
        for j in range(i+1, 8):
            # Ataque en misma fila (imposible con nuestra representación)
            # Ataque en diagonal
            if abs(i - j) == abs(solucion[i] - solucion[j]):
                ataques += 1
    return ataques

# Funcion vecindario
def generar_vecinos(solucion):
    """Genera todos los vecinos intercambiando dos reinas"""
    vecinos = []
    for i in range(7):
        for j in range(i+1, 8):
            vecino = solucion.copy()
            vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambiamos dos reinas
            vecinos.append(vecino)
    return vecinos

# Implementacion completa
import random
from typing import List, Tuple

def generar_solucion_inicial() -> List[int]:
    """Genera una solución inicial aleatoria (permutación de 0-7)"""
    return random.sample(range(8), 8)

def busqueda_tabu(max_iter: int = 1000, tam_lista_tabu: int = 10) -> List[int]:
    """Implementación de búsqueda tabú para las 8 reinas"""
    
    # Inicialización
    solucion_actual = generar_solucion_inicial()
    mejor_solucion = solucion_actual.copy()
    valor_mejor = calcular_ataques(mejor_solucion)
    
    lista_tabu = []  # Almacena movimientos tabú (i,j)
    iter_sin_mejora = 0
    
    for iteracion in range(max_iter):
        if valor_mejor == 0:
            break  # Solución encontrada
        
        # Generar vecindario y evaluar
        vecinos = generar_vecinos(solucion_actual)
        mejor_vecino = None
        mejor_valor_vecino = float('inf')
        mejor_movimiento = None
        
        for vecino in vecinos:
            # Encontrar qué movimiento generó este vecino
            movimiento = None
            for i in range(8):
                if solucion_actual[i] != vecino[i]:
                    j = [k for k in range(8) if solucion_actual[k] == vecino[i]][0]
                    movimiento = tuple(sorted((i, j)))
                    break
            
            valor_vecino = calcular_ataques(vecino)
            
            # Criterio de aspiración: aceptar si es mejor que el mejor global
            if valor_vecino < valor_mejor:
                mejor_vecino = vecino
                mejor_valor_vecino = valor_vecino
                mejor_movimiento = movimiento
                break
            # O si no es tabú y es el mejor del vecindario
            elif (movimiento not in lista_tabu) and (valor_vecino < mejor_valor_vecino):
                mejor_vecino = vecino
                mejor_valor_vecino = valor_vecino
                mejor_movimiento = movimiento
        
        # Actualizar solución actual
        if mejor_vecino is not None:
            solucion_actual = mejor_vecino
            if mejor_movimiento:
                lista_tabu.append(mejor_movimiento)
                if len(lista_tabu) > tam_lista_tabu:
                    lista_tabu.pop(0)  # Mantener tamaño fijo
            
            # Actualizar mejor solución global
            if mejor_valor_vecino < valor_mejor:
                mejor_solucion = solucion_actual.copy()
                valor_mejor = mejor_valor_vecino
                iter_sin_mejora = 0
            else:
                iter_sin_mejora += 1
        else:
            # Todos los movimientos son tabú, reiniciamos
            solucion_actual = generar_solucion_inicial()
            lista_tabu = []
        
        # Mostrar progreso
        if iteracion % 50 == 0:
            print(f"Iteración {iteracion}, Ataques: {valor_mejor}")
    
    print(f"\nSolución encontrada en iteración {iteracion}:")
    print(mejor_solucion)
    print(f"Ataques: {calcular_ataques(mejor_solucion)}")
    
    return mejor_solucion

def imprimir_tablero(solucion: List[int]):
    """Imprime el tablero con las reinas"""
    for fila in range(8):
        linea = ""
        for col in range(8):
            if solucion[col] == fila:
                linea += "Q "
            else:
                linea += ". "
        print(linea)

# Ejecutar la búsqueda tabú
solucion = busqueda_tabu(max_iter=1000, tam_lista_tabu=15)
print("\nTablero solución:")
imprimir_tablero(solucion)
