def contar_adjacencias(matriz, l, col):
	total = 0
	for k in range(-1, 2):
		for j in range(-1, 2):
			if (l + k) < 0 or (col + j) < 0:
				continue
			try:
				total += matriz[l + k][col + j]
			except IndexError:
				continue
	return total


def remover_papeis(matriz):
	count = 0
	acessiveis = []

	for l in range(len(matriz)):
		for col in range(len(matriz[0])):
			if not matriz[l][col]:
				continue
			total = contar_adjacencias(matriz, l, col)
			if total < 5:
				acessiveis.append((l, col))
				count += 1
	for x, y in acessiveis:
		matriz[x][y] = 0
	return matriz, count


with open('entrada.txt', 'r') as f:
	matriz = [
		[0 if i == '.' else 1 for i in linha]
		for linha in f.read().splitlines()
		]



total = 0
count = -1
while count != 0:
	matriz, count = remover_papeis(matriz)
	total += count
			
print(total)
