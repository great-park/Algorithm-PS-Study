### My Part ###
"""
2109 순회 강연 문제와 같은 유형
"""
import sys
input = sys.stdin.readline

N = int(input())
ASSIGNMENT = []
for _ in range(N) :
    ASSIGNMENT.append(list(map(int, input().split())))

ASSIGNMENT.sort(key = lambda x : x[0])

from collections import deque
ASSIGNMENT = deque(ASSIGNMENT)
SCORE = []

for _ in range(N) :
    dueDate, score = ASSIGNMENT.popleft()
    SCORE.append(score)
    SCORE.sort()
    if dueDate < len(SCORE) :
        SCORE.pop(0)

print(sum(SCORE))