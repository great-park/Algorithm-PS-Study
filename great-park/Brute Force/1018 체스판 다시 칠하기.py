from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
result = []
for i in range(n-7):
    for j in range(m-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    else:
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    else:
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))
