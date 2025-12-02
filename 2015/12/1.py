with open('entrada.txt', 'r') as f:
	entrada = f.read()

#entrada = '{"a":{"b":4},"c":-10}'

def somar_numeros(entrada):
	soma_total = 0
	numero_str = ''
	negativo = False
	for char in entrada:
		if char == '-':
			negativo = True
			continue
		if char.isnumeric():
			numero_str += char
			continue
		if numero_str:
			numero = int(numero_str)
			soma_total += -numero if negativo else numero
		numero_str = ''
		negativo = False
	return soma_total

print(somar_numeros(entrada))

