from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
TARGET_A, TARGET_B = map(int, input().split())
RELATION = int(input())

GRAPH = [[] for _ in range(N+1)]
VISITED = [False] * (N+1)

"""
부모 자식간의 관계 추가
"""
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
        """
        관계 차수계산
        """
        depth, target = q.popleft()
        """
        최소 관계 차수로 반환
        """
        if target == targetB :
            return depth
        for member in GRAPH[target] :
            """
            한 번도 확인하지 않은 직계/친척 가족일 경우에만
            """
            if not VISITED[member]  :
                VISITED[member] = True
                q.append([depth+1, member])
    return -1

print(calcRelation(TARGET_A, TARGET_B))