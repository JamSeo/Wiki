N = int(input())  # 단어의 개수 N: 13
words = []  # 입력된 단어 저장할 []

for _ in range(N):  # 단어 입력받기 (단, 문자열 길이는 50이하)
    word = input()
    if word not in words:  # 단, 중복된 단어 저장 X
        words.append(word)

words.sort(key = lambda x : len(x))  # 단어 길이 기준 정렬

# 2중[]를 이용해서 길이가 같은 단어들 묶음
two_d_lst = [[] for _ in range(51)]
for word in words:
    two_d_lst[len(word)].append(word)

# 리스트별 알파벳 순으로 정렬
for lst in two_d_lst:
    lst.sort()

# 다시 words[]에 저장
words = sum(two_d_lst, [])

for i in words:
    print(i)