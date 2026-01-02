#TODO: tentar fazer tudo a partir da leitura da entrada diretamente, linha por linha. se possivel -> menos espaco auxiliar
from functools import reduce

operacoes = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}


def solucao_1():
    with open('entrada.txt', 'r') as f:
        entrada = [linha.split() for linha in f.read().splitlines()]
    acc = [int(i) for i in entrada[0]]
    total_problemas = len(acc)

    for i in range(1, len(entrada) - 1):
        for k in range(total_problemas):
            operacao_func = operacoes[entrada[-1][k]]
            acc[k] = operacao_func(acc[k], int(entrada[i][k]))
    return sum(acc)


def get_numeros_coluna(numeros):
    quant_digitos = len(numeros[0])

    accs = [0] * quant_digitos
    for i in range(quant_digitos):
        multiplicador = 1
        for k in range(len(numeros)):
            numero = numeros[k]
            if numero[i] == ' ':
                continue
            accs[i] += (int(numero[i]) * multiplicador)
            multiplicador *= 10
    return accs

def parsear_entrada(entrada):
    tamanho_linha = len(entrada[0])
    delimitadores = []
    for i in range(tamanho_linha):
        if all(entrada[k][i] == ' ' for k in range(len(entrada) - 1)):
            delimitadores.append(i)
    operadores = entrada[-1].split()
    numeros = []
    for l in range(len(entrada) - 2, -1, -1):
        
        inicio_num = 0
        linha_nums = []
        for d in delimitadores:
            linha_nums.append(entrada[l][inicio_num: d])
            inicio_num = d + 1
        linha_nums.append(entrada[l][inicio_num:])
        numeros.append(linha_nums)

            
    return numeros, operadores
        


def solucao_2():
    with open('entrada.txt', 'r') as f:
        entrada = f.read().splitlines()

    numeros_linha, operadores = parsear_entrada(entrada)
    total_problemas = len(operadores)
    total = 0
    for j in range(total_problemas):
        numeros = [numeros_linha[k][j] for k in range(len(entrada) - 1)]
        numeros_col = get_numeros_coluna(numeros)
        total += reduce(operacoes[operadores[j]], numeros_col)
    return total


print(solucao_1())
print(solucao_2())
