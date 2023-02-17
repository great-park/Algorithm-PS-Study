import sys
input = sys.stdin.readline

N = int(input())
HOUSE = list(map(int, input().split()))

"""
집마다 설치했을 때의 서로 다른 효율성 없기 때문에
거리만 생각하면 됨
-> 시작점 ~ 끝점 구간의 중심에 있는 집에 설치하는 것이 가장 효율적
"""
""" 시작점 ~ 끝점 구간 만들기 """
HOUSE.sort()
""" 가운데에 있는 집에 설치 """
print(HOUSE[(N - 1) // 2])