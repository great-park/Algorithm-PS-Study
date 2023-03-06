from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
data = list([0]*20 for _ in range(N))

for k in range(M):
    line = list(map(int, input().split()))
    inst = line[0]
    i = line[1]
    x = 0
    if len(line) == 3:
        x = line[2]

    if inst == 1:  # add
        data[i-1][x-1] = 1
    elif inst == 2:  # sub
        data[i-1][x-1] = 0
    elif inst == 3:
        for j in range(19, 0, -1):
            data[i-1][j] = data[i-1][j-1]
        data[i-1][0] = 0
    elif inst == 4:
        for j in range(19):
            data[i-1][j] = data[i-1][j+1]
        data[i-1][19] = 0

ans = []
for check in data:
    if check not in ans:
        ans.append(check)
print(len(ans))
