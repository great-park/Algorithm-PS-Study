from collections import deque
import sys
input = sys.stdin.readline

#########
N = int(input())
MAP = []
RESULT = []

d = [[0,1],[0,-1],[1,0],[-1,0]]
"""
지도 그리기
"""
for _ in range(N) :
    MAP.append(list(input().strip()))

# print(MAP)
"""
단지 블럭 개수 계산 메서드
"""
def measureArea(y,x) :
    areaBlockCount = 0
    q = deque()
    q.append([y,x])
    MAP[y][x] = "0"
    areaBlockCount += 1
    while q :
        nowY, nowX = q.popleft()
        for i in range(4) :
            nextY = nowY + d[i][0]
            nextX = nowX + d[i][1]
            if (0 <= nextX < N and 0 <= nextY < N) and (MAP[nextY][nextX] == "1") :
                areaBlockCount += 1
                MAP[nextY][nextX] = "0"
                q.append([nextY, nextX])
    RESULT.append(areaBlockCount)

for i in range(N) :
    for k in range(N) :
        if MAP[i][k] == "1" :
            measureArea(i, k)

RESULT.sort()
print(len(RESULT),sep="\n")
for count in RESULT :
    print(count,sep="\n")
#########