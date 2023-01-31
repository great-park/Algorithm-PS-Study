from collections import deque
import sys
input = sys.stdin.readline


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N = int(input())

"""
방식 1 : 함수 분리
"""
blindColor = ["G", "R"]

MAP = []
for _ in range(N) :
    MAP.append(list(input().rstrip()))

VISITED_COMMON = [[False]*N for _ in range(N)]
VISITED_BLIND = [[False]*N for _ in range(N)]

COMMON_COUNT = 0
BLIND_COUNT = 0


"""
정상인 대상의 영역 계산 BFS 함수
"""
def bfsForCommon(y, x, color) :
    q = deque()
    q.append([y,x])
    VISITED_COMMON[y][x] = True
    while q :
        nowY, nowX = q.popleft()
        for i in range(4) :
            nextY = nowY + d[i][0]
            nextX = nowX + d[i][1]
            if 0 <= nextY < N and 0 <= nextX < N and MAP[nextY][nextX] == color and not VISITED_COMMON[nextY][nextX] :
                count += 1
                VISITED_COMMON[nextY][nextX] = True
                q.append([nextY, nextX])

"""
색약 장애인 대상의 색구분 결과 반환 함수
"""
def isSeemLikeSameArea(searchColor, nextColor):
    """
    Blue 영역을 계산하는 BFS 중일 때는
    기존 방식대로 같은지 비교한 boolean 값

    만약 Red 나 Green 일 때는
    다음 값이 Red나 Green이면 가능하기 때문에
    nextColor가 blindColor 안에 포함되는지에 대한 여부
    """
    if searchColor == "B":
        return searchColor == nextColor
    else:
        return nextColor in blindColor

def bfsForColorBlind(y, x, color) :
    q = deque()
    q.append([y, x])
    VISITED_BLIND[y][x] = True
    while q :
        nowY, nowX = q.popleft()
        for i in range(4):
            nextY = nowY + d[i][0]
            nextX = nowX + d[i][1]
            if 0 <= nextY < N and 0 <= nextX < N and isSeemLikeSameArea(color, MAP[nextY][nextX]) and not VISITED_BLIND[nextY][nextX]:
                count += 1
                VISITED_BLIND[nextY][nextX] = True
                q.append([nextY, nextX])
"""
각 블럭에 대해 
조건문1 : 정상인 VISITED를 사용한 정상인 영역 구분 연산 
조건문2 : 색약장애인 VISITED를 사용한 색약 장애인 영역 구분 연산 
"""
for i in range(N) :
    for k in range(N) :
        if not VISITED_COMMON[i][k] :
            COMMON_COUNT += 1
            bfsForCommon(i, k, MAP[i][k])

        if not VISITED_BLIND[i][k] :
            BLIND_COUNT += 1
            bfsForColorBlind(i, k, MAP[i][k])

print(COMMON_COUNT, BLIND_COUNT, sep=" ")


"""
방식 2 : 전용 지도로 변환하여 사용
"""
COMMON_MAP = []
BLIND_MAP = [[] for _ in range(N)]

BLIND_COLOR = ["R", "G"]

for i in range(N) :
    line = list(input().rstrip())
    COMMON_MAP.append(line)
    for k in range(N) :
        """
        R 이나 G 일 경우, RG라는 값으로 통일시켜 치환한 다음에 삽입
        """
        if line[k] in BLIND_COLOR :
            BLIND_MAP[i].append("RG")
        else :
            BLIND_MAP[i].append(line[k])

"""
전용 탐색 체크 리스트
"""
VISITED_COMMON = [[False]*N for _ in range(N)]
VISITED_BLIND = [[False]*N for _ in range(N)]

COMMON_COUNT = 0
BLIND_COUNT = 0

"""
좌표, 탐색 영역 그룹핑 기준 색, 방문 여부 체크 리스트, 전용 MAP
"""
def bfs(y, x, color, visited, map) :
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    while q :
        nowY, nowX = q.popleft()
        for i in range(4) :
            nextY = nowY + d[i][0]
            nextX = nowX + d[i][1]
            if 0 <= nextY < N and 0 <= nextX < N and map[nextY][nextX] == color and not visited[nextY][nextX] :
                visited[nextY][nextX] = True
                q.append([nextY, nextX])
    return map, visited

for i in range(N) :
    for k in range(N) :
        """
        - 각 상황별 count 누적합
        - 지도 및 체크리스트 갱신
        별개로 독립하여 계산해야하기 때문에 if~elif 가 아닌 if~if~ 로 사용해야함.
        1. 색약의 입장에서
        2. 일반인 입장에서
        """
        if not VISITED_BLIND[i][k] :
            BLIND_COUNT += 1
            BLIND_MAP, VISITED_BLIND =  bfs(i, k, BLIND_MAP[i][k], VISITED_BLIND, BLIND_MAP)
        if not VISITED_COMMON[i][k] :
            COMMON_COUNT += 1
            COMMON_MAP, VISITED_COMMON = bfs(i, k, COMMON_MAP[i][k], VISITED_COMMON, COMMON_MAP)

print(COMMON_COUNT, BLIND_COUNT, sep=" ")
