import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()


def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
cannot_complete = False
day = 0


def solve():
    global cannot_complete, day
    BFS()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cannot_complete = True
            day = max(day, graph[i][j])


solve()
if cannot_complete:
    print(-1)
else:
    print(day-1)
