import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
SCHEDULES = []
for _ in range(N) :
    SCHEDULES.append(list(map(int, input().split())))

"""
역시 배열은 입력 최댓값만큼 만들어놓는게 제일 편하네요...ㅎㅎ
최적화하려다가 Index Error가 꼐속 발생해서
-> *366으로 생성했습니다
"""
# SCHEDULES.sort(key=lambda x : (x[0], x[1]))
# SCHEDULES = deque(SCHEDULES)

# MAX_PERIOD = SCHEDULES[-1][1]
# CHECKED = [0] * (MAX_PERIOD + 2)
CHECKED = [0] * 366
AREA = 0
width, height = 0, 0
for schedule in SCHEDULES :
    for i in range(schedule[0], schedule[1]+1) :
        CHECKED[i] += 1

# print(CHECKED)
for i in range(1, 366) :
    if CHECKED[i] == 0 :
        AREA += (width*height)
        width, height = 0, 0
        continue
    if CHECKED[i] > 0 :
        width += 1
        height = max(height, CHECKED[i])
AREA += (width*height)

print(AREA)
# QUEUE = deque()
# while SCHEDULES :
#     startDate, endDate = SCHEDULES.popleft()
#     if startDate < start :
#         height += 1
