with open('1.txt', 'r') as f:
    entrada = f.read()
print(entrada.count('(') - entrada.count(')'))
