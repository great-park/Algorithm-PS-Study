from sys import stdin
input = stdin.readline
N, M, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
inst = list(map(int, input().split()))


def solve(x):
    temp = [[0 for _ in range(M)] for _ in range(N)]
    temp2 = [[0 for _ in range(N)] for _ in range(M)]
    if x == 1:
        for i in range(N):
            temp[i] = data[N-1-i]
        return temp

    if x == 2:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][M-1-j]
        return temp

    """
              x
    xixx ->   i
              x
              x

    i, j  =>   N-1-j, i
    """
    if x == 3:
        for i in range(M):
            for j in range(N):
                temp2[i][j] = data[N-1-j][i]
        return temp2

    if x == 4:
        for i in range(M):
            for j in range(N):
                temp2[i][j] = data[j][M-1-i]
        return temp2

    if x == 5:
        for i in range(N//2):  # 1과 2영역을 각각 2와 3으로 보낸다.
            for j in range(M//2):  # 1
                temp[i][j+M//2] = data[i][j]

            for k in range(M//2, M):  # 2
                temp[i+N//2][k] = data[i][k]

        for i in range(N//2, N):  # 3과 4영역을 각각 4와 1으로 보낸다.
            for j in range(M//2):  # 4
                temp[i-N//2][j] = data[i][j]

            for k in range(M//2, M):  # 3
                temp[i][k-M//2] = data[i][k]
        return temp

    if x == 6:
        for i in range(N//2):  # 1과 2영역을 각각 4와 1으로 보낸다.
            for j in range(M//2):  # 1
                temp[i+N//2][j] = data[i][j]

            for k in range(M//2, M):  # 2
                temp[i][k-M//2] = data[i][k]

        for i in range(N//2, N):  # 3과 4영역을 각각 2와 3으로 보낸다.
            for j in range(M//2):  # 4
                temp[i][j+M//2] = data[i][j]

            for k in range(M//2, M):  # 3
                temp[i-N//2][k] = data[i][k]
        return temp


for x in inst:
    data = solve(x)
    if x == 3 or x == 4:
        N, M = M, N

for row in data:
    print(*row)
