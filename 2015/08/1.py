with open('1.txt', 'r') as f:
    strings = f.read().splitlines()

total = 0
for s in strings:
    print(eval(s))
print(total)

