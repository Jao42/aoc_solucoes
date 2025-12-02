import hashlib
from tqdm import tqdm

# For a string
data_string = "yzbqklnj"
for i in tqdm(range(1_000_000_000)):
    s = data_string + str(i)
    md5_hash_string = hashlib.md5(s.encode('utf-8')).hexdigest()
    if md5_hash_string[0: 5] == '00000':
        print(s)
        print(i)
        exit()

