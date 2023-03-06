from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
p, m, mp, d = map(int, input().split())
MAX = -1e9
MIN = 1e9


def DFS(depth, final_val):
    global p, m, mp, d, MAX, MIN
    if depth == N:
        MAX = max(MAX, final_val)
        MIN = min(MIN, final_val)
        return

    if p > 0:
        p -= 1
        DFS(depth+1, final_val + A[depth])
        p += 1
    if m > 0:
        m -= 1
        DFS(depth+1, final_val - A[depth])
        m += 1
    if mp > 0:
        mp -= 1
        DFS(depth+1, final_val * A[depth])
        mp += 1
    if d > 0:
        d -= 1
        DFS(depth+1, int(final_val/A[depth]))
        d += 1


DFS(1, A[0])
print(MAX)
print(MIN)
