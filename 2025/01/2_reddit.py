fatores_direcoes = {'R': 1, 'L': -1}

with open('entrada.txt', 'r') as f:
  entrada = [
	(fatores_direcoes[linha[0]], int(linha[1:]))
	for linha in f.read().splitlines()
  ]

posicao = 50
cont = 0

for direcao, cliques in entrada:
	reflexao = (posicao * direcao) % 100 + cliques
	cont += reflexao // 100
	posicao = (reflexao * direcao) % 100

print(cont)
