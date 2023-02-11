# ### My Part ###
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# H,W = map(int, input().split())
# MAP = [[0]*W for _ in range(H)]
# CHECKED = [[False]*W for _ in range(H)]
#
#
# WALLS = list(map(int, input().split()))
# MAX_HEIGHT = max(WALLS)
# print("MAX_HEIGHT : ", MAX_HEIGHT)
# MAX_HEIGHT_POS = WALLS.index(MAX_HEIGHT)
#
# for i in range(W) :
#     for k in range(WALLS[i], 0, -1) :
#         MAP[H-k][i] = -1
#
#
# """
# MAX_HEIGHT부터 돌면 위로 움직일 필요가 없음
# """
# d = [[0, 1],[1, 1],[1, 0],[1,-1],[0,-1]]
# WATER = 0
# # def bfs(y,x) :
# #     global WATER
# #     q = deque()
# #     q.append([y,x])
# #     CHECKED[y][x] = True
# #     while q :
# #         y, x = q.popleft()
# #         for i in range(5) :
# #             ny = y + d[i][0]
# #             nx = x + d[i][1]
# #             if (H-MAX_HEIGHT)<=ny<H and 0<=nx<W and not CHECKED[ny][nx]:
# #                 if MAP[ny][nx] == -1 :
# #                     CHECKED[ny][nx] = True
# #                 elif MAP[ny][nx] == 0 :
# #                     WATER +=1
# #                     MAP[ny][nx] = 2
# #                     CHECKED[ny][nx] = True
# #                 q.append([ny,nx])
# # bfs(H-MAX_HEIGHT, MAX_HEIGHT_POS)
# # print(MAP)
# # print(WATER)
# leftStart = 0
# rightStart = W-1
#
# for i in range(MAX_HEIGHT_POS-leftStart) :
#     leftMax = max(WALLS[leftStart:MAX_HEIGHT_POS])
#     print("leftMax : ",leftMax)
#     for k in range(leftMax):
#         if MAP[(H-1)-k][i] == 0 :
#             WATER += 1
#
# print(WATER)
# print()
# print(rightStart-MAX_HEIGHT_POS)
# for i in range(rightStart-MAX_HEIGHT_POS) : # 0,1,2
#     rightMax = max(WALLS[MAX_HEIGHT_POS+1:W])
#     print("rightMax : ",rightMax)
#     for k in range(rightMax): # 0,1,
#         if MAP[(H-1)-k][(rightStart-1)-i] == 0 :
#             WATER += 1
# print(WATER)
# # for i in range(MAX_HEIGHT_POS) :
# #     for k in range(leftMax) :
# #         if MAP[H-i][k] == 0 :
# #             WATER += 1
# # print(WATER)
# #
# # for i in range(W, MAX_HEIGHT_POS, -1) :
# #     for k in range(rightMax) :
# #         if MAP[H-k][i] == 0 :
# #             WATER += 1
# # print(WATER)
#
#
#
#
#
#
#

### My Part ###
import sys
input = sys.stdin.readline
"""
투 포인터 공부해야겠네요
"""
H,W = map(int, input().split())
WALLS = list(map(int, input().split()))
WATER = 0

MAX_HEIGHT = max(WALLS)
MAX_HEIGHT_POS = WALLS.index(MAX_HEIGHT)

leftPointer = 0
rightPointer = W-1

leftMax = WALLS[leftPointer]
rightMax = WALLS[rightPointer]

"""
왼쪽 포인터가 벽에 도달하기 전까지만 &
오른쪽 포인터가 벽에 도달하기 전까지만
"""
while (leftPointer <= MAX_HEIGHT_POS) and (rightPointer >= MAX_HEIGHT_POS) :
    leftMax = max(leftMax, WALLS[leftPointer])
    rightMax = max(rightMax, WALLS[rightPointer])
    # print("왼쪽 포인터 위치 : ", leftPointer)
    # print("오른쪽 포인터 위치 : ", rightPointer)
    #
    # print()
    # print("왼쪽 ~ 가장 높은벽 전 영역 중 현재까지의 최대 높이 : ", leftMax)
    # print("가장 높은벽 이후 ~ 오른쪽 영역 중 현재까지의 최대 높이 : ", rightMax)
    """
    가장 큰 값에 도달할때까진 서로 움직일 수 밖에 없음
    """
    if leftMax < rightMax :
        """
        만약 현재까지 나온 가장 높은벽보다 낮은 영역을 만나면
        높이 차이만큼 더해주기
        """
        WATER += (leftMax - WALLS[leftPointer])
        leftPointer += 1
    else :
        WATER += (rightMax - WALLS[rightPointer])
        rightPointer -= 1
    # print()

print(WATER)

"""
반례
0 1 0 1 4 1 2 1


                 __
                ㅣ ㅣ   __
       __     __ㅣ ㅣ__ㅣ ㅣ__
    __ㅣ  ㅣ__ㅣ 

"""
# H,W = map(int, input().split())
# MAP = [[0]*W for _ in range(H)]
# CHECKED = [[False]*W for _ in range(H)]
#
#
# WALLS = list(map(int, input().split()))
# MAX_HEIGHT = max(WALLS)
# MAX_HEIGHT_POS = WALLS.index(MAX_HEIGHT)
#
# for i in range(W) :
#     for k in range(WALLS[i], 0, -1) :
#         MAP[H-k][i] = -1
#
# WATER = 0
#
# leftStart = 0
# rightStart = W-1
#
# for i in range(MAX_HEIGHT_POS-leftStart) :
#     leftMax = max(WALLS[leftStart:MAX_HEIGHT_POS])
#     for k in range(leftMax):
#         if MAP[(H-1)-k][i] == 0 :
#             WATER += 1
#
# for i in range(W-(MAX_HEIGHT_POS+1)) :
#     rightMax = max(WALLS[MAX_HEIGHT_POS+1:W])
#     for k in range(rightMax):
#         if MAP[(H-1)-k][(rightStart-1)-i] == 0 :
#             WATER += 1
# print(WATER)