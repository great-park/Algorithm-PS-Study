import sys
from collections import deque
input = sys.stdin.readline
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

R1, C1, R2, C2 = map(int, input().split())


def BFS(x, y):
    queue = deque([(x, y)])
    graph[y][x] = 1
    while queue:
        x, y = queue.popleft()

        if x == R2 and y == C2:
            return graph[y][x] - 1

        for i in range(6):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if graph[next_y][next_x] == 0:
                    queue.append([next_x, next_y])
                    graph[next_y][next_x] = graph[y][x] + 1
    return -1


print(BFS(R1, C1))
