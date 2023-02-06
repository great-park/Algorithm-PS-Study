### My Part ###
import sys
input = sys.stdin.readline
N = int(input())
""" 20년 + 4년(Index 최대치)꺼지 보장된 DP"""
LIVE = [0] * 21
DEAD = [0] * 25

"""
for문을 2년차부터 세기 때문에
1년차에 대한 LIVE와 DEAD 값 설정
"""
LIVE[1] = 1
DEAD[4] = 1
for i in range(2, N+1) :
    """
    1월에 분열한 상황
    """
    born = LIVE[i-1]
    LIVE[i] = born*2 - DEAD[i]

    """
    2월에 사망할 상황
    """
    if i % 2 == 1:
        """
        홀수 해에 태어남 -> 3년 이후 사망할 개체 수 누적합
        """
        print("%d년차 홀수"%i)
        DEAD[i+3] += born

    else :
        """
        짝수 해에 태어남 -> 4년 이후 사망할 개체 수 누적합
        """
        print("%d년차 짝수" % i)
        DEAD[i+4] += born

    print(DEAD)
    print(LIVE)
print(LIVE[N])