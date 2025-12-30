with open('entrada.txt', 'r') as f:
    linhas = f.read().splitlines()

intervalos = [i.split('-') for i in linhas[:linhas.index('')]]
entradas = [int(i) for i in linhas[linhas.index('') + 1:]]

intervalos = [range(int(k[0]), int(k[1]) + 1) for k in intervalos]

def parte_1():
    return (sum((int(any(i in r for r in intervalos)) for i in entradas)))

def parte_2_tentativa1():
    uniao = set()
    for intervalo in intervalos:
        uniao = uniao.union(intervalo)
    return len(uniao)

def parte_2_tentativa2():
    partes_intervalos = [ [intervalo] for intervalo in intervalos ]
    for i in range(len(intervalos) - 1):
        for k in range(i + 1, len(intervalos)):
            novas_partes = []
            for parte in partes_intervalos[i]:
                intersec = range(
                            max(parte[0], intervalos[k][0]),
                            min(parte[-1], intervalos[k][-1]) + 1
                            )
                if len(intersec) == 0:
                    novas_partes.append(parte)
                    continue

                i1 = range(parte[0], intersec[0])
                i2 = range(intersec[-1] + 1, parte[-1] + 1)

                if len(i1) != 0:
                    novas_partes.append(i1)
                if len(i2) != 0:
                    novas_partes.append(i2)
            partes_intervalos[i] = novas_partes

    return sum(
                sum(
                (len(parte) for parte in partes)
                )
                for partes in partes_intervalos
            )
            

if __name__ == '__main__':
    #print(parte_2_tentativa1())
    print(parte_2_tentativa2())
        


