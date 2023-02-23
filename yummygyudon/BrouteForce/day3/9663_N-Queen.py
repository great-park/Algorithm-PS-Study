import sys
input = sys.stdin.readline

N = int(input())

EACH_ROW = [0]*N
# 매 열 시작마다 필요한 리스트 -> 재귀 돌아올 때 다시 False로 초기화 필요
EACH_COLUMN = [False]*N

CASE = 0
def nQueen(nowRow) :
    global CASE
    """
    N까지 갔다는 것 : N-1을 넘었다는 것 : 마지막 줄까지 잘 도착했다는 것
    """
    # print("지금부터 %d행 시작"%nowRow)
    if nowRow == N :
        CASE += 1
        return
    for column in range(N) :
        # 아직 안간 열이면
        if not EACH_COLUMN[column] :
            # print("지금부터 %d열 시작"%column)
            # 현재 행 내 해당 열에 퀸을 놓는다고 가정
            EACH_ROW[nowRow] = column
            # print("EACH ROW = ",EACH_ROW)
            if checkIsPossible(nowRow) :
                EACH_COLUMN[column] = True
                # print("EACH COLUMN = ", EACH_COLUMN)
                nQueen(nowRow+1)
                EACH_COLUMN[column] = False
    # print()

def checkIsPossible(nowRow) :
    for i in range(nowRow) :
        if EACH_ROW[i] == EACH_ROW[nowRow] or (nowRow-i == abs(EACH_ROW[nowRow]-EACH_ROW[i])) :
            return False
    return True

nQueen(0)
print(CASE)
"""
4
지금부터 0행 시작
지금부터 0열 시작
EACH ROW =  [0, 0, 0, 0]
EACH COLUMN =  [True, False, False, False]
지금부터 1행 시작
지금부터 1열 시작
EACH ROW =  [0, 1, 0, 0]
지금부터 2열 시작
EACH ROW =  [0, 2, 0, 0]
EACH COLUMN =  [True, False, True, False]
지금부터 2행 시작
지금부터 1열 시작
EACH ROW =  [0, 2, 1, 0]
지금부터 3열 시작
EACH ROW =  [0, 2, 3, 0]

지금부터 3열 시작
EACH ROW =  [0, 3, 3, 0]
EACH COLUMN =  [True, False, False, True]
지금부터 2행 시작
지금부터 1열 시작
EACH ROW =  [0, 3, 1, 0]
EACH COLUMN =  [True, True, False, True]
지금부터 3행 시작
지금부터 2열 시작
EACH ROW =  [0, 3, 1, 2]

지금부터 2열 시작
EACH ROW =  [0, 3, 2, 2]


지금부터 1열 시작
EACH ROW =  [1, 3, 2, 2]
EACH COLUMN =  [False, True, False, False]
지금부터 1행 시작
지금부터 0열 시작
EACH ROW =  [1, 0, 2, 2]
지금부터 2열 시작
EACH ROW =  [1, 2, 2, 2]
지금부터 3열 시작
EACH ROW =  [1, 3, 2, 2]
EACH COLUMN =  [False, True, False, True]
지금부터 2행 시작
지금부터 0열 시작
EACH ROW =  [1, 3, 0, 2]
EACH COLUMN =  [True, True, False, True]
지금부터 3행 시작
지금부터 2열 시작
EACH ROW =  [1, 3, 0, 2]
EACH COLUMN =  [True, True, True, True]
지금부터 4행 시작

지금부터 2열 시작
EACH ROW =  [1, 3, 2, 2]


지금부터 2열 시작
EACH ROW =  [2, 3, 2, 2]
EACH COLUMN =  [False, False, True, False]
지금부터 1행 시작
지금부터 0열 시작
EACH ROW =  [2, 0, 2, 2]
EACH COLUMN =  [True, False, True, False]
지금부터 2행 시작
지금부터 1열 시작
EACH ROW =  [2, 0, 1, 2]
지금부터 3열 시작
EACH ROW =  [2, 0, 3, 2]
EACH COLUMN =  [True, False, True, True]
지금부터 3행 시작
지금부터 1열 시작
EACH ROW =  [2, 0, 3, 1]
EACH COLUMN =  [True, True, True, True]
지금부터 4행 시작


지금부터 1열 시작
EACH ROW =  [2, 1, 3, 1]
지금부터 3열 시작
EACH ROW =  [2, 3, 3, 1]

지금부터 3열 시작
EACH ROW =  [3, 3, 3, 1]
EACH COLUMN =  [False, False, False, True]
지금부터 1행 시작
지금부터 0열 시작
EACH ROW =  [3, 0, 3, 1]
EACH COLUMN =  [True, False, False, True]
지금부터 2행 시작
지금부터 1열 시작
EACH ROW =  [3, 0, 1, 1]
지금부터 2열 시작
EACH ROW =  [3, 0, 2, 1]
EACH COLUMN =  [True, False, True, True]
지금부터 3행 시작
지금부터 1열 시작
EACH ROW =  [3, 0, 2, 1]


지금부터 1열 시작
EACH ROW =  [3, 1, 2, 1]
EACH COLUMN =  [False, True, False, True]
지금부터 2행 시작
지금부터 0열 시작
EACH ROW =  [3, 1, 0, 1]
지금부터 2열 시작
EACH ROW =  [3, 1, 2, 1]

지금부터 2열 시작
EACH ROW =  [3, 2, 2, 1]
"""
