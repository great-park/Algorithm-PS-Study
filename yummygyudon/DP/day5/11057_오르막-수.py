import sys
input = sys.stdin.readline

N = int(input())
"""
2째자리부턴 0이 가능 -> 0,1,2,...,9 까지 총 10가지 경우의 수 필요
"""
DP =[[0]*10 for _ in range(N+1)]
MOD = 10007
"""
한자릿수 1 ~ 9는 자체적으로 오르막수
-> 첫째 자릿수가 1이 될 수 있도록 임의의 0째자릿수에 모두 1로 설정 

자릿수 돌기
1째 자리부터
"""
for i in range(10) :
    DP[0][i] = 1

"""
i = 자릿수
k = 

ex. 1
DP[1][0] = DP[0][0] -> 1 (0까지의 오르막수 경우의 수)
DP[1][1] = DP[0][0] + DP[0][1] -> 2 (1까지의 오르막수 경우의 수)
DP[1][2] = DP[0][0] + DP[0][1] + DP[0][2] -> 3 (2까지의 오르막수 경우의 수)
.
.
DP[1][9] = DP[0][0] + .... + DP[0][9] -> 10 (9까지의 오르막수 경우의 수)
"""
for i in range(1, N+1):
    for k in range(10): # 0~9까지만
        """
        기준 숫자보다 같거나 작은 숫자들에 대해서만 -> k+1만큼 idx 반복
        0-1 -> -1 -> 이전 자릿수의 9의 DP 값이 오는데 
        원래 9보다 큰 오르막가 없기 때문에
        """
        for p in range(k+1): # 0~9까지의
            DP[i][k] += DP[i-1][p]
"""
자릿수의 __9까지의 경우의 수 확인하면 됨
"""
print(DP[N][9]%MOD)

"""
ex. 2
DP[1][0] = DP[0][0] -> 1 (0까지의 오르막수 경우의 수)
DP[1][1] = DP[0][0] + DP[0][1] -> 2 (1까지의 오르막수 경우의 수)
DP[1][2] = DP[0][0] + DP[0][1] + DP[0][2] -> 3 (2까지의 오르막수 경우의 수)
.
.
DP[1][9] = DP[0][0] + .... + DP[0][9] -> 10 (9까지의 오르막수 경우의 수)

DP[2][0] = DP[1][0] -> 1
DP[2][1] = DP[1][0] + DP[1][1] -> 3 ( 00, 01, 11  -> 0, 1, 11 의 경우)
DP[2][2] = DP[1][0] + DP[1][1] + DP[1][2] -> 6 ( 00, 01, 02, 11, 12, 22  -> 0, 1, 2, 11, 12, 22)
.
.
DP[2][9] = DP[1][0] + .... + DP[1][9] -> 55 (99까지의 오르막수 경우의 수 -> 0,1,2,...,9,10,11,12,...69,,77,78,79,88,89,99
                                                                      10+9+8+...+3+2+1)
=> [[1,1,...,1], [1,2,..., 10]
    | 0째 자리  |  | 1째 자리    |
    
역으로 생각하면
이전 자리가 9면 다음 자리에는 9만 가능하기 때문에 1
이전 자리가 8이면 다음 자리에는 8,9 가능하기 때문에 2
...
이전 자리가 1이면 다음 자리에는 1~9가 가능하기 때문에 9

-> 올 수 있는 이전 자리까지의 경우의 수들을 누적하며 더해가면 됨.
"""