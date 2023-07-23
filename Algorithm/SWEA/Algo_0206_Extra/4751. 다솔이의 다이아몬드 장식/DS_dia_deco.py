import sys
sys.stdin = open("sample_input.txt")

def mkit_dia(word):
    N = len(word)
    a1 = ['.' + '.#..' * N]
    a2 = ['.' + '#.#.' * N]
    a3 = []
    w3 = '#'
    for char in word:
        w3 += f'.{char}.#'
    a3.append(w3)
    return '\n'.join(a1 + a2 + a3 + a2 + a1)


T = int(input())
for _ in range(T):
    print(mkit_dia(input()))