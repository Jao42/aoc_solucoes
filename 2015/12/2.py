import json

with open('entrada.txt', 'r') as f:
	entrada = f.read()

a = json.loads(entrada)

def somar_numeros(objeto):
	iteravel = []
	if type(objeto) == list:
		iteravel = objeto
	if type(objeto) == dict:
		iteravel = objeto.values()
		if 'red' in iteravel:
			return 0
	if len(iteravel) == 0:
		return 0
	total = 0
	for i in iteravel:
		if type(i) == int:
			total += i
		if type(i) == dict or type(i) == list:
			soma_parcial = somar_numeros(i)
			total += soma_parcial
			
	return total
	
print(somar_numeros(a))

