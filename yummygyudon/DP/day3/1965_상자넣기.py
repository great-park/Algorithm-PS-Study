### My Part ###
import sys
input = sys.stdin.readline
N = int(input())
"""
순서대로 담아가야하는 것이 규칙 -> sort금지
"""
BOX = list(map(int, input().split()))

DP = [0] * N
"""
맨 처음 박스 = 1 로처리
(안해주면 처음부터 박스가 없는 상태로 시작하는 것 -> 말이 안되는 상황)
"""
DP[0] = 1
"""
2번째 박스부터 쭉 브루트포스처럼 모든 순서의 박스를 시작으로 DP 시작
( 박스가 총 1개이면 range(1,1)로 for문을 안돌고 끝냄 )
"""
for i in range(1,N) : # 1,2,3,4,5,6,7,8
    """
    기본 값 : 자기자신 : 1
    """
    MAX_POSSIBLE = 1
    """
    현재 기준박스까지의 수열로의 경우의 수 확인하기
    """
    for k in range(i) :
        """
        앞에 있는 박스들을 쭉 돌면서 더 작은 박스일 경우,
        앞에 있는 박스이면서 
        해당 박스안에 담겨있는 최대 박스의 수를 MAX_POSSIBLE에 저장
        """
        if BOX[i] > BOX[k] :
            possible = DP[k]+1
            MAX_POSSIBLE = max(MAX_POSSIBLE, possible)

    DP[i] = MAX_POSSIBLE
    """
    [1, 2, 0, 0, 0, 0, 0, 0]
    [1, 2, 2, 0, 0, 0, 0, 0]
    [1, 2, 2, 3, 0, 0, 0, 0]
    [1, 2, 2, 3, 4, 0, 0, 0]
    [1, 2, 2, 3, 4, 3, 0, 0]
    [1, 2, 2, 3, 4, 3, 4, 0]
    [1, 2, 2, 3, 4, 3, 4, 5]
    """
"""
앞선 순서에서 더 많이 담을 수 있는 경우가 있을 수 있기 때문에
max로 추출
(가장 마지막 박스가 가장 큰 박스라는 보장이 없음)
"""
print(max(DP))