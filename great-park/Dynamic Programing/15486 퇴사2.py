import sys
input = sys.stdin.readline
N = int(input())
# i일까지 일 했을 때의 최대 수익
dp = [0]*(N+1)
schedule = [list(map(int, input().split())) for _ in range(N)]
profit = 0
for i in range(N):
    profit = max(profit, dp[i])
    # 퇴사일 넘김
    if i + schedule[i][0] > N:
        continue

    dp[i+schedule[i][0]] = max(profit + schedule[i][1], dp[i + schedule[i][0]])
print(max(dp))
