import sys
input = sys.stdin.readline

N = int(input())
TIME_TABLE = [[0,0] for _ in range(N+1)]
for i in range(1,N+1) :
    # time_cost , income
    TIME_TABLE[i][0] , TIME_TABLE[i][1] = map(int, input().split())

print(TIME_TABLE)
"""
당일 하루짜리 상담이 가능하기 때문에 
N일차의 수입이 아닌 N일까지 상담한 후, 다음 날 수입을 봐야 한다.
-> *(N+1)이 아닌 *(N+2)
"""
INCOME = [0] * (N+2)

"""
당일을 포함해서 경과시간이 책정된 것을 잊지말자
"""

"""
N일에 일한 값 -> N+1 인덱스에 저장
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 3, 6, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 3, 6, 10, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 3, 6, 10, 15, 0, 0, 0, 0, 0]
[0, 0, 1, 3, 6, 10, 15, 21, 0, 0, 0, 0]
[0, 0, 1, 3, 6, 10, 15, 21, 28, 0, 0, 0]
[0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 0, 0]
[0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 0]
[0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
"""
# for i in range(1, N+1) : #
#     if i + TIME_TABLE[i][0] <= N+1 :
#         INCOME[i+TIME_TABLE[i][0]] = max(INCOME[i+TIME_TABLE[i][0]], INCOME[i]+TIME_TABLE[i][1])
#     print(INCOME)
MAX = -1e9
for i in range(1, N+1) :
    """
    만약 나중에 기한을 넘기지 않고 더 큰 수입이 있을 가능성 
    -> 당장 안하고 더 큰 수입있을 때까지 넘어갈 수 있기 때문에 MAX 값을 가지면서 비교해야함
    -> 모든(i+TIME_TABLE[i][0] <= M)을 통과하는 값들의 경우와 대조해보기
    """
    """
    해당 일자에 도달하기 전까지의 최댓값
    """
    MAX = max(MAX, INCOME[i])
    if i + TIME_TABLE[i][0] <= N+1:
        """
        이번 일자까지 "상담이 가능한 상태로 유지할 수 있는" 이전 과정 중의 최댓값으로 계산
        """
        INCOME[i + TIME_TABLE[i][0]] = max(INCOME[i + TIME_TABLE[i][0]], MAX + TIME_TABLE[i][1])

print(INCOME)

"""
마지막날에 항상 하루짜리 상담이 있을 것이란 보장도 없으면
이미 가장 큰 수입을 벌 수 있는 경우가 N일 전에 끝나는 상황도 가능하기 때문에
전체 값들 중에 가장 큰 값을 출력
"""
print(max(INCOME))

