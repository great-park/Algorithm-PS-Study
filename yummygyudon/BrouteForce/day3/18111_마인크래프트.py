import sys
input = sys.stdin.readline
N, M, BLOCK_QUANT = map(int, input().split())
MAP = []
MAX_HEIGHT, MIN_HEIGHT = -1e9, 1e9
for _ in range(N) :
    line = list(map(int, input().split()))
    MAX_HEIGHT = max(MAX_HEIGHT, max(line))
    MIN_HEIGHT = min(MIN_HEIGHT, min(line))
    MAP.append(line)
print(MAX_HEIGHT)
print(MIN_HEIGHT)
"""
BFS 방식 시도 - 실패
"""
# WASTE_TIME = 0
# d = [[1,0], [0,1], [-1,0], [0,-1]]
#
# COMMAND = dict()
# # Remove : 블록 제거 & 인벤토리에 넣기
# COMMAND['R'] = 2
# # Stack : 인벤토리에서 꺼내 쌓기
# COMMAND['S'] = 1
#
# from queue import PriorityQueue
# def startLevelingOn(y,x, blockQuantity) :
#     # global WASTE_TIME
#     # if MAP[y][x] == level :
#     #     WASTE_TIME
#
#     LEVEL = MAP[y][x] # 기준 레벨
#     CHECKED = [[False] * M for _ in range(N)]
#     q = PriorityQueue()
#     #높은 것 먼저 해야 하기 때문에 음수화
#     q.put([-LEVEL,y,x])
#     CHECKED[y][x] = True
#     TIME = 0
#     lessBlock = False
#     print("기준 좌표 : [ %d, %d ]" % (y, x))
#     print("기준 좌표 높이 : ", LEVEL)
#     """
#
#     """
#     while q :
#         nowLevel, nowY, nowX = q.get()
#         nowLevel = -(nowLevel)
#         print("현재 좌표 : [ %d, %d ]"%(nowY,nowX))
#         print("현재 좌표 높이 : ", nowLevel)
#         if MAP[nowY][nowX] > LEVEL:
#             print("삭제 및 인벤토리 저장")
#             waste, blockQuantity = remove(nowLevel, LEVEL, blockQuantity)
#         elif MAP[nowY][nowX] < LEVEL and blockQuantity > 0:
#             # if blockQuantity <= 0 :
#             #     lessBlock = True
#             #     break
#             print("인벤토리 반출 및 적재")
#             waste, blockQuantity = stack(nowLevel, LEVEL, blockQuantity)
#         else :
#             print("기준 높이와 동일 높이")
#             waste, blockQuantity = 0, blockQuantity
#         TIME += waste
#         print("현재 소요시간 : ",TIME)
#         print()
#         for i in range(4):
#             nextY = d[i][0]
#             nextX = d[i][1]
#             if 0<=nextY<N and 0<=nextX<M and not CHECKED[nextY][nextX] :
#                 CHECKED[nextY][nextX] = True
#                 q.put([-(MAP[nextY][nextX]), nextY, nextX])

#
# def stack(nowLevel, targetLevel, blockQuantity) :
#     haveToStack = targetLevel-nowLevel
#     return (haveToStack*COMMAND.get('S'), blockQuantity-haveToStack)
#
# def remove(nowLevel, targetLevel, blockQuantity) :
#     haveToRemove = nowLevel-targetLevel
#     return (haveToRemove*COMMAND.get('R'), blockQuantity+haveToRemove)
#
# for i in range(N) :
#     for k in range(M) :
#         startLevelingOn(i,k, BLOCK_QUANT)

BEST_TIME = 1e9
BEST_TIME_LEVEL = 0
"""
최저층 ~ 최고층까지 각 층에 맞춰 땅 고르기 해보기
-> 상단 MIN, MAX 값 구하는 연산 -> 시간 초과 요인
-> 최대 가능 높이인 0 ~ 257로 돌아야 통과됨.
"""
for level in range(MIN_HEIGHT, MAX_HEIGHT+1) :
    print("%d층 땅 고르기 시작!"%level)
    haveToRemove = 0
    haveToStack = 0
    for i in range(N):
        for k in range(M) :
            if MAP[i][k] > level :
                haveToRemove += MAP[i][k] - level

            else :
                """
                elif MAP[i][k] < level :
                elif 로 조건문 연산 -> 시간 초과 요인
                """
                haveToStack += level - MAP[i][k]
    """
    (기존에 가진 블록 - 인벤토리에서 꺼내야 할 블록 갯수 + 인벤토리에 채울 블록 갯수)가 0보다 커야 고르기를 할 수 있음
    0개보다 여유있거나 0개로 딱 맞아 떨어지면 가능하다는 의미
    """
    if BLOCK_QUANT - haveToStack + haveToRemove >= 0 :
        """
        만약 이전 층에서 나올 수 있는 최소 시간보다 작으면 갱신
        
        ++ 답이 여러 개 있다면 : 시간이 같다면 -> 그중에서 땅의 높이가 가장 높은 것 
        -> for 문으로 한층씩 올라가기 때문에 자동으로 앞 전에 낮은 층에서의 경우와 시간이 같을 경우가 나오면(조건문 : <= BEST_TIME)
         높은 층으로 저장됨
        """
        if ((haveToStack*1) + (haveToRemove*2)) <= BEST_TIME :
            # Stack 작업 소요 시간 + Remove 작업 소요 시간
            BEST_TIME = ((haveToStack*1) + (haveToRemove*2))
            BEST_TIME_LEVEL = level
# print(BEST_TIME)
# print(BEST_TIME_LEVEL)
print("%d %d"%(BEST_TIME, BEST_TIME_LEVEL))
