

def gerar_senha_nova(senha_antiga):
	letras = [ chr(i) for i in range(ord('a'), ord('z') + 1) ]
	shift = ord('a')
	senha_nova = ''
	passo = 1
	for i in range(len(senha_antiga) -1, -1, -1):
		if passo == 0:
			senha_nova = senha_antiga[:i + 1] + senha_nova
			break
		letra = senha_antiga[i]	
		passo, indice = divmod(
			ord(letra) - shift + passo, len(letras)
		)
		senha_nova = letras[indice] + senha_nova
		
	return senha_nova

def teste_01(senha):
	total = 1
	for i in range(1, len(senha)):
		if total == 3:
			return True
		if (ord(senha[i]) - ord(senha[i - 1])) == 1:
			total += 1
			continue
		total = 1
	return False

def teste_02(senha):
	return not any(letra in 'iol' for letra in senha)
		
def teste_03(senha):
	pares = set()	
	for i in range(1, len(senha)):
		if (ord(senha[i]) == ord(senha[i - 1])):
			pares.add(senha[i] * 2)
		if len(pares) == 2:
			return True
	return False


	

def checar_validade_senha(senha):
	return (
		teste_01(senha) and
		teste_02(senha) and
		teste_03(senha)
	)

def main(senha):
	senha = gerar_senha_nova(senha)
	while checar_validade_senha(senha) == False:
		senha = gerar_senha_nova(senha)
	return senha
	
senha = 'hepxxyzz'

print(main(senha))

"""
print(teste_01(senha))
print(teste_02(senha))
print(teste_03(senha))
"""
