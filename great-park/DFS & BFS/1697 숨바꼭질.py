import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10**5
graph = [0]* (2* MAX + 1)

def BFS():
  queue = deque([N])
  while queue:
    a = queue.popleft()
    
    if a == K:
      print(graph[K])
      return
    
    # 만약 0이 아니라면, 이미 "다른 경로"로 해당 자리를 거쳤고,
    # 그 자리 값에 1을 더하는 행위는 곧, 현재의 경로가 최단 경로가 아님을 의미한다.
    # 순간이동하는 경우가 이득일 때만 실시
    if abs(K - 2*a) < abs(K - a) and graph[2*a] == 0:
      queue.append(2*a)
      graph[2*a] = graph[a]+1
    # 걷기
    if a+1 <= MAX and graph[a+1] == 0:
      queue.append(a+1)
      graph[a+1] = graph[a]+1
    if a-1 >= 0 and graph[a-1] == 0:
      queue.append(a-1)
      graph[a-1] = graph[a]+1

BFS()