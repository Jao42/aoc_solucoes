with open('entrada.txt', 'r') as f:
	entrada = f.read().splitlines()

def parsear(linha):
	linha_dividida = linha.split()
	velocidade = int(linha_dividida[3])
	correndo_tempo = int(linha_dividida[6])
	descansando_tempo = int(linha_dividida[-2])
	return [velocidade, correndo_tempo, descansando_tempo]

corredores = []
for linha in entrada:
	corredores.append(parsear(linha))

maior = 0
tempo = 2503

corredores_estado = [corredor[1:] + [ 0, 0, 0 ] for corredor in corredores]
maior = 0
for seg in range(tempo):
	for i in range(len(corredores)):
		corredor = corredores[i]
		estado_atual = corredores_estado[i]
		ponteiro = estado_atual[4]
		estado_atual[ponteiro] -= 1

		if ponteiro == 0:
			estado_atual[2] += corredor[0]
		if estado_atual[ponteiro] == 0:
			estado_atual[ponteiro] = corredor[ponteiro + 1]
			estado_atual[4] = (ponteiro + 1) % 2

		maior = max(maior, estado_atual[2])
	for i in range(len(corredores)):
		estado_atual = corredores_estado[i]
		if maior == estado_atual[2]:
			estado_atual[3] += 1
	
print(max(c[3] for c in corredores_estado))
