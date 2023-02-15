import sys
input = sys.stdin.readline

"""
최소 강의실 수 사용 경우의 수를 구하는게 아니라
모든 수업을 할 수 있는 최소한의 강의실 사용량을 구하는 것(겹쳐도 됨 : 1번째 끝나는 시간 <= 2번째 시작하는 시간 같은 강의장 사용)
"""

N = int(input())

LESSON = []
for _ in range(N) :
    # LESSON.append([start,end,abs(start-end)])
    LESSON.append(list(map(int, input().split())))

# LESSON.sort(key=lambda x : x[0])
LESSON.sort()
# print(LESSON)

# nowLessonEnd = 0

"""
시도 1 : 시간 초과
"""
# onTime = []#deque()
# onTime.append(LESSON[0][1])
# count = 1
# for start, end in LESSON[1:] :
#
#     """
#     기존 최솟값보다 더 빨리 끝나는 값이 들어올 경우 대비
#     -> sort해서 매번 가장 일찍 끝나는 시간을 조회해서 start를 비교함
#
#     이미 수업중인 수업중에서 이번에 끝나거나 이미 끝난 수업이 없을 경우, append
#     끝나거나 이미 끝난 수업이 있을 경우 -> 같은 강의실로 이어붙일 수 있다는 것 -> 기존 강의 pop & 이어붙일 강의 append
#     """
#     if onTime[0] <= start :
#         count -= 1
#         onTime.pop(0)
#
#     onTime.append(end)
#     count += 1
#     onTime.sort()
#     # print(onTime)
# print(count)

import heapq
onTime = []
heapq.heappush(onTime, LESSON[0][1])
count = 1
for start, end in LESSON[1:] :
    if onTime[0] <= start :
        heapq.heappop(onTime)
        count -= 1
    heapq.heappush(onTime, end)
    count+=1
# print(onTime)
print(count)