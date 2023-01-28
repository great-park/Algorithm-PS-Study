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
# root 노드 인덱스
root = 0


for i in range(N):
    if parent_info[i] != -1:
        tree[parent_info[i]].append(i)  # 자식 추가
    else:
        root = i


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

    # root 노드를 삭제하는 경우
    if removed_node == root:
        return 0
    # 리프노드를 삭제하는 경우
    elif len(tree[removed_node]) == 0:
        # 삭제하려는 노드의 부모 인덱스 구하기
        parent_index = 0
        for i, parent in enumerate(tree):
            for child in parent:
                if child == removed_node:
                    parent_index = i
        # 삭제하려는 노드을 부모에서 제거
        tree[parent_index].remove(removed_node)
    # internal 노드를 삭제하는 경우
    else:
        for child in tree[removed_node]:
            BFS(child)

    for i in range(N):
        if alive[i] and len(tree[i]) == 0:
            cnt += 1
    return cnt


print(solve(Removed))
