import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
INF = 1e9
shark_size = 2
now_x,now_y = 0,0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            now_x,now_y = i,j
            graph[i][j] = 0

def BFS():
    queue = deque([(now_x, now_y)])
    
    # 방문 여부
    visited = [[-1]*N for _ in range(N)]
    visited[now_x][now_y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 크기가 같은 경우
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

def solve(visited):
    x,y = 0, 0
    min_distance = INF
    for i in range(N):
        for j in range(N):
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x , y = i, j
    if min_distance == INF:
        return False
    else:
        return x,y,min_distance

answer = 0
food = 0

while True:
    result = solve(BFS())

    if not result:
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        graph[now_x][now_y] = 0
        food += 1
    
    if food >= shark_size:
        shark_size += 1
        food = 0
