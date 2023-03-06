import sys
from collections import deque
input = sys.stdin.readline
M, N, K = map(int, input().split()) # M=>y, N=>x
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = []
graph = [[1 for _ in range(N)] for _ in range(M)]

# 직사각형 영역 방문 불가 상태로 만들기
for i in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for _y in range(y1, y2):
    for _x in range(x1, x2):
      graph[_y][_x] = 0

def BFS(x,y):
  queue = deque()
  queue.append([x,y])
  graph[y][x] = 0 # 방문 처리
  
  cnt = 1
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      next_x = x + dx[i]
      next_y = y + dy[i]
      
      if 0 <= next_x < N and 0 <= next_y < M: # 범위 확인
        if graph[next_y][next_x] == 1: # 방문 가능한지 확인
          graph[next_y][next_x] = 0
          queue.append([next_x, next_y])
          cnt += 1
  answer.append(cnt)
  
for _x in range(N):
  for _y in range(M):
    if graph[_y][_x] == 1: # 방문 가능하다면,
      BFS(_x, _y) # 방문할 수 있는 모든 점 다 채우기 and cnt 계산
      
answer.sort()
print(len(answer))
for cnt in answer:
  print(cnt, end=' ')
