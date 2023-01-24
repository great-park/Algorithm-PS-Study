from collections import deque
import sys
input = sys.stdin.readline
N, M, V = map(int, sys.stdin.readline().split(' '))

# 인접 리스트
graph = [list() for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# DFS 1


def DFS(graph, start, visited=[]):
    stack = []
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if not graph[node]:
                return visited
            for i in range(len(graph[node])-1, -1, -1):
                stack.append(graph[node][i])
    return visited

# DFS 2
# 재귀함수로 풀어보기


def DFS_recursive(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            DFS_recursive(graph, node, visited)
    return visited


# BFS

def BFS(graph, start, visited=[]):
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)

            if not graph[node]:
                return visited
            # extend는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다.
            queue.extend(graph[node])
    return visited


# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for i in range(1, len(graph)):
    graph[i].sort()
for node in DFS_recursive(graph, V):
    print(node, end=' ')
print()
for node in BFS(graph, V):
    print(node, end=' ')
