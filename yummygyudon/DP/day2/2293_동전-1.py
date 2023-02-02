import sys
input = sys.stdin.readline
"""
N 가지 종류의 동전 : 각 동전의 가치는 다름
-> 합이 K원인 동전 구성의 경우의 수를 
"""
N, TARGET = map(int,input().split())
COINS = []
for _ in range(N) :
    COINS.append(int(input()))

"""
작은 코인부터 해야
idx-coin의 차액의 경우의 수를 누적해서 더해줄 수 있음.
-> sort
"""
COINS.sort()

DP = [0]*(TARGET+1)

"""
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 1원일 때
[0, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
[0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 10]
"""
for coin in COINS :
    for idx in range(1,TARGET+1) :
        """
        
        """
        if idx - coin > 0 : #
            DP[idx] = DP[idx] + DP[idx-coin]
        elif idx - coin == 0 :
            """
            coin 자기 자신의 값일 경우, 경우의 수 하나씩을 더해줘야 함
            """
            DP[idx] += 1
        print(DP)
print(DP[TARGET])


"""
이전 풀이
"""
N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

dp = [0]*(K+1)
dp[0]=1
for c in coin :
    for i in range(1,K+1) :
        if i-c >= 0 :
            dp[i] += dp[i-c]
print(dp[K])