import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
parent_info = list(map(int, input().split()))
Removed = int(input())

# 각 부모당 자식의 정보들 -> 자식의 개수가 0인 node가 leaf node
tree = [[] for _ in range(N)]
# 생존 여부
alive = [True for _ in range(N)]


for i in range(N):
    if parent_info[i] != -1:
        tree[parent_info[i]].append(i)  # 자식 추가


def BFS(p):
    queue = deque([p])
    # 방문 여부
    visited = [False for _ in range(N)]
    visited[p] = True
    alive[p] = False

    while queue:
        p = queue.popleft()

        for c in tree[p]:
            if not visited[c]:
                queue.append(c)
                visited[c] = True
                alive[c] = False


def solve(removed_node):
    cnt = 0
    alive[removed_node] = False
    for child in tree[removed_node]:
        BFS(child)

    for i in range(N):
        if alive[i] and len(tree[i]) == 0:
            cnt += 1
    return cnt


print(solve(Removed))
