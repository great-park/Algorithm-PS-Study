import sys
input = sys.stdin.readline
"""
2x1 범위 채우는 경우의 수 : 1
2x2 범위 채우는 경우의 수 : 2
2x3 범위 채우는 경우의 수 : 3
2x4 범위 채우는 경우의 수 : 5
"""
"""
피보나치 수열 규칙 처럼 일정 패턴이 있음
"""
N = int(input())
# CASE = [0] * (N+1) -> 이렇게 하면 IndexError가 나네요;;
CASE = [0] * 1001
CASE[1] = 1
CASE[2] = 2
if N > 2 :
    for c in range(3,N+1) :
        CASE[c] = CASE[c-1] + CASE[c-2]
print(CASE[N] % 10_007)