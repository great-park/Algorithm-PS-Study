import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

# 나이트의 이동 경우의 수
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def BFS(x, y):
    queue = deque([(x, y)])
    graph[y][x] = 0

    while queue:
        x, y = queue.popleft()

        if x == target[0] and y == target[1]:
            return graph[y][x]

        for i in range(8):
            next_x, next_y = x + dx[i], y + dy[i]

            if 0 <= next_x < L and 0 <= next_y < L:
                if graph[next_y][next_x] == 0:
                    queue.append([next_x, next_y])
                    graph[next_y][next_x] = graph[y][x] + 1


for case in range(T):
    L = int(input())
    graph = [[0 for _ in range(L)] for _ in range(L)]
    knight = list(map(int, input().split()))
    target = list(map(int, input().split()))
    print(BFS(knight[0], knight[1]))
