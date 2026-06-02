# 문제: 큰 수의 법칙
# 입력 조건: 첫 줄에 N(2< N < 1000), M(1< M < 10000), K(1< K < 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분
# 둘째 줄에 n개의 자연서가 주어지며, 공백으로 구분, 1 이상 10000 이하
# 입력으로 주어지는 K는 항상 M 보다 작거나 같다
# 출력 조건 첫째 주에 동빈이의 큰 수의 법칙에 따라 더해진 값 출력

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

x = data[n-1]
y = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += x
        m -= 1
    if m == 0:
        break
    result += y
    m -= 1

print(result)