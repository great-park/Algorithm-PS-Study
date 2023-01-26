import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

# 벽을 -1로 바꿔주기
for i in range(M):
  for j in range(N):
    if graph[j][i] == 1:
      graph[j][i] = -1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
break_wall = 0

# (1,1)은 0,0 으로, (N,M)은 N-1, M-1으로 생각하고 풀기
# 벽을 부수는 카운트 변수를 정해서 0이면 벽을 부술 수 있고, 1보다 크거나 같으면 부술 수 없도록 한다.
def BFS(x,y):
  queue = deque([(x,y)])
  
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      next_x, next_y = x+dx[i], y+dy[i]
      if 0 <= next_x < M and 0 <= next_y < N:  # 범위 확인
          if graph[next_x][next_y] != -1:  # 경로 확인
              queue.append((next_x, next_y))
              graph[next_x][next_y] = graph[x][y] + 1  # value 자체를 이동 횟수로 사용

# 벽을 부술 기회를 언제 써야 하는가??