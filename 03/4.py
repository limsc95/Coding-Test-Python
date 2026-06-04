# 1이 될 때까지
# 어떠한 수를 1이 될때 까지 두기지 과정 중 하나를 반복하여 수행
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

n, k = map(int, input().split())

count = 0

while n > 1:
    if n % k != 0:
        n -= 1
    else:
        n //= k
    count += 1

print(count)