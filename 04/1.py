# 구현
# 상하좌우
# N * N 크기의 정사각형의 공간에서 상하좌우로 움직여서 목적지 도착하기

n = int(input())

moves = input().split()

x,y = 1,1
dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_type = ["L", "R", "U", "D"]

for m in moves:
    for i in range(len(move_type)):
        if m == move_type[i]:
            dumpX = x + dx[i]
            dumpY = y + dy[i]

    if dumpX < 1 or dumpY < 1 or dumpX > n or dumpY > n:
        continue
    x, y = dumpX, dumpY

print(x, y)
