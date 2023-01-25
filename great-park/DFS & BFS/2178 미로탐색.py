from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 2차원 리스트 생성
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0, 0)])

# 미로 문제 풀 때는 이동을 표현해준다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

# BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0 <= next_x < N and 0 <= next_y < M:  # 범위 확인
            if graph[next_x][next_y] == 1:  # 경로 확인
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1  # value 자체를 이동 횟수로 사용

print(graph[N-1][M-1])
