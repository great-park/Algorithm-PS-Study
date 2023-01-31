### My Part ###
import sys
input = sys.stdin.readline
# d = [[1,1],[-1,-1],[-1,1],[-1,-1]] # 각 대각선
TC = int(input())

for _ in range(TC):
    N = int(input())
    SCORE = [[0]*N]*2
    STICKER = []
    for _ in range(2):
        STICKER.append(list(map(int, input().split())))
    # print(STICKER)
    if N > 1 :
        """
        2번째까지는 절대적으로 대각선 값만 누적시킬 수 있기 때문에 전처리
        """
        STICKER[0][1] += STICKER[1][0]
        STICKER[1][1] += STICKER[0][0]
        for i in range(2, N) :
            """
            한 칸 건너뛴 전 단계의 점수는 같은 층에 있더라도 변이 안닿기 때문에 더할 수 있음
            temp = 변이 절대 닿지 않는 한 칸 건너뛴 전 단계에서의 1층 2층 점수 중 최대점수값 저장
            
            경우의 수
            1. 내 대각선 전 칸까지의 최대 점수와 내 점수 더하기
            2. 대각선을 포기하고 한칸 건너뛴 단계에서의 최대 점수가 나오는 경우의 수 값을 내 점수와 더하기
            """
            temp = max(STICKER[0][i-2], STICKER[1][i-2])
            STICKER[0][i] = max(STICKER[0][i]+temp, STICKER[0][i]+STICKER[1][i-1])
            STICKER[1][i] = max(STICKER[1][i] + temp, STICKER[1][i] + STICKER[0][i-1])
    """
    마지막 단계의 1층 2층값 중 가장 큰 점수를 얻는 경우의 수의 값을 출력
    """
    print(max(STICKER[0][N-1], STICKER[1][N-1]), end="\n")
