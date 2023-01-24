from collections import deque
from re import T
from sys import stdin
input = stdin.readline

N = int(input())
com_num = int(input())
graph = list([] for _ in range(N+1))
visited = [False] * (N+1)
cnt = 0

for i in range(com_num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def DFS(start):
    global cnt
    stack = deque([start])

    while stack:
        x = stack.pop()
        visited[x] = True

        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                stack.append(node)
                cnt += 1


def BFS(start):
    global cnt
    queue = deque([start])

    while queue:
        x = queue.popleft()
        visited[x] = True

        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                cnt += 1


# BFS(1)
DFS(1)
print(cnt)
