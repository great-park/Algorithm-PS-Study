"""
- 점(',') : 빈 필드
- 샾('#') : 울타리
- 'o' : 양
- 'v' : 늑대
"""
from collections import deque
import sys
input = sys.stdin.readline

EMPTY_FIELD = "."
SHEEP = "o"
WOLF = "v"
HEDGE = "#"

STATE = {"o" : 0, "v" : 0}

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

R, C = map(int, input().split())
MAP = []
for _ in range(R) :
    MAP.append(list(input().rstrip()))
CHECKED = [[False]*C for _ in range(R)]
def bfs(sheep_y, sheep_x) :
    sheepCount = 0
    wolfCount = 0
    q = deque()
    q.append([sheep_y, sheep_x])
    CHECKED[sheep_y][sheep_x] = True
    while q:
        y, x = q.popleft()
        """
        해당 위치가 양이라면 sheepCount에 누적합
        해당 위치가 늑대라면 wolfCount에 누적합
        """
        if MAP[y][x] == SHEEP :
            sheepCount += 1
        elif MAP[y][x] == WOLF :
            wolfCount += 1
        for i in range(4):
            nextY = y + d[i][0]
            nextX = x + d[i][1]
            """
            다음칸이 울타리(HEDGE)가 아니면서 -> 각 bfs마다 같은 영역을 돌 수 있음
            & 처음 방문하는 경우
            """
            if (0 <= nextY < R) and (0 <= nextX < C) and not MAP[nextY][nextX] == HEDGE and not CHECKED[nextY][nextX] :
                CHECKED[nextY][nextX] = True
                q.append([nextY, nextX])
    # print(sheepCount, wolfCount, sep=" ")
    """
    양 수와 늑대 수를 비교한 boolean 값을 활용해서 살아남은 개체에 대해 dict의 값에 누적합
    
    양의 수 > 늑대의 수 -> 늑대는 더하지 않음
    늑대의 수 > 양의 수 -> 양은 더하지 않음
    """
    sheepAlive = (sheepCount > wolfCount)
    if not sheepAlive :
        STATE[WOLF] = STATE.get(WOLF) + wolfCount
    else :
        STATE[SHEEP] = STATE.get(SHEEP) + sheepCount


for i in range(R) :
    for k in range(C) :
        if (MAP[i][k] == SHEEP or MAP[i][k] == WOLF) and not CHECKED[i][k] :
            bfs(i, k)

print(STATE[SHEEP], STATE[WOLF], sep=" ")