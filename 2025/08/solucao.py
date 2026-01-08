from math import sqrt

class Ponto():
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.circuito = {self, }

    def __repr__(self):
        return f"Ponto({self.x}, {self.y}, {self.z})"

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y and self.z == p.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))
        
    def dist(self, p) -> float:
        return (
            sqrt(
            (self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2
            )
        )


"""
A gente tem que criar
uma classe(?) para capturar o estado dos circuitos

PERGUNTAS:
qual tipo de dado usar por baixo?

RESPOSTAS:
1.1 acho que um hashmap e ordenacao funcionaria.
tipo, ter uma funcao de mesclar os circuitos...
1.2 ou, só ter o circuito como uma propriedade de cada nó e na contagem ter um set
para evitar a contagem n-upla. assim o circuito tambem pode ser um set(facilitaria a insercao tb).

n deu certo, tem que ser uma estrutura compartilhada mesmo

n deu certo de novo, gerenciar estado e muito dificil

teria como fazer sem a redundancia? TODO
"""

        
def menor_distancia(p: Ponto, pontos_comp: list) -> Ponto:
    menor_dist = p.dist(pontos_comp[0])
    ponto_menor_dist = pontos_comp[0]
    for i in range(1, len(pontos)):
        ponto_atual = pontos_comp[i]
        dist_atual = p.dist(ponto_atual)
        if dist_atual < menor_dist:
            menor_dist = dist_atual
            ponto_menor_dist = ponto_atual
    return ponto_menor_dist
        
#10 -> (n) * (n - 1)/2
#   -> (n**2 - n)/2
def get_distancias_ordenadas(pontos):
    distancias = []
    for i in range(len(pontos) - 1):
        for k in range(i + 1, len(pontos)):
            dist = (pontos[i].dist(pontos[k]), pontos[i], pontos[k])
            distancias.append(dist)
    return sorted(distancias)
            

def conectar_circuitos(ponto_1, ponto_2) -> int:
    if ponto_1 in ponto_2.circuito:
        return ponto_1.circuito

    for ponto in ponto_2.circuito:
        ponto_1.circuito.add(ponto)
    for ponto in ponto_1.circuito:
        ponto.circuito = ponto_1.circuito

    return ponto_1.circuito
 

def get_todos_circuitos(pontos):
    pontos_circuitos = set()
    circuitos = []
    for ponto in pontos:
        if ponto in pontos_circuitos:
            continue
        circuitos.append(ponto.circuito)
        pontos_circuitos |= ponto.circuito
    return sorted(circuitos, key=len, reverse=True)

def solucao_1():
    distancias = get_distancias_ordenadas(pontos)
    for i in range(1000):
        _, ponto_1, ponto_2 = distancias[i]
        conectar_circuitos(ponto_1, ponto_2)
    circuitos = get_todos_circuitos(pontos)
    total = 1
    for i in range(3):
        total *= len(circuitos[i])
    return total

def solucao_2():
    distancias = get_distancias_ordenadas(pontos)
    for _, ponto_1, ponto_2 in distancias:
        circuito = conectar_circuitos(ponto_1, ponto_2)
        circuitos = get_todos_circuitos(pontos)
        if len(circuitos) == 1:
            return (ponto_1.x * ponto_2.x)
 

if __name__ == '__main__':
    with open('entrada.txt', 'r') as f:
        entrada = f.read().splitlines()
        pontos = []
        for l in entrada:
            pontos.append(Ponto(*(int(i) for i in l.split(','))))
        print(solucao_1())
        print(solucao_2())


      
