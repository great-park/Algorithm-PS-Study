from sys import stdin

input = stdin.readline
data = list(map(int, input().rstrip()))
len = len(data)

dp = [0] * (len + 1)
dp[0] = 1  # 1번 인덱스의 1자리수 경우 구할 때 필요
dp[1] = 1

if data[0] == 0:
    print(0)
else:
    for k in range(1, len):
        i = k + 1  # dp용 인덱스
        if data[k] > 0:  # 1자리 허용
            dp[i] += dp[i-1]
        if 10 <= data[k] + data[k-1]*10 <= 26:  # 2자리 허용, dp[i-1]이 0일 수도 있다.
            dp[i] += dp[i-2]
    print(dp[len] % 1000000)

""" 
    25114을 계산하는 과정
    - 2511에 4을 붙인다고 하자.
    1. 4가 1자리로 붙는 경우 
    -> 0이상인지 확인
    -> 2511의 경우의 수와 동일
    
    2/5/1/1/4
    25/1/1/4
    25/11/4
    2/5/11/4
    
    2. 4가 앞에 있는 1과 2자리로 붙는 경우 
    -> 2자리의 수가 26이하인지 확인
    -> 251의 경우의 수와 동일
    
    25/1/14
    2/5/1/14
"""
