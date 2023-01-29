from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
TARGET_A, TARGET_B = map(int, input().split())
RELATION = int(input())

GRAPH = [[] for _ in range(N+1)]
VISITED = [False] * (N+1)

for _ in range(RELATION) :
    # a = 부모 / b = 자식
    a, b = map(int, input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)

def calcRelation(targetA, targetB) :
    depth = 0
    q = deque()
    q.append([depth, targetA])
    VISITED[targetA] = True
    while q :
        depth, target = q.popleft()
        if target == targetB :
            return depth
        for member in GRAPH[target] :
            if not VISITED[member]  :
                VISITED[member] = True
                q.append([depth+1, member])
    return -1

print(calcRelation(TARGET_A, TARGET_B))