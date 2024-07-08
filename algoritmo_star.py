#import random
""" 
def crear_matriz(dimension):
    # Crear una matriz bidimensional
    matriz = []
    
    for a in range(1, dimension+1):
        fila = []
        for b in range(1, dimension+1):
            fila.append(0)  # Puedes inicializar cada celda con 0 u otro valor si lo prefieres
        matriz.append(fila)
    
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" " )
        print()  # Esto asegura que el cursor pase a una nueva línea después de imprimir la matriz completa

def agregarObstaculo(matriz, coordenada, tipo):
     
    x, y = coordenada

    ruta = {
        'camino':       0,
        'pasto':        1,
        'agua':         2,
        'edificio':     3,
    }
        
    if x >= 0 and x < len(matriz) and y >= 0 and y < len(matriz) and tipo in ruta.keys() and tipo != 'camino' and coordenada != inicio_y_fin():
        matriz[x][y] = ruta[tipo]
        imprimir_matriz(matriz)
    else:
        print("Lo ingresado no está dentro de las dimensiones de las coordenadas(matriz) o tu obstaculo no está dentro de los tipos: pasto, agua, edificio")

def inicio_y_fin(matriz, inicio, fin):

    x_inicio, y_inicio = inicio
    x_final, y_final = fin

    if x_inicio > 0 and x_inicio <= len(matriz) and y_inicio > 0 and y_inicio <= len(matriz) and \
    x_final > 0 and x_final <= len(matriz) and y_final > 0 and y_final <= len(matriz):
        
        matriz[x_inicio][y_inicio] = inicio
        matriz[x_final][y_final] = fin

        imprimir_matriz(matriz)

    else:
        print("Las coordenadas no son válidas")

# # Definir el tamaño de la matriz
dimension = 3

# # Crear y mostrar la matriz
matriz = crear_matriz(dimension)
imprimir_matriz(matriz)


# Solicitar al usuario ingresar coordenadas y tipo de obstáculo
usuario_input = input("Ingrese las coordenadas y el tipo de obstáculo (ej. '1,1 agua'): ")
coordenada_str, tipo = usuario_input.split()
coordenada = tuple(map(int, coordenada_str.split(',')))

coordenada = coordenada[0] - 1, coordenada[1] - 1

# Agregar el obstáculo ingresado por el usuario
agregarObstaculo(matriz, coordenada, tipo)
 """
 
import heapq

def crear_matriz(dimension):
    matriz = []
    for a in range(dimension):
        fila = []
        for b in range(dimension):
            fila.append(0)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end=" ")
        print()

def agregarObstaculo(matriz, coordenada, tipo):
    x, y = coordenada
    ruta = {
        'camino': 0,
        'pasto': 1,
        'agua': 2,
        'edificio': 3,
    }
    if x >= 0 and x < len(matriz) and y >= 0 and y < len(matriz[0]) and tipo in ruta.keys() and tipo != 'camino':
        matriz[x][y] = ruta[tipo]
        imprimir_matriz(matriz)
    else:
        print("Lo ingresado no está dentro de las dimensiones de las coordenadas (matriz) o tu obstáculo no está dentro de los tipos: pasto, agua, edificio")

def inicio_y_fin(matriz, inicio, fin):
    x_inicio, y_inicio = inicio
    x_final, y_final = fin
    if x_inicio >= 0 and x_inicio < len(matriz) and y_inicio >= 0 and y_inicio < len(matriz[0]) and \
       x_final >= 0 and x_final < len(matriz) and y_final >= 0 and y_final < len(matriz[0]):
        matriz[x_inicio][y_inicio] = 'I'
        matriz[x_final][y_final] = 'F'
        imprimir_matriz(matriz)
    else:
        print("Las coordenadas no son válidas")

def heuristica(a, b): # para calcular el costo estimado
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def vecinos(matriz, nodo):
    x, y = nodo
    candidatos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    resultados = []
    for cx, cy in candidatos:
        if 0 <= cx < len(matriz) and 0 <= cy < len(matriz[0]) and matriz[cx][cy] != 3:
            resultados.append((cx, cy))
    return resultados

def a_star(matriz, inicio, fin):
    nodos_abiertos = []
    heapq.heappush(nodos_abiertos, (0, inicio))
    origen = {}
    puntaje_g = {inicio: 0}
    puntaje_f = {inicio: heuristica(inicio, fin)}
    while nodos_abiertos:
        _, actual = heapq.heappop(nodos_abiertos)
        if actual == fin:
            camino_tomado = []
            while actual in origen:
                camino_tomado.append(actual)
                actual = origen[actual]
            camino_tomado.append(inicio)
            camino_tomado.reverse()
            return camino_tomado
        for vecino in vecinos(matriz, actual):
            tentivo_puntaje_g = puntaje_g[actual] + 1
            if vecino not in puntaje_g or tentivo_puntaje_g < puntaje_g[vecino]:
                origen[vecino] = actual
                puntaje_g[vecino] = tentivo_puntaje_g
                puntaje_f[vecino] = tentivo_puntaje_g + heuristica(vecino, fin)
                if vecino not in [i[1] for i in nodos_abiertos]:
                    heapq.heappush(nodos_abiertos, (puntaje_f[vecino], vecino))
    return []

def marcar_camino(matriz, camino):
    for x, y in camino:
        if matriz[x][y] == 0:
            matriz[x][y] = '*'

# Dimensión de la matriz
dimension = int(input("Ingrese la dimensión de la matriz: "))
matriz = crear_matriz(dimension)
imprimir_matriz(matriz)

# Coordenadas de inicio y fin
inicio_input = input("Ingrese las coordenadas de inicio (ej. '1,1'): ")
fin_input = input("Ingrese las coordenadas de fin (ej. '3,3'): ")

inicio = tuple(map(int, inicio_input.split(',')))
fin = tuple(map(int, fin_input.split(',')))

inicio = inicio[0] - 1, inicio[1] - 1
fin = fin[0] - 1, fin[1] - 1

inicio_y_fin(matriz, inicio, fin)

# Agregar obstáculos
num_obstaculos = int(input("Ingrese la cantidad de obstáculos: "))
for _ in range(num_obstaculos):
    obstaculo_input = input("Ingrese las coordenadas y el tipo de obstáculo (ej. '1,1 agua'): ")
    coordenada_str, tipo = obstaculo_input.split()
    coordenada = tuple(map(int, coordenada_str.split(',')))
    coordenada = coordenada[0] - 1, coordenada[1] - 1
    agregarObstaculo(matriz, coordenada, tipo)

# Ejecutar el algoritmo A*
camino = a_star(matriz, inicio, fin)
if camino:
    print("***********") # no estás segura, ve donde poner para que la matriz final(marcada)
    marcar_camino(matriz, camino)
    imprimir_matriz(matriz)
    print("El camino más corto es:")
    for paso in camino:
        print(paso)
else:
    print("No se encontró un camino.")
