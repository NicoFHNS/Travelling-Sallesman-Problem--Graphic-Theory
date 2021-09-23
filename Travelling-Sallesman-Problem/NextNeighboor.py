import sys

def nearestNeighbor(matrix, source):

    # escolhe um vértice arbitrário como vértice atual
    verticeAtual = source

    # descobre a aresta de menor peso que seja conectada ao vértice atual e a um vértice não visitado V
    distanciaProximo = sys.maxsize
    proximoVertice = 0
    verticeVisitado = []
    lenPath = 0
    distanciaArray = []

    while lenPath < (len(matrix[0])-1):
        for i in range(len(matrix[0])):
            if verticeAtual != i and i not in verticeVisitado:
                if distanciaProximo > float(matrix[verticeAtual][i]):
                    distanciaProximo = float(matrix[verticeAtual][i])
                    proximoVertice = i

        # faz o vértice atual ser marcado como V
        V = verticeAtual
        verticeAtual = proximoVertice

        # marca o v[ertice V como visitado.
        verticeVisitado.append(V)

        # caso todos os vértices no domínio foram visitados encerre o algoritmo
        if lenPath == len(matrix[0]):

            break
        # se não volte ao inicio e desscubra o menor peso da aresta
        else:
            lenPath += 1
            distanciaArray.append(distanciaProximo)
            distanciaProximo = sys.maxsize

    distanceLastToSource = float(matrix[verticeVisitado[0]][proximoVertice])
                                  
    distanciaArray.append(distanceLastToSource)
    verticeVisitado.append(proximoVertice)                             
    verticeVisitado.append(verticeVisitado[0])

    return [sum(distanciaArray), verticeVisitado]

    # print('Menor custo =>', sum(distanciaArray), '\n')
    # print('Melhor caminho =>', verticeVisitado)

import numpy as np
matrix = np.array()

nearestNeighbor(matrix, source=0)