with open('1.txt', 'r') as f:
    presentes = f.read().splitlines()
total = 0

for dimensoes in presentes:
    d = [int(i) for i in dimensoes.split('x')]
    areas = [d[0] * d[1], d[0] * d[2], d[1] * d[2]]
    total += 2 * sum(areas) + min(areas)

print(total)


