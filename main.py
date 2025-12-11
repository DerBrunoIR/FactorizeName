from sympy import primefactors, factorint
from functools import reduce
import sys

def formula(factors: dict[int, int]) -> str:
    s = []
    factors = sorted(factors.items(), key=lambda a: a[0])
    for (prime, times) in factors:
        assert times >= 1
        if times == 1:
            s.append(f'{prime}')
        if times > 1:
            s.append(f'{prime}**{times}')

    return ' * '.join(s)

def main(text: str):
    num = int(''.join([str(hex(ord(c))[2:]) for c in text]), 16)
    factors = factorint(num)

    _formula = formula(factors)
    check_num = reduce(
        lambda a, b: a * b, 
        [prime**times for (prime, times) in factors.items()],
    )
    assert check_num == num
    print(_formula)
    print('check via:', file=sys.stderr)
    print(f"python3 -c \"print(({_formula}).to_bytes({len(text)}, 'big'))\"", file=sys.stderr)


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        print(f"{argv[0]} <text>")
        exit(1)
    text = argv[1]
    main(text)
