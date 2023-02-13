N = int(input())
find = int(input())
data = [[0]*N for _ in range(N)]

# 시계방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
i = 0
x, y = 0, -1  # -> 0,0부터 시작
find_x, find_y = 0, 0
for value in range(N**2, 0, -1):
    next_x, next_y = x + dx[i], y + dy[i]  # 시계 방향으로 회전

    if not (0 <= next_x < N and 0 <= next_y < N and data[next_y][next_x] == 0):
        i = (i+1) % 4  # 1->2->"3"
        next_x, next_y = x + dx[i], y + dy[i]
    data[next_y][next_x] = value
    x, y = next_x, next_y

    if value == find:
        find_x, find_y = x+1, y+1


for row in data:
    print(*row)
print(find_x, find_y)
