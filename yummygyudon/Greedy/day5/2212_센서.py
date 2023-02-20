import sys
input = sys.stdin.readline
"""
적어도 하나의 집중국과는 통신이 가능
"""
N = int(input()) # 센서 갯수
K = int(input()) # 집중국 갯수
SENSORS = list(map(int, input().split()))
SENSORS.sort()

DISTANCE = [0] * (N-1)

"""
정렬했기에 따로 값 비교 혹은 abs 연산 필요 x
"""
for i in range(N-1) :
    DISTANCE[i] = SENSORS[i+1]-SENSORS[i]
DISTANCE.sort()

"""
6개 지점 : 6개의 거리 관계 -> 2개 기지국 -> 그룹 2 : 4개의 거리 관계 
10개 지점 : 10개의 거리 관계 -> 5개 기지국 -> 그룹 5 : 5개의 거리 관계

: N-K 개 만큼 관계가 줄어듦

거리 차이 큰 관계를 끊어내어 거리 차이 합을 최대한 줄여야함
-> 작은 거리 관계 순으로 합해서 최소 거리 차이 합을 구함
"""
print(sum(DISTANCE[:N-K]))
print(DISTANCE)