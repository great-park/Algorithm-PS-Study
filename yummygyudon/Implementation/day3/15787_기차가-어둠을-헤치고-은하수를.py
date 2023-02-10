import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

"""
각 기차마다 Deque 만들기
"""
TRAIN = [deque([0]*20) for _ in range(N+1)]

"""
1 (기차 번째) (좌석 위치) -> 사람 태우기 (이미 사람 있으면 아무것도 안하기)
2 (기차 번째) (좌석 위치) -> 사람 태우기 (이미 사람 있으면 아무것도 안하기
3 (기차 번째) -> 해당 순서의 기차 승객 모두 한 칸씩 뒤로 (20번째에 사람 있으면 하차)
4 (기차 번째) -> 해당 순서의 기차 승객 모두 한 칸씩 앞으로 (1번째에 사람 있으면 하차)
"""


for _ in range(M):
    command=list(map(int,input().split()))
    if command[0]==1:
        TRAIN[command[1]][command[2]-1]=1
    elif command[0]==2:
        TRAIN[command[1]][command[2]-1]=0

    elif command[0]==3:
        """
        오른쪽으로 한 칸씩 밀기
        """
        TRAIN[command[1]].rotate(1)
        """
        밀려서 맨 앞으로 온 값-> 빈자리로 갱신
        """
        TRAIN[command[1]][0]=0
    else:
        """
        왼쪽으로 한 칸씩 밀기
        """
        TRAIN[command[1]].rotate(-1)
        """
        당겨져서 맨 뒤로 온 값-> 빈자리로 갱신
        """
        TRAIN[command[1]][19]=0


alreadyPass=[]
"""
1호차 부터
[deque([0]*20) for _ in range(N+1)] 했기 때문에
"""
for eachTrain in TRAIN[1:]:
    """
    동일한 상태의 기차가 없을 경우에만 통과
    """
    if i not in alreadyPass:
        alreadyPass.append(eachTrain)
print(len(alreadyPass))