from collections import deque
import heapq
import sys
input = sys.stdin.readline
"""<1차 시도 : 매개변수 쓰기>"""
# def startGame(pos_subin, pos_bro) :
#     q = deque()
#     q.append([0, pos_subin])
#     while q :
#         time, nowPosition = q.popleft()
#         visited[nowPosition] = True
#         if (nowPosition == pos_bro) :
#             print(time)
#             break
#         if not visited[nowPosition + 1] :
#             q.append([time + 1, nowPosition+1])
#         if not visited[nowPosition - 1] :
#             q.append([time + 1, nowPosition - 1])
#         if not visited[nowPosition * 2] :
#             q.append([time + 1, nowPosition * 2])
#
# pos_subin, pos_bro = map(int, input().split())
# startGame(pos_subin, pos_bro)

"""<2차 시도 : 전역변수 쓰기>"""
# POS_SUBIN, POS_BROTHER = map(int, input().split())
# def startGame() :
#     q = deque()
#     q.append([0, POS_SUBIN])
#     while q :
#         time, nowPosition = q.popleft()
#         if (nowPosition == POS_BROTHER) :
#             print(time)
#             break
#         q.append([time + 1, nowPosition+1])
#         q.append([time + 1, nowPosition-1])
#         q.append([time + 1, nowPosition*2])
#
# startGame()

"""<3차 시도 : 계산 이력 체크로 동일 값 중복 계산 방지> -> 런타임 에러 -> 수정 통과"""
# visited = [False]*100_001
# def startGame(pos_subin, pos_bro) :
#     q = deque()
#     q.append([0, pos_subin])
#     while q :
#         time, nowPosition = q.popleft()
#         visited[nowPosition] = True
#         if (nowPosition == pos_bro) :
#             print(time)
#             break
#         if not visited[nowPosition + 1] :
#             q.append([time + 1, nowPosition+1])
#         if not visited[nowPosition - 1] :
#             q.append([time + 1, nowPosition - 1])
#         if not visited[nowPosition * 2] :
#             q.append([time + 1, nowPosition * 2])
#
# pos_subin, pos_bro = map(int, input().split())
# startGame(pos_subin, pos_bro)

"""<4차 시도 : 이동 횟수 & 계산 이력 & 한계값 동시 체크 + 체크리스트 값으로 확인까지> -> 런타임 에러 -> 수정 통과"""
# HISTORY = [0]*100_001
# LIMIT = 100_000
# def startGame(pos_subin, pos_bro) :
#     q = deque()
#     q.append(pos_subin)
#     while q :
#         nowPosition = q.popleft()
#         if (nowPosition == pos_bro) :
#             print(HISTORY[nowPosition])
#             break
#         """
#          == 0 논리 연산으로 중복 계산 방지 ( 최초 계산일 경우에만 append )
#         """
#         positionValue = HISTORY[nowPosition]
#         if (HISTORY[nowPosition + 1] == 0) and (0 <= (nowPosition + 1) <= LIMIT) :
#             HISTORY[nowPosition + 1] = positionValue+1
#             q.append(nowPosition + 1)
#         if (HISTORY[nowPosition - 1] == 0) and (0 <= (nowPosition - 1) <= LIMIT) :
#             HISTORY[nowPosition - 1] = positionValue + 1
#             q.append(nowPosition - 1)
#         if (HISTORY[nowPosition * 2] == 0) and (0 <= (nowPosition * 2) <= LIMIT) :
#             HISTORY[nowPosition * 2] = positionValue + 1
#             q.append(nowPosition * 2)
#
# pos_subin, pos_bro = map(int, input().split())
# startGame(pos_subin, pos_bro)

# HISTORY = [0]*100_001
# LIMIT = 100_000
# pos_subin, pos_bro = map(int, input().split())
#
# q = deque()
# q.append(pos_subin)
# while q :
#     nowPosition = q.popleft()
#     if (nowPosition == pos_bro) :
#         print(HISTORY[nowPosition])
#         break
#     """
#      == 0 논리 연산으로 중복 계산 방지 ( 최초 계산일 경우에만 append )
#     """
#     positionValue = HISTORY[nowPosition]
#     if (HISTORY[nowPosition + 1] == 0) and (0 <= (nowPosition + 1) <= LIMIT) :
#         HISTORY[nowPosition + 1] = positionValue+1
#         q.append(nowPosition + 1)
#
#     if (HISTORY[nowPosition - 1] == 0) and (0 <= (nowPosition - 1) <= LIMIT) :
#         HISTORY[nowPosition - 1] = positionValue + 1
#         q.append(nowPosition - 1)
#
#     if (HISTORY[nowPosition * 2] == 0) and (0 <= (nowPosition * 2) <= LIMIT) :
#         HISTORY[nowPosition * 2] = positionValue + 1
#         q.append(nowPosition * 2)

