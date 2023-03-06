from sys import stdin
from collections import deque
input = stdin.readline
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
MAX_H = max(max(city))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
MAX = 0


def BFS(x, y, H):
    queue = deque()
    queue.append([x, y])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and city[ny][nx] > H:
                queue.append([nx, ny])
                visited[ny][nx] = True


result = []
for H in range(MAX_H):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for b in range(N):
        for a in range(N):
            if not visited[b][a] and city[b][a] > H:
                BFS(a, b, H)
                cnt += 1
    result.append(cnt)

print(max(result))
