import sys
input = sys.stdin.readline
N = int(input())
TIMES = list(map(int, input().split()))

TIMES.sort()

RESULT= [0]*(N+1)

"""
누적합 시켜주기
"""
for i in range(N) :
    RESULT[i+1] = RESULT[i]+TIMES[i]
"""
s = 0
for i in range(N) :
    for k in range(i+1):
        s += time[k]
"""
print(sum(RESULT))