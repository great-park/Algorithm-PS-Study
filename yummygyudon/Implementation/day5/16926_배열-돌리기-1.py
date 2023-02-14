import copy
import sys
input = sys.stdin.readline
from copy import deepcopy

"""
시도 1 : 시간 초과
- deepcopy 연산 & TEMP라는 복사본에도 계속 반복 조회하는 바람에 시간이 오래 걸린 것 같다.
- MATRIX 하나로 갱신하며 사용하고 임시 저장할 단일 값 저장은 temp 변수를 선언해서 사용하면 될 듯
"""
# """
# 반 시계 방향으로 돌리기
# 단, 1칸씩만 옮겨짐(90도가 아니다.)
#
# """
# N, M, R = map(int, input().split())
# MAX_DEPTH = min(N,M)//2
#
# MATRIX = [list(map(int, input().split())) for _ in range(N)]
# """
# < 껍질 돌리듯이 바깥에서부터 안쪽으로 들어가며 돌리기 >
#
# 작은 변의 길이를 기준으로 최대 계층을 구해야함 ( Index Error )
# ( min(N,M) % 2 = 0 이라는 전제가 있기 때문에 반드시 중간 값을 찾을 수 있음. )
# """
# #
# def moveLeft(y, x, depth) :
#     for i in range(depth + 1, N - depth) :
#         """
#         맨 위칸은 제외 -> depth+1부터
#         """
#         y = i
#         TEMP[i][x] = MATRIX[i][x]
#         MATRIX[i][x] = TEMP[i-1][x]
#     return [y, x]
# def moveDown(y, x, depth):
#     for i in range(depth + 1, M - depth):
#         """
#         맨 왼칸은 제외 -> depth+1부터
#         """
#         x = i
#         TEMP[y][i] = MATRIX[y][i]
#         MATRIX[y][i] = TEMP[y][i-1]
#     return [y, x]
# def moveRight(y, x, depth):
#     for i in range(depth + 1, N - depth):
#         """
#         맨 아랫칸은 제외 -> depth+1부터
#         """
#         y = N - i -1
#         TEMP[(N-1)-i][x] = MATRIX[(N-1)-i][x]
#         MATRIX[(N - 1) - i][x] = TEMP[(N-1)-i+1][x]
#
#     return [y, x]
#
# """
# 마지막 연산이기 때문에 return 안해도 됨.
# """
# def moveUp(y, depth):
#     for i in range(depth + 1, M - depth):
#         """
#         맨 오른칸은 제외 -> depth+1부터
#         """
#         TEMP[y][(M-1)-i] = MATRIX[y][(M-1)-i]
#         # MATRIX[y][(M-1)-x] = MATRIX[y][(M-1)-x+1]
#         MATRIX[y][(M - 1) - i] = TEMP[y][(M-1)-i+1]
#
# def rotateMatrix() :
#     for depth in range(MAX_DEPTH) :
#         startY, startX = depth, depth
#         startY, startX = moveLeft(startY, startX, depth)
#         startY, startX = moveDown(startY, startX, depth)
#         startY, startX = moveRight(startY, startX, depth)
#         moveUp(startY, depth)
#
#
# for i in range(1, R+1) :
#     """
#     다돌린 후에 다시 돌 때, 이전 상태의 MATRIX로 새롭게 갱신해서 사용해야 함,.
#     """
#     TEMP = copy.deepcopy(MATRIX)
#     rotateMatrix()
#
# for row in MATRIX :
#     print(*row)

