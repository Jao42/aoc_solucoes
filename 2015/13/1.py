with open('entrada.txt', 'r') as f:
	entrada = f.read().splitlines()


def parsear_entrada(entrada):
	resultado = {'felicidades': {}, 'integrantes': set()}
	for linha in entrada:
		termos = linha.split()
		pessoa1 = termos[0]
		pessoa2 = termos[-1][:-1]
		chave = (pessoa1, pessoa2)
		resultado['integrantes'].add(pessoa1)
		resultado['integrantes'].add(pessoa2)
		felicidade = int(termos[3])
		if termos[2] == 'lose':
			felicidade *= -1
		resultado['felicidades'][chave] = felicidade
	return resultado


def gerar_permutacoes(integrantes):
	permutacoes = set()
	if len(integrantes) == 0:
		return permutacoes
	for i in integrantes:
		sub_perm = gerar_permutacoes(integrantes - set([i]))
		if not sub_perm:
			return ((i,),)
		for sub in sub_perm:
			permutacoes.add((i,) + sub)
	return permutacoes


def gerar_permutacoes_adjacencias(permutacoes):
	perms_adjacencias = []
	for perm in permutacoes:
		perm_adjacencias = set()
		tamanho_perm = len(perm)
		for j in range(tamanho_perm):
			num = perm[j]
			anterior = perm[(j + 1) % tamanho_perm]
			sucessor = perm[(j - 1) % tamanho_perm]
			perm_adjacencias.add((num, anterior))
			perm_adjacencias.add((num, sucessor))
		perms_adjacencias.append(perm_adjacencias)
	return set(frozenset(n) for n in perms_adjacencias)


res = parsear_entrada(entrada)
perms = gerar_permutacoes(res['integrantes'])
perms_adjacencias = (gerar_permutacoes_adjacencias(perms))

maior = 0
for perm in perms_adjacencias:
	count = 0
	for adj in perm:
		count += res['felicidades'][adj]
	if count > maior:
		maior = count

print(maior)

