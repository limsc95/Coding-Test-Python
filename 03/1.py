# 그리디
# 문제: 거스름돈
# N원을 받았을 때, 500원, 100원, 10원으로 거스름돈을 돌려줄 최소의 개수
# N은 10의 배수

m = 1260
count = 0
moneyList = [500,100,50,10]

for money in moneyList:
    x, m = divmod(m, money)
    count = count + x

print(count)
