with open('entrada.txt', 'r') as f:
	entrada = f.read().splitlines()

fator_mult = {'R': 1, 'L': -1}
total = 50
clock_zero = 0
for linha in entrada:
	passo = fator_mult[linha[0]] * int(linha[1:])
	if total == 0 and passo < 0:
		clock_zero -= 1
	total += passo
	clock_zero += abs(total // 100)
	total %= 100
	if total == 0 and passo < 0:
		clock_zero += 1
	
	
print(clock_zero)
