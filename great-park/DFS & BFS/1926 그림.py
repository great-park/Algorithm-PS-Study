import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = list()


def BFS(x, y):
    queue = deque([(x, y)])
    graph[y][x] = 1
    size = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if graph[next_y][next_x] == 1:
                    queue.append([next_x, next_y])
                    graph[next_y][next_x] = 0
                    size += 1
    return size


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer.append(BFS(j, i))
print(len(answer))
if len(answer) == 0:
    print(0)
else:
    if max(answer) == 1:
        print(max(answer))
    else:
        print(max(answer) - 1)
