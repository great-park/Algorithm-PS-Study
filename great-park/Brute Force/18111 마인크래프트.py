from sys import stdin
input = stdin.readline
N, M, B = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
# 제거 2초, 쌓기 1초
# 1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107
MIN = 1e9
MIN_h = 0
for h in range(257):
    # h만큼 높이를 맞추는 시간 구하기
    success = True
    block = B
    remove = 0
    add = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] > h:
                remove += g[i][j] - h
            elif g[i][j] < h:
                add += h - g[i][j]
    block = block + remove - add
    if block < 0:
        success = False
    if success:
        time = remove*2 + add*1
        if time <= MIN:
            MIN = time
            MIN_h = h
print(MIN, MIN_h)
