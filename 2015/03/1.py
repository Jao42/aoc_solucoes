with open('1.txt', 'r') as f:
    coordenadas = f.read()
casas =  {(0,0), }

coord_dic = {
    #(qual_coordenada -> x = 0 ; y = 1, quanto_anda)
    '^': (1, 1),
    'v': (1, -1),
    '>': (0, 1),
    '<': (0, -1),
    }

coord_atual = [0, 0]
for coord in coordenadas:
    c = coord_dic[coord]
    coord_atual[c[0]] += c[1]
    casas.add(tuple(coord_atual))

print(len(casas))


