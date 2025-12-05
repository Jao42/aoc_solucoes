import sys
sys.set_int_max_str_digits(100000)

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 
          211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

sumseq = lambda x, y: (y+x-1) * (y-x) // 2 if y > x else 0

def sumsymm(n, base, repeats):
    pattern = ((base*10)**repeats - 1) // (base*10 - 1)
    assert base * pattern < n
    assert base < min((n+pattern-1)//pattern, base*10) 
    x, y = base, min((n+pattern-1)//pattern, base*10)
    return sumseq(x, y) * pattern

def repsymm(n, repeats):
    res = 0
    base = 1
    while ((base*10)**repeats - 1) // (base*10 - 1) * base < n:
        res += sumsymm(n, base, repeats)
        base *= 10
    return res

def repsymm_diff(a, b, repeats):
    return repsymm(b, repeats) - repsymm(a, repeats)


def part1(a, b):
    return repsymm_diff(a, b, 2)

def sumall2(a, b):
    max_repeats = len(str(b))
    assert max_repeats <= primes[-1]
    res = 0
    for p in primes:
        if p > max_repeats: break
        res += repsymm_diff(a, b, p)
    for p in primes:
        for q in primes:
            if q >= p or p*q > max_repeats: break
            res -= repsymm_diff(a, b, p*q)
    for p in primes:
        for q in primes:
            if q >= p or p*q > max_repeats: break
            for r in primes:
                if r >= q or p*q*r > max_repeats: break
                res += repsymm_diff(a, b, p*q*r)
    for p in primes:
        for q in primes:
            if q >= p or p*q > max_repeats: break
            for r in primes:
                if r >= q or p*q*r > max_repeats: break
                for s in primes:
                    if s >= r or p*q*r*s > max_repeats: break
                    res -= repsymm_diff(a, b, p*q*r*s)
    return res


def solve(data):
    data = [pair.split('-') for pair in data.split(',')]
    ans1, ans2 = 0, 0
    for pairs in data:
        a, b = int(pairs[0]), int(pairs[1])
        ans1 += part1(a, b+1)
        ans2 += sumall2(a, b+1)
    return ans1, ans2

def solve_range(a, b):
    return part1(a, b+1), sumall2(a, b+1)

print(solve_range(0, 10**220))

