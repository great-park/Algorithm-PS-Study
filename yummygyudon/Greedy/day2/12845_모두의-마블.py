### My Part ###
import sys
input = sys.stdin.readline

N = int(input())
LEVEL = list(map(int, input().split()))


if N < 3 :
    print(sum(LEVEL))
else :
    LEVEL.sort(reverse=True)
    LEVEL[1] = LEVEL[0] + LEVEL[1]
    for i in range(2,len(LEVEL)) :
        LEVEL[i] = (LEVEL[0] + LEVEL[i]) + LEVEL[i-1]
    print(LEVEL[-1])
# MIX_LEVEL = [0]*(N+1)
# maxScore = 0
# beforeLevel = 0
# MAX = []
#
# # beforeLevel = LEVEL[0]
# for i in range(len(LEVEL)) :
#     beforeLevel = max(LEVEL[i], LEVEL[i+1])
#     if LEVEL
#     maxScore += maxScore + LEVEL[i] # LEVEL[i-1]
#     # maxScore += beforeLevel+LEVEL[i+1]
# print(maxScore)
# MAX.append(maxScore)
# # beforeLevel = LEVEL[-1]
# maxScore = 0
# for i in range(1, len(LEVEL)) : # 1, 2
#     # beforeLevel = max(beforeLevel,LEVEL[i-1])
#     maxScore += LEVEL[-i-1] + LEVEL[-i]
# print(maxScore)
# MAX.append(maxScore)
# print(MAX)
# for i in range()
# print(sum(MIX_LEVEL))


