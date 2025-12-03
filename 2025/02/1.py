from math import log

with open('entrada.txt', 'r') as f:
	intervalos = [
		[int(i) for i in s.split('-')]
		for s in f.read().split(',')
		]


soma_invalidos = 0
for intervalo in intervalos:
	for i in range(intervalo[0], intervalo[1] + 1):
		tamanho = int(log(i, 10)) + 1
		if (tamanho % 2) != 0:
			continue
		mascara = 10 ** (tamanho // 2)
		if (i // mascara != i % mascara):
			continue
		soma_invalidos += i
print(soma_invalidos)
		
