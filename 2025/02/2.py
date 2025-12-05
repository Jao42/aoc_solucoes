from math import log

with open('entrada.txt', 'r') as f:
	intervalos = [
		[int(i) for i in s.split('-')]
		for s in f.read().split(',')
		]

def get_divisores(valor):
	divisores = set()
	for i in range(1, int(valor ** (1/2) + 1)):
		if valor % i == 0:
			divisores.add(i)
			divisores.add(valor // i)
			
	return divisores

soma_invalidos = 0
for intervalo in intervalos:
	for i in range(intervalo[0], intervalo[1] + 1):
		tamanho = int(log(i, 10)) + 1
		divisores = get_divisores(tamanho)
		for divisor in divisores:
			partes = set(dividir_identificador(id_str, divisor))
			if divisor != tamanho and len(partes) == 1:
				soma_invalidos += i
				break
print(soma_invalidos)
	
