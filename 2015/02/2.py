with open('1.txt', 'r') as f:
    presentes = f.read().splitlines()

total = 0

for dimensoes in presentes:
    d = sorted([int(i) for i in dimensoes.split('x')])
    total += 2 * (d[0] + d[1]) + d[0] * d[1] * d[2]

print(total)


