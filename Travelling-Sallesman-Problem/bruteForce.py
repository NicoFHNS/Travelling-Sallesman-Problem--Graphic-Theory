# Implementando o algoritmo Força Bruta
from itertools import *

def GerarCaminho(Values):
    # Recebendo as posições de todas as cidades da matriz informada
    Cidades = [node for node in range(len(Values))]

    # Removendo a ultima cidade para não gerar permutações com ciclos
    ultima_cidade = Cidades.pop()

    # Recebendo todas as permutações possiveis 
    Permutations = list(permutations(Cidades))
    
    # Gerando uma arvore a partir da minha lista de permutações
    Arvore = list(map(list, Permutations))
  
    # Finalizando o ciclo adicionando a ultima cidade
    for caminhos in Arvore:
        caminhos.append(ultima_cidade)
        caminhos.append(caminhos[0])
  
    return Cidades, Arvore

def ForcaBruta(Values):
    
    # Gerando todos os possiveis caminhos
    Cidades, Arvores = GerarCaminho(Values)
    
    # Calculando o custo de cada ciclo
    ListaDeCusto = []
    for ciclo in Arvores:
        # Inicia o custo para cada ciclo
        CustoPorCiclo = 0
        # Converte cada 2 nós de um ciclo em um índice na lista definida
        for index in range(0,(len(Cidades)-1)):
            # O CustoPorCiclo é calculado a partir da matriz definida a cada 2 nós do ciclo
            CustoPorCiclo = CustoPorCiclo + Values[ciclo[index]][ciclo[index+1]]
        ListaDeCusto.append(CustoPorCiclo)
    
    # Calculando o ciclo menos custoso
    MenosCustoso = min(ListaDeCusto)
    MenosCustosoIndex = ListaDeCusto.index(MenosCustoso)
    
   

    Values = ["Forca Bruta:", MenosCustoso, Arvores[MenosCustosoIndex]]
    
    return(Values)

Matriz =  [[0.0, 27.0, 12.1, 17.7, 11.0, 29.2, 22.4],
        [27.0, 0.0, 16.8, 11.2, 29.2, 11.0, 31.8],
        [12.1, 16.8, 0.0, 6.0, 12.5, 17.1, 27.9],
        [17.7, 11.2, 6.0, 0.0, 18.0, 11.7, 30.0],
        [11.0, 29.2, 12.5, 18.0, 0.0, 27.0, 33.2],
        [29.2, 11.0, 17.1, 11.7, 27.0, 0.0, 40.2],
        [22.4, 31.8, 27.9, 30.0, 33.2, 40.2, 0.0]]

print(ForcaBruta(Matriz))
