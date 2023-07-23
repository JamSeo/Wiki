n = int(input())
stack = []
ans = []    # ans: 최종 출력 리스트

i = 1       # i: 1부터 n까지의 수

for _ in range(n):
    # 수열 입력 받기
    series = int(input())

    # i가 수열값보다 작으면?
    if i <= series:
        while i <= series:   # i랑 같아질 때 까지
            stack.append(i)  # push
            ans.append('+')
            i += 1
    # 이후 스택값과 수열값이 같다면?
    if stack[-1] == series:
        stack.pop()           # pop
        ans.append('-')
    # 다르다면? 가망없음
    else:
        print('NO')   # 'NO' 출력
        break
# for문이 끝나면?
else:
    for token in ans:
        print(token)  # ans 출력