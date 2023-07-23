from sys import stdin
stdin = open("input.txt")

def input():
    return stdin.readline().rstrip()

# N : int -- 포켓몬의 개수
# M : int -- 문제의 개수
N, M = map(int, input().split())

# ///////////////////// Success /////////////////////////
name = dict()  # name : {} -- 포켓몬 이름 : 번호
id = dict()  # id : {} -- 포켓몬 번호 : 이름
for i in range(1, N+1):
    poketmon = input()
    id[i] = poketmon
    name[poketmon] = i

for _ in range(M):
    quest = input()
    if quest.isdigit():
        print(id.get(int(quest)))
    else:
        print(name.get(quest))


# ///////////////////// 시간초과 /////////////////////////
book = []  # book : [] -- 포켓몬 도감
for _ in range(N):
    book.append(input())

for _ in range(M):
    # quest : int or str -- 입력되는 문제
    quest = input()

    # try문 : quest가 int형일 경우, 도감에서 포켓몬 이름 출력
    # except문 : quest가 str형일 경우, 도감에서 포켓몬 번호 출력
    try:
        print(book[int(quest)-1])

    except ValueError:
        for idx in range(N):
            if book[idx] == quest:
                print(idx+1)