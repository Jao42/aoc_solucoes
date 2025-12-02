from tqdm import tqdm

def gerar_string(entrada):
    count = 1
    ultimo = entrada[0]
    count_str = ''
    for i in range(1, len(entrada)):
        if entrada[i] == ultimo:
            count += 1
            continue
        count_str += str(count) + ultimo
        ultimo = entrada[i]
        count = 1
    count_str += str(count) + ultimo
    return count_str

entrada = '1113222113'
for _ in tqdm(range(50)):
    entrada = gerar_string(entrada)
print(len(entrada))


