from itertools import combinations

def solucao_1(coordenadas):
    #bruteforcezao de cria
    retangulos = combinations(coordenadas, 2)

    maior = 0
    for coords in retangulos:
        dist_x = abs(coords[0][0] - coords[1][0] + 1)
        dist_y = abs(coords[0][1] - coords[1][1] + 1)
        maior = max(maior, dist_x * dist_y)
    print(maior)

def solucao_2(coordenadas):
    pass
    
if __name__ == '__main__':
    coordenadas = list(map(eval, open('entrada.txt')))

