from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
visitied = [False]*N
ans = []


def DFS():
    if len(ans) == M:
        print(*ans)
        return

    duplicated_num = 0
    for i in range(N):
        if not visitied[i] and duplicated_num != data[i]:
            if len(ans) == 0:
                visitied[i] = True
                ans.append(data[i])
                duplicated_num = data[i]
                DFS()
                ans.pop()
                visitied[i] = False
            else:
                if data[i] >= ans[-1]:
                    visitied[i] = True
                    ans.append(data[i])
                    duplicated_num = data[i]
                    DFS()
                    ans.pop()
                    visitied[i] = False


DFS()
