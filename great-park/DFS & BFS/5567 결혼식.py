import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[0] * (n+1) for i in range(n+1)] # 1번 인덱스부터 사용
visited = [0 for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 1번 인덱스 -> 상근이 -> 상근이의 친구들
# 상근이 친구들의 친구들을 탐색한다. -> 이때 이미 초대할 사람인 지를 확인하여 중복되지 않도록 한다.
# 탐색 깊이는 최대 2이다. -> visited의 값을 누적합으로 정해서 탐색의 depth를 표현
# -> 어떤 사람의 visited의 값은 최대 3이다. (1: 본인, 2: 직접 친구, 3: 친구의 친구)

def BFS(x):
  queue = deque([x])
  visited[x] = 1
  
  while queue:
    friend_num = queue.popleft()
    for people_num in graph[friend_num]:
      if visited[people_num] == 0:
        queue.append(people_num)
        visited[people_num] = visited[friend_num] + 1


def solve():
  BFS(1)
  result = 0
  for i in range(2, n+1):
    if 0 < visited[i] <=3:
       result += 1
  print(result)

solve()