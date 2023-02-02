"""
N개의 돌 -> 일렬로 나열
돌틈 사이에 산삼

돌과 돌 사이를 점프하면서 이동
점프 1 : 다음 돌 점프 [작은 점프]
점프 2 : 1개의 돌 건너뛰는 점프 [큰 점프]
점프 3 : 2개의 돌을 건너뛰는 점프 -> 단 한번의 기회 : 돌 상관없이 k 만큼 에너지 소비

돌마다 소비하는 에너지가 다름
"""
import sys
input = sys.stdin.readline
N = int(input())
ROCKS = [[0,0] for _ in range(N)] # [[0,0][0,0][0,0][0,0][0,0]]
for i in range(1, N): # 1,2,3,4
    ROCKS[i][0], ROCKS[i][1] = map(int, input().split())
K = int(input())

NO_HUGE_JUMP = [1e9] * (N+1)
"""
돌 소요 체력 표
[[0,0]  처음 시작 
 [1,2]  1번돌에서 뛸 때
 [2,3]  2번돌에서 뛸 때
 [4,5]  3번돌에서 뛸 때
 [6,7]] 4번돌에서 뛸 때

NO_HUGE_JUMP : 매우 큰 점프 없이 끝 해당 돌까지 도착했을 때의 최소 체력 경우의 수
[[0] 무시
 [0] 1번돌 도착 상태
 [0] 2번돌 도착 상태
 [0] 3번돌 도착 상태
 [0] 4번돌 도착 상태
 [0]]5번돌 도착 상태
"""
"""그저 평지일 때"""
NO_HUGE_JUMP[1] = ROCKS[0][0]

"""N이 1로 입력됐을 경우 0 출력되게끔"""
minimalJump = 0


if N >= 2 :
    NO_HUGE_JUMP[2] = ROCKS[1][0]
    """
    매우 큰 점프 없이 이동했을 경우 먼저 계산
    """
    print(NO_HUGE_JUMP)
    for nowPos in range(3, N+1): # 3,4,5
        """
        (1칸 전의 상태 + 현재 위치 돌의 1칸 점프 시의 소요 체력) vs (2칸 전의 상태 + 현재 위치 돌의 2칸 점프 시의 소요 체력)
        [1000000000.0, 0, 1, 1000000000.0, 1000000000.0, 1000000000.0]
        [1000000000.0, 0, 1, 2, 1000000000.0, 1000000000.0]
        [1000000000.0, 0, 1, 2, 4, 1000000000.0]
        [1000000000.0, 0, 1, 2, 4, 7]   
        """
        NO_HUGE_JUMP[nowPos] = min(NO_HUGE_JUMP[nowPos-1] + ROCKS[nowPos-1][0], NO_HUGE_JUMP[nowPos-2] + ROCKS[nowPos-2][1])
        print(NO_HUGE_JUMP)

    """
    << 시도 1 >> : 실패
    만약 돌이 4개 이상 -> 매우 큰 점프 가능
    [1000000000.0, 0, 1, 2, 4, 7]
    [1000000000.0, 0, 1, 2, 4, 5]
    """
    # if N >= 4 :
    #     print("만약 돌이 4개 이상 -> 매우 큰 점프 가능")
    #     for nowPos in range(4, N+1) :
    #         NO_HUGE_JUMP[nowPos] = min(NO_HUGE_JUMP[nowPos-3] + K, NO_HUGE_JUMP[nowPos])
    #         print(NO_HUGE_JUMP)

    """
    << 시도 2 >> 4번째 돌부터 모든 매우 큰 점프 시나리오에 대해 DP 돌기
    """
    minimalJump = NO_HUGE_JUMP[-1]
    for i in range(4,N+1) : # 4, 5
        """
        3칸 이동할 수 있는 상황부터 모든 경우 다돌기
        단 한번만 뛸 수 있기 때문에 4 -> 1번째 돌 시작 -> 반복 & 5 -> 2번째 돌 시작 -> 반복
        """
        scenario, case1, case2 = NO_HUGE_JUMP[i-3] + K, 1e9, 1e9 # 0, 1e9, 1e9
        """
        [1000000000.0, 0, 1, 2, 4, 7]  
        
        점프할 수 있는 돌까지만 계산 -> (i, N)
        아래 조건문으로 더 뛸 수 있는지 확인해서 시나리오 진행
        """
        for k in range(i, N) : # 4
            """
            한 칸 이동 케이
            case 1 = min (1e9, 0 + 4) 1-> 4 + ROCKS[k][0] -> 5
            case 1 = min ( case2 (6번쨰 돌 기본 DP값),  5번째 돌에서 1칸이동했을
            """
            if i+1 <= N :
                case1 = min(case1, scenario+ROCKS[k][0])
            """
            두 칸 이동 케이스
             1 -> 4 + 2
            """
            if i+2 <= N :
                case2 = min(case2, scenario+ROCKS[k][1])
            """
            다음 돌 시나리오로 인계
            sc = case1 = 6 -> 5번째 돌에 도착했을 때의 상태
            case1 = case2 = 7 -> 6번째 돌에 도착했을 때의 상태
            """
            scenario, case1, case2 = case1, case2, 1e9
        """
        "매우 큰 점프 안했을 때의 최소값" 과 "매우 큰 점프 시나리오 적용 후의 최소값" 비교
        """
        minimalJump = min(minimalJump, scenario)

print(minimalJump)