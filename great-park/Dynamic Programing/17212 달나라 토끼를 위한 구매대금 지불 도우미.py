import sys
input = sys.stdin.readline
N = int(input())
# i원의 금액을 지불할 최소의 동전 개수
dp = [1e9]*(N+1)
dp[0] = 0
for i in range(1, N+1):
    # dp[i]에 최소값이 담기도록 한다.
    # 순서는 1원 -> 2원 -> 5원 -> 7원
    # 어짜피 모두 검사하여 고려하기 때문에 최솟값이 담긴 후에야 다음 인덱스로 넘어간다.

    dp[i] = dp[i-1] + 1

    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5] + 1)
    if i >= 7:
        dp[i] = min(dp[i], dp[i-7] + 1)

print(dp[-1])
