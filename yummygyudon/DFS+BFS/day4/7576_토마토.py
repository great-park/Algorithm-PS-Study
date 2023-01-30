from collections import deque
import sys
input = sys.stdin.readline
"""
보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수
"""
"""
인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향
- 인접한 곳 : 왼쪽, 오른쪽, 앞, 뒤 네 방향 (대각선은 영향 x)
"""

M, N = map(int, input().split())
BOX = []
TOMATO_POS = []
d = [[0, 1],[0, -1],[-1, 0],[1, 0]]
POSSIBLE = True

for i in range(N) :
    tomatoLine = list(map(int, input().split()))
    BOX.append(tomatoLine)
    for k in range(M) :
        if tomatoLine[k] == 1 :
            TOMATO_POS.append([i,k])

""" CASE 1 : VISITED 안쓰는 방법 / 값 비교를 통한 최솟값 설정 -> 예제 통과를 했지만 브루트포스 방식이기 때문에 '시간초과' """
# def ripeningTomato(tomatoPostion:list) :
#     global BOX
#     q = deque()
#     q.append([tomatoPostion[0], tomatoPostion[1], 0])
#     while q:
#         y, x, move = q.popleft()
#         for i in range(4):
#             n_y = y + d[i][0]
#             n_x = x + d[i][1]
#             if (0 <= n_y < N) and (0 <= n_x < M) and BOX[n_y][n_x] >= 0:
#                 if (BOX[n_y][n_x] > move) or (BOX[n_y][n_x] == 0):
#                     BOX[n_y][n_x] = move + 1
#                     q.append([n_y, n_x, move + 1])

""" CASE 2 : VISITED 쓰고 값비교까지 활용 -> 최하단의 과거 제출 코드 소요시간의 절반 절약( 3960ms to 1948ms ) """
VISITED = [[False]*M for _ in range(N)]
def ripeningTomato(tomatoPostionList:list) :
    global BOX
    q = deque()
    for position in tomatoPostionList :
        q.append([position[0], position[1], 0])
        VISITED[position[0]][position[1]] = True
    while q:
        y, x, move = q.popleft()
        for i in range(4):
            n_y = y + d[i][0]
            n_x = x + d[i][1]
            if (0 <= n_y < N) and (0 <= n_x < M) and not (BOX[n_y][n_x] == -1) and not VISITED[n_y][n_x]:
                VISITED[n_y][n_x] = True
                BOX[n_y][n_x] = move+1
                q.append([n_y, n_x, move + 1])

"""
박스 안에 가장 큰 값이 가장 최소 경과 시간
"""
def calcResult(box) :
    MAX = -1e9
    for line in box :
        for block in line :
            """
            단 1개라도 익지 않았다면 -1 반환
            """
            if block == 0 :
                return -1
            """
            더 큰 값이 나타날때마다 MAX 값 갱신
            """
            if block > MAX :
                MAX = block
    """
    MAX가 1이라는 것은 시작 완숙 토마토에서 더이상 퍼져나가지 못하는 상황 (완숙 토마토 1개 + 빈 칸만 있는 경우)
    """
    if MAX == 1 :
        return 0
    """
    if MAX == 1 조건문이나 if block == 0 조건문에 걸리지 않았다면
    갱신했던 MAX값 반환
    """
    return MAX

ripeningTomato(TOMATO_POS)
print(calcResult(BOX))


"""CASE 2에서 사용하는 로직"""
# for pos in TOMATO_POS:
#     ripeningTomato(pos)

# MAX = -1e9
# for i in range(N):
#     for k in range(M):
#         if BOX[i][k] == 0 :
#             POSSIBLE = False
#             break
#         if BOX[i][k] > MAX :
#             MAX = BOX[i][k]
# if POSSIBLE :
#     if MAX == 1 :
#         print(0)
#     else :
#         print(MAX)
# else :
#     print(-1)


"""
과거 제출
"""
# import sys
# input = sys.stdin.readline
# M, N = map(int, input().split())
# box = []
# pos = []
# visited = [[0]*M for _ in range(N)]
# time = [[1e9]*M for _ in range(N)]
# for i in range(N):
#     box.append(list(map(int, input().split())))
#     for k in range(M) :
#         if box[i][k] == 1 :
#             pos.append([i, k])
#             visited[i][k] = 1
#             time[i][k] = 0
#
# d = [[0, 1],[0, -1],[1, 0],[-1, 0]]
#
# from collections import deque
# q = deque()
# for i in range(len(pos)) :
#     q.append([pos[i][0], pos[i][1], 0])
# while q :
#     h, w, tm = q.popleft()
#     for i in range(4) :
#         next_h = h + d[i][0]
#         next_w = w + d[i][1]
#         if 0 <= next_h < N and 0 <= next_w < M and visited[next_h][next_w] == 0 and box[next_h][next_w] != -1:
#             q.append([next_h, next_w, tm+1])
#             time[next_h][next_w] = tm+1
#             visited[next_h][next_w] = 1
#
# mx = -1
# for i in range(N):
#     for k in range(M) :
#         if box[i][k] == -1 :
#             continue
#         elif time[i][k] == 1e9 and box[i][k] == 0 :
#             print(-1)
#             sys.exit()
#         else :
#             mx = max(mx, time[i][k])
# print(mx)




