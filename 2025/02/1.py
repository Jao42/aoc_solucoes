with open('entrada.txt', 'r') as f:
	intervalos = [
		[int(i) for i in s.split('-')]
		for s in f.read().split(',')
		]


soma_invalidos = 0
for intervalo in intervalos:
	for i in range(intervalo[0], intervalo[1] + 1):
		id_str = str(i)
		tamanho = len(id_str)
		if (
		(tamanho % 2 != 0) or
		id_str[0:tamanho // 2] != id_str[tamanho // 2: tamanho]
		):
			continue
		soma_invalidos += i
print(soma_invalidos)
		
