def res():
	with open('entrada.txt', 'r') as f:
		baterias = [
			[int(d) for d in linha]
			for linha in f.read().splitlines()
		]
	total = 0
	for bateria in baterias:
		num = ''
		for i in range(11, -1, -1):
			tam = len(bateria)
			pedaco = bateria[:tam - i]
			n = max(pedaco)
			num += str(n)
			bateria = bateria[bateria.index(n) + 1:]
		total += int(num)
	return total

print(res())
