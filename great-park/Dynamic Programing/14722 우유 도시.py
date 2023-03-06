import sys
input = sys.stdin.readline
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(N) for _ in range(N)]

if city[0][0] == 0:
    dp[0][0] = 1
""" 
  city
  0 -> 1 -> 2 -> 0 -> 1 -> 2

  dp
  1 -> 2 -> 3 -> 4 -> 5 -> 6
"""
for i in range(1, N):
    if city[i][0] == dp[i-1][0] % 3:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    # dp[i][0] = dp[i-1][0] + 1 if city[i][0] == dp[i-1][0] % 3 else dp[i-1][0]

    if city[0][i] == dp[0][i-1] % 3:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1]
"""
  [1, 2, 3, 3]
  [2, 0, 0, 0]
  [3, 0, 0, 0]
  [4, 0, 0, 0]
"""


for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # from 왼쪽 or 위쪽
        if city[i][j] == dp[i][j] % 3:
            dp[i][j] += 1
print(dp[N-1][N-1])
