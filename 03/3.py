# 숫자카드 게임
# 숫자 행 N, 열 M 을 공백을 기준으로 입력 (1< n,m < 100)
# 각 카드의 값 1이상 10,000 이하
# 여러개의 숫자 카드 중 가장 높은 숫자 카드를 한 장 뽑기
# 각 행에서 가장 낮은 숫자 추출 후 그 중 가장 큰 숫자 뽑기

n, m = map(int, input().split())

res = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    res = max(res, min_value)

print(res)