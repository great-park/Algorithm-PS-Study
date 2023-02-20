import sys
input = sys.stdin.readline
"""
<시도 1>
실패
"""
# BENEFIT_MAP = dict()
# N = int(input())
# for _ in range(N) :
#     benefit, day = map(int, input().split())
#     if day in BENEFIT_MAP.keys() :
#         BENEFIT_MAP[day] = max(BENEFIT_MAP.get(day), benefit)
#     else :
#         BENEFIT_MAP[day] = benefit
# # print(BENEFIT_MAP)
# print(sum(BENEFIT_MAP.values()))

"""
<시도 2>
d 일에만 할 수 있는 것이 아니라
d 일 안에만 와서 하면 되기 때문에
d가 같더라도 할 수 있다.
"""
"""
하지만 이것도 틀렸습니다..
"""
N = int(input())
SUGGEST = []
for _ in range(N) :
    SUGGEST.append(list(map(int, input().split())))

SUGGEST.sort(key = lambda x : (x[1],-x[0]))
from collections import deque
print(SUGGEST)
SUGGEST = deque(SUGGEST)
ACCEPT = []
for _ in range(N) :
    benefit, dueDate = SUGGEST.popleft()
    """
    만약 해당 일자 이전에 돌아야할 강의 수가 적다면 수락
    """
    if dueDate > len(ACCEPT) :
        ACCEPT.append(benefit)
print(sum(ACCEPT))

"""
[[20, 1], [2, 1], [100, 2], [8, 2], [10, 3], [50, 10], [5, 20]]
"""

"""
<시도 3>
내가 찾은 반례
5
3 3
2 3
1 3
100 4
90 4

이처럼 
일자가 작은 순으로 
가능한 강연을 모두 받아 버리면
이후 더 큰 값을 받을 수 있는 강연을 못받을 수도 있다.
"""
N = int(input())
SUGGEST = []
for _ in range(N) :
    SUGGEST.append(list(map(int, input().split())))

SUGGEST.sort(key = lambda x : x[1])
from collections import deque
print(SUGGEST)
SUGGEST = deque(SUGGEST)
ACCEPT = []
for _ in range(N) :
    benefit, dueDate = SUGGEST.popleft()
    """
    일단 마감 일자가 낮은 강연부터 수락
    """
    ACCEPT.append(benefit)
    """
    이득을 정렬하기
    """
    ACCEPT.sort()
    """
    만약 해당 일자 까지 받을 수 있는 이득들의 갯수가
    일자보다 넘칠 경우
    가장 작은 이득을 빼버리기
    """
    if dueDate < len(ACCEPT) :
        ACCEPT.pop(0)

print(sum(ACCEPT))