""" 시도 1 출력 Test """
"""
####  1 회 ####
*** Move Left ***
Previous :  1
TEMP[y][x] :  5
1 2 3 4
1 6 7 8
9 10 11 12
13 14 15 16
Previous :  5
TEMP[y][x] :  9
1 2 3 4
1 6 7 8
5 10 11 12
13 14 15 16
Previous :  9
TEMP[y][x] :  13
1 2 3 4
1 6 7 8
5 10 11 12
9 14 15 16

*** Move Down ***
1 2 3 4
1 6 7 8
5 10 11 12
9 13 15 16
1 2 3 4
1 6 7 8
5 10 11 12
9 13 14 16
1 2 3 4
1 6 7 8
5 10 11 12
9 13 14 15

*** Move Right ***
1 2 3 4
1 6 7 8
5 10 11 16
9 13 14 15
1 2 3 4
1 6 7 12
5 10 11 16
9 13 14 15
1 2 3 8
1 6 7 12
5 10 11 16
9 13 14 15

*** Move Up ***
0
Previous :  4
TEMP[y][x] :  3
1 2 4 8
1 6 7 12
5 10 11 16
9 13 14 15
Previous :  3
TEMP[y][x] :  2
1 3 4 8
1 6 7 12
5 10 11 16
9 13 14 15
Previous :  2
TEMP[y][x] :  1
2 3 4 8
1 6 7 12
5 10 11 16
9 13 14 15

*** Move Left ***
Previous :  6
TEMP[y][x] :  10
2 3 4 8
1 6 7 12
5 6 11 16
9 13 14 15

*** Move Down ***
2 3 4 8
1 6 7 12
5 6 10 16
9 13 14 15

*** Move Right ***
2 3 4 8
1 6 11 12
5 6 10 16
9 13 14 15

*** Move Up ***
1
Previous :  7
TEMP[y][x] :  6
2 3 4 8
1 7 11 12
5 6 10 16
9 13 14 15

####  2 회 ####
*** Move Left ***
Previous :  2
TEMP[y][x] :  1
2 3 4 8
2 7 11 12
5 6 10 16
9 13 14 15
Previous :  1
TEMP[y][x] :  5
2 3 4 8
2 7 11 12
1 6 10 16
9 13 14 15
Previous :  5
TEMP[y][x] :  9
2 3 4 8
2 7 11 12
1 6 10 16
5 13 14 15

*** Move Down ***
2 3 4 8
2 7 11 12
1 6 10 16
5 9 14 15
2 3 4 8
2 7 11 12
1 6 10 16
5 9 13 15
2 3 4 8
2 7 11 12
1 6 10 16
5 9 13 14

*** Move Right ***
2 3 4 8
2 7 11 12
1 6 10 15
5 9 13 14
2 3 4 8
2 7 11 16
1 6 10 15
5 9 13 14
2 3 4 12
2 7 11 16
1 6 10 15
5 9 13 14

*** Move Up ***
0
Previous :  8
TEMP[y][x] :  4
2 3 8 12
2 7 11 16
1 6 10 15
5 9 13 14
Previous :  4
TEMP[y][x] :  3
2 4 8 12
2 7 11 16
1 6 10 15
5 9 13 14
Previous :  3
TEMP[y][x] :  2
3 4 8 12
2 7 11 16
1 6 10 15
5 9 13 14

*** Move Left ***
Previous :  7
TEMP[y][x] :  6
3 4 8 12
2 7 11 16
1 7 10 15
5 9 13 14

*** Move Down ***
3 4 8 12
2 7 11 16
1 7 6 15
5 9 13 14

*** Move Right ***
3 4 8 12
2 7 10 16
1 7 6 15
5 9 13 14

*** Move Up ***
1
Previous :  11
TEMP[y][x] :  7
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14

"""


"""
시도 2 : 시도 1 개선
- Python 3 : 시간 초과
- PyPy3 : 통과
"""
N, M, R = map(int, input().split())
MAX_DEPTH = min(N,M)//2

MATRIX = []
for _ in range(N) :
    MATRIX.append(list(map(int, input().split())))

for _ in range(R) :
    for depth in range(MAX_DEPTH) :
        nowY, nowX = depth, depth
        temp = MATRIX[nowY][nowX]
        beforeVal = MATRIX[nowY][nowX]
        """
        한 칸씩 pointer 이동해가기
        
        N-startPos / M-startPos : (위 아래 왼쪽 오른쪽) 모두 한 칸씩 더해져 안쪽으로 들어와야하기 때문
        """
        for i in range(depth + 1, N - depth) : # 왼쪽 변 ( 위 -> 아래 )
            nowY = i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        for i in range(depth + 1, M - depth) : # 아랫 변 ( 왼 -> 오 )
            nowX = i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        for i in range(depth + 1, N - depth):  # 오른쪽 변 ( 아래 -> 위 )
            nowY = (N-1) - i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        for i in range(depth + 1, M - depth) : # 윗 변 ( 오 -> 왼 )
            nowX = (M-1) - i
            temp = MATRIX[nowY][nowX]
            MATRIX[nowY][nowX] = beforeVal
            beforeVal = temp
        # for row in MATRIX:
        #     print(*row)
        # print()

for row in MATRIX :
    print(*row)