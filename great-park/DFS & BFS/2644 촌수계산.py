import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
A, B = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def BFS(a, b):
    queue = deque([a])
    visited[a] = 0

    while queue:
        people = queue.popleft()

        if people == b:
            return visited[b]

        for f in graph[people]:
            if visited[f] == 0:
                queue.append(f)
                visited[f] = visited[people] + 1
    return -1


print(BFS(A, B))
