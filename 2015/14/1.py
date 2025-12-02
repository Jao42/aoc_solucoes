with open('entrada.txt', 'r') as f:
	entrada = f.read().splitlines()

def parsear(linha):
	linha_dividida = linha.split()
	velocidade = int(linha_dividida[3])
	correndo_tempo = int(linha_dividida[6])
	descansando_tempo = int(linha_dividida[-2])
	return (velocidade, correndo_tempo, descansando_tempo)

corredores = []
for linha in entrada:
	corredores.append(parsear(linha))

maior = 0
tempo = 2503
for corredor in corredores:
	voltas, resto = divmod(tempo, corredor[1] + corredor[2])
	distancia = voltas * corredor[1] * corredor[0]
	print(distancia)
	if resto > corredor[1]:
		resto = corredor[1]
	distancia += resto * corredor[0]
	if distancia > maior:
		maior = distancia
print(maior)

	
