with open('1.txt', 'r') as f:
    strings = f.read().splitlines()

def is_nice_string(s):
    exclude = ['ab', 'cd', 'pq', 'xy']
    if any(sub in s for sub in exclude):
        return False
    anterior = ''
    vogais_presentes = 0
    duo = False
    for letra in s:
        if letra in 'aeiou':
            vogais_presentes += 1
        if letra == anterior:
            duo = True
        anterior = letra
    if duo and vogais_presentes >= 3:
        return True
    return False


        
        
total = 0
#strings = [ 'ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
for s in strings:
    #print(is_nice_string(s))
    total += int(is_nice_string(s))
print(total)


