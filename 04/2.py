# 시각
# N이 입력되면 00:00:00 부터 N:59:59 까지의 모든 시각 중 3이 하나라도 포함된 모든 경우의 수 구하기

x = int(input())

count = 0

for i in range(0, x+1):
    for j in range(0, 60):
        for k in range(0,60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)