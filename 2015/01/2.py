with open('2.txt', 'r') as f:
    entrada = f.read()
pilha_andares = 0

for indice, andar in enumerate(entrada):
    if andar == '(':
        pilha_andares += 1
    else:
        pilha_andares -= 1
    if pilha_andares == -1:
        print(indice + 1)
        exit()
