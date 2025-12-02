def parsear_declaracao(declaracao):
    expressao, variavel = declaracao.split(' -> ')
    if not ' ' in expressao:
        return (variavel, expressao)
    operandos = expressao.split()
    operador = operandos.pop(-2)
    return (variavel, (operador, operandos))
       

def resolver_expressao(rotulo):
    if type(rotulo) == int or rotulo.isnumeric():
        return int(rotulo)
    expressao = variaveis[rotulo]
    if type(expressao) in (str, int):
        variaveis[rotulo] = resolver_expressao(expressao)
        return variaveis[rotulo]

    operador = expressao[0]
    operandos = expressao[1]
    operandos = [resolver_expressao(operando) for operando in operandos]

    operacoes = {
            'AND': (lambda x, y: x & y),
            'OR': (lambda x, y: x | y),
            'NOT': (lambda x: ~ x),
            'LSHIFT': (lambda x, y: x << y),
            'RSHIFT': (lambda x, y: x >> y),
            }

    variaveis[rotulo] = operacoes[operador](*operandos) % 65536
    return variaveis[rotulo]


with open('1.txt', 'r') as f:
    declaracoes = f.read().splitlines()

variaveis = {}

for declaracao in declaracoes:
    variavel, valor = parsear_declaracao(declaracao)
    variaveis[variavel] = valor

print(resolver_expressao('a'))
