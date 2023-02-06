# 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다
from sys import stdin
N = int(stdin.readline())
"""
N = 1 -> 1 + 2 = 3
N = 2 -> 1 + 4 + 2 = 7   
=> 2x(N-1) 에서 2x1을 추가할 때 새로운 사자를 (1) 놓는다. (2) 놓지 않는다.
(1) = 3, (2) = 2 + 2

N = 3 -> 1 + 6 + 8 + 2 = 17
(1) = 7, (2) = 5 + 5
여기서 5 = (dp[i-1] - dp[i-2])/2 

따라서 점화식 : dp[i] = dp[i-1] + 2*{dp[i-2] + (dp[i-1]-dp[i-2])/2} = 2dp[i-1] + dp[i-2]
그림 풀이는 블로그에
"""
if N == 1:
    print(3)
else:
    dp = [1 for _ in range(N+1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, N+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
    print(dp[N])
