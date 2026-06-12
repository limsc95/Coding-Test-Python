# 체스 나이트 움직이기
# 8*8 좌표 평면에서 나이트가 L(수평2, 수작1 or 수직2, 수평1) 로 움직일 때 이동 가능한 경우의 수 찾기

input_data = input()

x = int(input_data[1])
y = int(ord(input_data[0])) - int(ord('a')) + 1 # 'a' = 97

result = 0

move_type = [(-2,-1),(-2,1),(2,-1),(2,1),(1,-2),(1,2),(-1,-2),(-1,2)]

for move in move_type:
    nx = x + move[0]
    ny = y + move[1]

    if nx >=1 and ny >= 1 and nx <= 8 and ny <= 8:
        result += 1

print(result)