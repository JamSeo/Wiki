# Googling 해법 코드
# : nCm의 0의 개수를 출력하기 위해 계산식에서 2와 5의 개수만 파악해줄 예정

# *** 이때, key point는 지수 구하는 법 ***
# cf. n!에 대한 5의 지수 == n//5 + n//25 + n//125 + ...
# cf. m!에 대한 2의 지수 == m//2 + m//4 + m//8 + m//16 + ...

def count_index(num, index):  # 지수 구하는 함수
    cnt = 0
    while num >= index:
        cnt += num // index
        num //= index
    return cnt


n, m = map(int, input().split())  # 25, 12

cnt2 = count_index(n, 2) - count_index(n - m, 2) - count_index(m, 2)
cnt5 = count_index(n, 5) - count_index(n - m, 5) - count_index(m, 5)

print(min(cnt2, cnt5))  # 2와 5의 지수 중 더 작은값 출력