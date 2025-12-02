with open('1.txt', 'r') as f:
    strings = f.read().splitlines()

def is_nice_string(s):
    ultima = ''
    penultima = ''
    vogais_presentes = 0
    indice_ultimo_duo = -1
    sanduiche = False
    duos = {}
    ultimo_duo = ''
    for indice, letra in enumerate(s):
        duo = letra + ultima
        if indice == 0:
            duo = ''
        if duo != ultimo_duo or indice_ultimo_duo != indice - 1:
            duos[duo] = duos.get(duo, 0) + 1
            indice_ultimo_duo = indice
            ultimo_duo = duo
        if letra == penultima:
            sanduiche = True
        penultima = ultima
        ultima = letra
    if max(duos.values()) >= 2 and sanduiche:
        return True
    return False


        
        
total = 0
#strings = [ 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
for s in strings:
    #print(is_nice_string(s))
    total += int(is_nice_string(s))
print(total)


