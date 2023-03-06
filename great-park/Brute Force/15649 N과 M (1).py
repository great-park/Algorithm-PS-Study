from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
ans = []


def answer():
    for x in ans:
        print(x, end=' ')
    print()


def DFS():
    if len(ans) == M:
        answer()
        return

    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            DFS()
            ans.pop()


DFS()
