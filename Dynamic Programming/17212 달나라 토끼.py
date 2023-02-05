n = int(input())
dp = [100001]*(n+1) #지불해야 하는 금액의 MAX
dp[0] = 0 #0원은 동전 0개로 가능
coin = [7, 5, 2, 1] #동전 종류

for money in range(1, n + 1):
    for c in coin:
        if c <= money and dp[money - c] + 1 < dp[money]:
            dp[money] = dp[money - c] + 1

print(dp[-1])