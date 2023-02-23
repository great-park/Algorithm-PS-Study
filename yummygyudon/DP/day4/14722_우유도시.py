### My Part ###
import sys
input = sys.stdin.readline
from collections import deque

"""
시도 1 : DP + BFS 방식 -> 시간 초과
"""
# ABLE_BEFORE = dict()
# ABLE_BEFORE[0] = 2
# ABLE_BEFORE[1] = 0
# ABLE_BEFORE[2] = 1

ABLE_NEXT = dict()
ABLE_NEXT[0] = 1
ABLE_NEXT[1] = 2
ABLE_NEXT[2] = 0

"""동쪽과 남쪽으로만 이동 가능"""
d = [[0,1], [1,0]]


N = int(input())
MAP = []
for _ in range(N) :
    MAP.append(list(map(int, input().split())))

DP = [[0] * N for _ in range(N)]


DP[0][0] = 1

q = deque()
q.append([0,0])
while q :
    y, x = q.popleft()
    for i in range(2) :
        ny = d[i][0] + y
        nx = d[i][1] + x
        # if ny == N-1 and nx == N-1 :
        #     continue
        # if MAP[y][x] == ABLE_BEFORE[MAP[by][bx]] :
        #     if 0<=by<N and 0<=bx<N :
        #         DP[y][x] = max(DP[]
        if 0<=ny<N and 0<=nx<N :
            """
            순서에 맞는 우유가 다음 칸에 있다면 본 값에 + 1 한값과 다음 칸의 DP 값에 대한 max
            """
            if MAP[ny][nx] == ABLE_NEXT[MAP[y][x]] :
                DP[ny][nx] = max(DP[ny][nx], DP[y][x] + 1)

            else :
                """
                다음 칸이 무시해야하는 칸일 경우, 다음 칸의 DP값과 현재 칸의 DP 값에 대한 max
                """
                DP[ny][nx] = max(DP[ny][nx], DP[y][x])
            """
            다음 칸의 우유를 먹든 무시하든 우선 이동하긴해야함.
            """
            print(DP)
            q.append([ny, nx])
            # print(DP)
print(DP[N-1][N-1])



