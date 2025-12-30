from math import log

#https://github.com/jimm89/AdventOfCode2025/blob/main/Day%202/Day%202.ipynb


def soma_intervalo(n, m):
	def soma_pa(p):
		return ((1 + p) * p) // 2
	return soma_pa(m) - soma_pa(n - 1)


def get_min_max_intervalo(inicio, fim, mascara):
	inicio_tam = mascara // 10
	fim_tam = mascara - 1
	min_ = inicio_tam
	max_ = fim_tam 
	pi = inicio // mascara
	pf = fim // mascara
	min_ = pi + ((pi * (mascara + 1)) < inicio) if pi > inicio_tam else inicio_tam
	max_ = pf - ((pf * (mascara + 1)) > fim) if pf < fim_tam else fim_tam 
	return (min_, max_)
	


with open('entrada.txt', 'r') as f:
	intervalos = [
		[int(i) for i in s.split('-')]
		for s in f.read().split(',')
		]


soma_invalidos = 0
for inicio, fim in intervalos:
	t0 = int(log(inicio, 10)) + 1
	t1 = int(log(fim, 10)) + 1
	t0 += t0 % 2
	for t in range(t0, t1 + 1, 2):
		mascara = 10 ** (t // 2)
		min_, max_ = get_min_max_intervalo(
				inicio, fim, mascara
				)
		soma_invalidos += soma_intervalo(min_, max_) * (mascara + 1)
print(soma_invalidos)
