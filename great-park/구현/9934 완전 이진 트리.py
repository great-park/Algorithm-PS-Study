from sys import stdin
input = stdin.readline
K = int(input())
building = list(map(int, input().split()))

ans = {i: [] for i in range(K)}  # depth 당 노드들
# 분할 정복


def find(building, depth):
    mid = len(building) // 2
    ans[depth].append(building[mid])

    if depth == K-1:
        return

    find(building[:mid], depth+1)
    find(building[mid:], depth+1)


find(building, 0)
for i in range(K):
    for k in range(len(ans[i])):
        print(ans[i][k], end=' ')
    print()
