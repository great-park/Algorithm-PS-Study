import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
# input이 붙어서 나오므로 구분해서 넣어줘야 함
graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = []

def BFS(x,y):
  cnt = 1
  # 파이썬의 deque() 함수는 선언할 때 들어왔던 인자를 자동으로 deque화 시켜서 저장
  queue = deque([(x,y)]) # cannot unpack non-iterable int object -> 괄호로 감싸기  or 선언 후 []만 append 하기
  graph[y][x] = 0
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      next_x = x + dx[i]
      next_y = y + dy[i]

      if 0 <= next_x < N and 0 <= next_y < N:
        if graph[next_y][next_x] == 1:
          queue.append([next_x, next_y])
          graph[next_y][next_x] = 0
          cnt += 1
  if cnt != 0:
    answer.append(cnt)
  
  
for i in range(N):
  for j in range(N):
    if graph[j][i] == 1:
      BFS(i,j)
      
print(len(answer))
answer.sort()
for cnt in answer:
  print(cnt)