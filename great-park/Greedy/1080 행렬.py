from sys import stdin
input = stdin.readline
N, M = map(int, input().split())

first = [list(map(int, input().rstrip())) for _ in range(N)]
second = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = 0
success = False

for i in range(N-2):
    for j in range(M-2):
        if first[i][j] != second[i][j]:
            for x in range(i, i+3):
                for y in range(j, j+3):
                    first[x][y] = 1 - first[x][y]
            cnt += 1

# 연산이 끝난 후 확인
if first == second:
    print(cnt)
else:
    print(-1)
