class ConjuntosDisjuntos:
    def __init__(self, n:int):
        self.ancestrais = [i for i in range(n)]
        self.tamanhos = [1 for i in range(n)]

    def unir(self, a, b):
        raiz_a = self.find(a)
        raiz_b = self.find(b)
        if raiz_a == raiz_b:
            return 0
        self.ancestrais[raiz_a] = raiz_b
        self.tamanhos[raiz_b] += self.tamanhos[raiz_a]

    def eh_representante(self, i):
        return i == self.ancestrais[i]

    def find(self, i):
        if self.eh_representante(i):
            return i
        pai = self.ancestrais[i]
        return self.find(pai)


class Ponto:
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
            (
            (self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2
            ) ** (1/2)
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

DSU/UnionFind -> parece ser a solucao
"""

#10 -> (n) * (n - 1)/2
#   -> (n**2 - n)/2
def get_distancias_ordenadas(pontos):
    distancias = []
    for i in range(len(pontos) - 1):
        for k in range(i + 1, len(pontos)):
            dist = (pontos[i].dist(pontos[k]), i, k)
            distancias.append(dist)
    return sorted(distancias)
            

def solucao_1():
    distancias = get_distancias_ordenadas(pontos)
    conjuntos = ConjuntosDisjuntos(1000)
    for i in range(1000):
        _, idx_ponto_1, idx_ponto_2 = distancias[i]
        conjuntos.unir(idx_ponto_1, idx_ponto_2)
    top_3 = sorted(
            [ conjuntos.tamanhos[i] if conjuntos.eh_representante(i) else 0 for i in range(len(conjuntos.tamanhos)) ],
            reverse=True
            )[:3]
    total = 1
    for tam in top_3:
        total *= tam
    return total


def solucao_2():
    def tem_unico_ancestral(conjuntos):
        quant_repr = 0
        for i in range(len(conjuntos.ancestrais)):
            quant_repr += conjuntos.eh_representante(i)
            if quant_repr > 1:
                return False
        return True

    distancias = get_distancias_ordenadas(pontos)
    conjuntos = ConjuntosDisjuntos(len(pontos))
    for _, idx_ponto_1, idx_ponto_2 in distancias:
        conjuntos.unir(idx_ponto_1, idx_ponto_2)
        if not tem_unico_ancestral(conjuntos):
            continue
        return (pontos[idx_ponto_1].x * pontos[idx_ponto_2].x)
 

if __name__ == '__main__':
    with open('entrada.txt', 'r') as f:
        entrada = f.read().splitlines()
        pontos = []
        for l in entrada:
            pontos.append(Ponto(*(int(i) for i in l.split(','))))
        print(solucao_1())
        print(solucao_2())

