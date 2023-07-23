# 구글링...ㅠㅠ

table = dict()
rep = dict()
for i in range(51):
    for j in range(51):
        table[i, j] = 'EMPTY'
        rep[i, j] = (i, j)


# find_set : (r, c)가 속한 집합의 대표 좌표 리턴
def find_set(r, c):
    while (r, c) != rep[r, c]:
        (r, c) = rep[r, c]
    return r, c


# union: (r2, c2)의 대표원소가 (r1, c1)의 대표원소를 가리키도록 함
def union(r1, c1, r2, c2):
    rep[r2, c2] = (r1, c1)


def solution(commands):
    answer = []

    for command in commands:
        cmd, *arg = command.split()

        if cmd == 'UPDATE' and len(arg) == 3:
            r, c, value = arg
            table[find_set(int(r), int(c))] = value

        elif cmd == 'UPDATE' and len(arg) == 2:
            value1, value2 = arg
            for cell in table:
                r, c = find_set(*cell)
                table[r, c] = value2 if table[r, c] == value1 else table[r, c]

        elif cmd == 'MERGE':
            r1, c1, r2, c2 = map(int, arg)
            r1, c1 = find_set(r1, c1)
            r2, c2 = find_set(r2, c2)

            if (r1, c1) == (r2, c2):
                continue
            if table[r1, c1] != 'EMPTY':
                union(r1, c1, r2, c2)
            else:
                union(r2, c2, r1, c1)

        elif cmd == 'UNMERGE':
            r, c = map(int, arg)
            value = table[find_set(r, c)]
            pr, pc = find_set(r, c)
            merge_list = []

            for cell in table:
                if find_set(*cell) == (pr, pc):
                    merge_list.append(cell)
            for mi, mj in merge_list:
                table[mi, mj] = 'EMPTY'
                rep[mi, mj] = (mi, mj)
            table[r, c] = value

        elif cmd == 'PRINT':
            r, c = map(int, arg)
            answer.append(table[find_set(r, c)])

    return answer
