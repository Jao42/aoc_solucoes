from functools import cache

with open('exemplo.txt', 'r') as f:
    linhas = f.read().splitlines()

total_linhas = len(linhas)
total_colunas = len(linhas[0])
inicio_pos = (linhas[0].find('S'), 0)
feijoes_pos = []

for i in range(total_colunas):
    feijoes = []
    for k in range(total_linhas):
        if linhas[k][i] == '^':
            feijoes.append(k)
    feijoes_pos.append(feijoes)
            
def encontrar_particao_pos(inicio_pos):
    x, y = inicio_pos
    feijoes = feijoes_pos[x]

    for f in feijoes:
        if f >= y:
            return (x, f)
    return ()

            
def solucao_1(posicoes, acc=0, particoes_pos=set()):
    if len(posicoes) == 0:
        return acc
    novas_posicoes = set()
    for posicao in posicoes:
        particao_pos = encontrar_particao_pos(posicao)
        if len(particao_pos) != 0 and (particao_pos not in particoes_pos):
            x, y = particao_pos
            acc += 1
            novas_posicoes.add(((x - 1, y)))
            novas_posicoes.add((x + 1, y))
            particoes_pos.add(particao_pos)
    return solucao_1(novas_posicoes, acc, particoes_pos)


def solucao_2(posicoes, acc=1):
    if len(posicoes) == 0:
        return acc
    novas_posicoes = {}
    for posicao, count in posicoes.items():
        particao_pos = encontrar_particao_pos(posicao)
        if len(particao_pos) != 0:
            acc += count
            x, y = particao_pos
            esq_pos = (x - 1, y) 
            dir_pos = (x + 1, y) 
            novas_posicoes[esq_pos] = novas_posicoes.get(esq_pos, 0) + count
            novas_posicoes[dir_pos] = novas_posicoes.get(dir_pos, 0) + count
    return solucao_2(novas_posicoes, acc)



print(solucao_1([inicio_pos]))
print(solucao_2({inicio_pos: 1}))
