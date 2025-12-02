with open('1.txt', 'r') as f:
    instructions_str = f.read().splitlines()

grid = [
        #0 -> off / 1 -> on
        [0 for _ in range(1000)]
        for _ in range(1000)
        ]


def do_instruction(instruction, inicio, fim):
    instructions_dic = {
            'on': 1,
            'off': 0
            }
    for i in range(inicio[0], fim[0] + 1):
        for j in range(inicio[1], fim[1] + 1):
            if instruction == 'toggle':
                grid[i][j] = (grid[i][j] + 1) % 2
                continue
            grid[i][j] = instructions_dic[instruction]


def get_total_on():
    total = 0
    for linha in grid:
        total += sum(linha)
    return total
        
for instruction_str in instructions_str:
    instructions_split = instruction_str.split(' ')
    fim = [ int(i) for i in instructions_split[-1].split(',') ]
    inicio = [ int(i) for i in instructions_split[-3].split(',') ]
    instruction = instructions_split[-4]
    do_instruction(instruction, inicio, fim)
print(get_total_on())

#print(get_total_on())
