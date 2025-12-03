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

def dividir_identificador(identificador, divisor):
	partes = []
	for i in range(0, len(identificador), divisor):
		partes.append(identificador[i:i + divisor])
	return partes

soma_invalidos = 0
for intervalo in intervalos:
	for i in range(intervalo[0], intervalo[1] + 1):
		id_str = str(i)
		tamanho = len(id_str)
		divisores = get_divisores(tamanho)
		for divisor in divisores:
			partes = set(dividir_identificador(id_str, divisor))
			if divisor != tamanho and len(partes) == 1:
				soma_invalidos += i
				break
print(soma_invalidos)
	