"""
논리 연산 순서가 문제였습니닼ㅋㅋㅋㅋㅋㅋㅋ nowPostion의 값 범위를 먼저 확인해야함.

++ 전역변수를 사용한 경우가 메모리를 8KB 절약됨
++ 함수와 전역 변수를 사용한 경우 & positionValue = HISTORY[nowPosition] 처럼 각 if문에 쓰이는 값을
  변수로 선언하여 사용하면 메모리 1000KB 이상 절약 & 시간 20ms 가량 절약
"""

############ 정답 Zone ############
""" 정답 1 : 전역변수 사용 & 함수화 & Deque """
# HISTORY = [0]*100001
# LIMIT = 100000
# SUJIN, BROTHER = map(int, input().split())
# def startGame() :
#     q = deque()
#     q.append(SUJIN)
#     while q :
#         nowPosition = q.popleft()
#         if (nowPosition == BROTHER) :
#             print(HISTORY[nowPosition])
#             break
#         """
#          == 0 논리 연산으로 중복 계산 방지 ( 최초 계산일 경우에만 append )
#         3개의 조건문에서 사용되는 동일 값에 대하여 변수 선언 -> 조회 시간 절약
#         """
#         positionValue = HISTORY[nowPosition]
#         if (0 <= (nowPosition + 1) <= LIMIT) and (HISTORY[nowPosition + 1] == 0) :
#             HISTORY[nowPosition + 1] = positionValue+1
#             q.append(nowPosition + 1)
#         if (0 <= (nowPosition - 1) <= LIMIT) and (HISTORY[nowPosition - 1] == 0) :
#             HISTORY[nowPosition - 1] = positionValue + 1
#             q.append(nowPosition - 1)
#         if (0 <= (nowPosition * 2) <= LIMIT) and (HISTORY[nowPosition * 2] == 0) :
#             HISTORY[nowPosition * 2] = positionValue + 1
#             q.append(nowPosition * 2)
#
# startGame()

""" 정답 2 : 매개변수 사용 & 함수화 & Deque """
# HISTORY = [0]*100001
# LIMIT = 100000
# def startGame(pos_sujin, pos_bro) :
#     q = deque()
#     q.append(pos_sujin)
#     while q :
#         nowPosition = q.popleft()
#         if (nowPosition == pos_bro) :
#             print(HISTORY[nowPosition])
#             break
#         """
#          == 0 논리 연산으로 중복 계산 방지 ( 최초 계산일 경우에만 append )
#         """
#         positionValue = HISTORY[nowPosition]
#         if (0 <= (nowPosition + 1) <= LIMIT) and (HISTORY[nowPosition + 1] == 0) :
#             HISTORY[nowPosition + 1] = positionValue+1
#             q.append(nowPosition + 1)
#         if (0 <= (nowPosition - 1) <= LIMIT) and (HISTORY[nowPosition - 1] == 0) :
#             HISTORY[nowPosition - 1] = positionValue + 1
#             q.append(nowPosition - 1)
#         if (0 <= (nowPosition * 2) <= LIMIT) and (HISTORY[nowPosition * 2] == 0) :
#             HISTORY[nowPosition * 2] = positionValue + 1
#             q.append(nowPosition * 2)
#
# pos_sujin, pos_bro = map(int, input().split())
# startGame(pos_sujin, pos_bro)

""" 정답 3 : 전역변수 사용 & 함수화 & Heap -> 메모리&시간 효율이 비교적 낮음"""
VISITED = [False]*100001
LIMIT = 100000
SUJIN, BROTHER = map(int, input().split())
def startGame() :
    heap = []
    heapq.heappush(heap, [0, SUJIN])
    VISITED[SUJIN] = True
    while heap :
        time, nowPosition = heapq.heappop(heap)
        if (nowPosition == BROTHER) :
            print(time)
            break
        if (0 <= (nowPosition + 1) <= LIMIT) and not VISITED[nowPosition + 1]:
            VISITED[nowPosition + 1] = True
            heapq.heappush(heap, [time + 1, nowPosition + 1])
        if (0 <= (nowPosition - 1) <= LIMIT) and not VISITED[nowPosition - 1]:
            VISITED[nowPosition - 1] = True
            heapq.heappush(heap, [time + 1, nowPosition - 1])
        if (0 <= (nowPosition * 2) <= LIMIT) and not VISITED[nowPosition * 2]:
            VISITED[nowPosition * 2] = True
            heapq.heappush(heap, [time + 1, nowPosition * 2])

startGame()