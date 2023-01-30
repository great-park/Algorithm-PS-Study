import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
b_visited = [[False for _ in range(N)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
b_cnt = 0


def BFS(x, y, color):
    global cnt
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_y][next_x]:
                if graph[next_y][next_x] == color:
                    queue.append([next_x, next_y])
                    visited[next_y][next_x] = True
    cnt += 1


def b_BFS(x, y, color):
    global b_cnt
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        b_visited[y][x] = True
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and not b_visited[next_y][next_x]:
                if graph[next_y][next_x] == color:
                    queue.append([next_x, next_y])
                    b_visited[next_y][next_x] = True
                elif (color == 'R' and graph[next_y][next_x] == 'G') \
                        or (color == 'G' and graph[next_y][next_x] == 'R'):
                    queue.append([next_x, next_y])
                    b_visited[next_y][next_x] = True
    b_cnt += 1


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(j, i, graph[i][j])
        if not b_visited[i][j]:
            b_BFS(j, i, graph[i][j])
print(cnt, end=' ')
print(b_cnt, end=' ')
