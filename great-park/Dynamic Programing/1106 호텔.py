import sys
input = sys.stdin.readline
C, N = map(int, input().split())
info = []
for i in range(N):
    cost, p = map(int, input().split())
    info.append([cost, p])
info.sort()

# 해당 인원만큼 고객이 늘어날 때 드는 최소 비용
dp = [1e9]*(C+101)
dp[0] = 0


for cost, p in info:
    for i in range(p, len(dp)):
        dp[i] = min(dp[i-p] + cost, dp[i])
print(min(dp[C:]))
