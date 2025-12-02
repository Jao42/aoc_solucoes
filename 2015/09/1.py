with open('1.txt', 'r') as f:
    strings = f.read().splitlines()

cidades = set()
distancias = {}
for s in strings:
    print(s)
    cidades_str, distancia = s.split(' = ')
    distancia = int(distancia)
    cidades_dist = cidades_str.split(' to ')
    cidades = cidades.union(set(cidades_dist))
    distancias[tuple(cidades_dist)] = distancia
    distancias[tuple(cidades_dist[::-1])] = distancia


def get_permutacoes(iteravel):
    perms = []
    if len(iteravel) == 1:
        a = [ [next(iter(iteravel))] ]
        return a
    for i in iteravel:
        sub_perm = get_permutacoes(set(iteravel) - {i,})
        for j in sub_perm:
            perms.append([i] + j)
    return perms


def get_caminhos(perms):
    caminhos = []
    for perm in perms:
        caminhos.append(list(zip(perm[:-1], perm[1:])))
    return caminhos


perms = get_permutacoes(cidades)
caminhos = get_caminhos(perms)
maior_caminho = 0
for caminho in caminhos:
    dist_total = 0
    for rota in caminho:
        dist = distancias.get(rota)
        if dist is None:
            dist_total = maior_caminho
            break
        dist_total += dist
    if dist_total > maior_caminho:
        maior_caminho = dist_total

print(maior_caminho)



