import sys
input = sys.stdin.readline

N = int(input())
MOD = 9901
"""
[(우리를 모두 비웠을 때의 DP), (왼쪽을 택했을 때의 DP), (오른쪽을 택했을 때의 DP)]
"""
DP = [[0]*3 for _ in range(N+1)]
"""
2x1의 경우 - 초기값
"""
DP[1][0], DP[1][1], DP[1][2] = 1, 1, 1

"""
기준 칸에서 '하나도 선택하지 않는 경우'라면 이전 칸까지의 경우의 수밖에 안되므로 DP[i] = DP[i-1]
기준 칸에서 '왼쪽을 선택할 경우'라면 이전칸까지의 경우의 수 중 이전 칸의 '왼쪽을 택한 경우'는 포기해야함
기준 칸에서 '오른쪽을 선택할 경우'라면 이전칸까지의 경우의 수 중 이전 칸의 '왼쪽을 택한 경우'는 포기해야함
"""
# 왜 안될까 이해가 안되서 찾아보니까 값을 저장할때까지 % MOD를 해서 넣어야하더군요
# 저희가 쏘마 준비하는데는 중요한 요소가 아니니 이유는 깊게 안찾아봤습니닸!!
if N > 1 :
    for i in range(2,N+1) :
        for k in range(3) :
            """
            해단 번째에서 우리를 비울 때
            """
            if k == 0 :
                DP[i][k] = (DP[i - 1][0] + DP[i - 1][1] + DP[i-1][2]) % MOD
            """
            해당 번째에서 왼쪽에 사자를 넣을 때
            """
            if k == 1 :
                DP[i][k] = (DP[i - 1][0] + DP[i - 1][2]) % MOD
            """
            해당 번째에서 오른쪽에 사자를 넣을 때
            """
            if k == 2 :
                DP[i][k] = (DP[i - 1][0] + DP[i - 1][1]) % MOD
        print(DP)
        """
        [[0, 0, 0], [1, 1, 1], [3, 2, 2], [0, 0, 0], [0, 0, 0]]
        [[0, 0, 0], [1, 1, 1], [3, 2, 2], [7, 5, 5], [0, 0, 0]]
        [[0, 0, 0], [1, 1, 1], [3, 2, 2], [7, 5, 5], [17, 12, 12]]
        """

print(sum(DP[N]) % MOD)