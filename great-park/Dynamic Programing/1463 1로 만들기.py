import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * (N+1)

# 한 loop될 떄마다 dp[i]에 3가지 연산에 대해서 가장 작은 값이 담긴다.
# 나누기의 경우 나누어 떨어지지 않을 수 있으니 조건문에서 수행한다.
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)


print(dp[N])
