"""
BFS 방식
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        now_node = q.popleft()
        for neighbor in GRAPH[now_node] :
            if not VISIT[neighbor]:
                q.append(neighbor)
                VISIT[neighbor] = True


# 정점 개수 N, 간선 개수 M
N, M = map(int, input().split())
# 주소가 1부터 시작하기 때문에 index 연산을 위해선 길이 +1
GRAPH = [[] for _ in range(N+1)]
# 연결 간선에 따라 각자 연결된 노드들 목록에 서로를 등록
for _ in range(M):
    v1,v2 = map(int, input().split())
    GRAPH[v1].append(v2)
    GRAPH[v2].append(v1)

# 주소가 1부터 시작하기 때문에 index 연산을 위해선 길이 +1
VISIT = [False] * (N+1) # 연산 여부 체크리스트 : 전역 변수
cnt = 0

for node in range(1, N+1):
    # 이미 해당 시작 노드에 대해서 BFS 연산을 했을 경우, Skip
    if VISIT[node]:
        continue
    VISIT[node] = True
    bfs(node)
    cnt += 1

print(cnt)


"""
UnionFind 방식

def find_parent(Parent, x) :
    if Parent[x] != x :
        Parent[x] = find_parent(Parent,Parent[x])
    return Parent[x]

def union_parent(Parent, a, b) :
    a = find_parent(Parent,a)
    b = find_parent(Parent,b)
    if a < b :
        Parent[b] = a
    else :
        Parent[a] = b


N, M = map(int, input().split())
route = [list(map(int,input().split())) for _ in range(M)]

Parent = [0] * (N+1)
for i in range(N+1):
    Parent[i] = i

for _ in range(2) :
    for x,y in route :
        union_parent(Parent, x, y)

print(len(set(Parent[1:])))
"""