import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC) :
    N = int(input())
    SCORES = []
    for _ in range(N) :
        SCORES.append(list(map(int, input().split())))

    """
    바보 같았네요..
    점수가 아니라 등수였어...
    """
    """ 시도 1 """
    # SCORES.sort(key=lambda x: (x[0],x[1]), reverse=True)
    # print(SCORES)
    # result =
    # cv, interview = SCORES[0][0], SCORES[0][1]
    # for i in range(1,N) :
    #     result += 1
    #     if cv > SCORES[i][0] and interview > SCORES[i][1] :
    #         result -= 1
    #     cv, interview = SCORES[i][0], SCORES[i][1]
    """ 시도 2 """
    """
    서류 점수로 오름차순 정렬
    -> 배치 : 서류점수가 높은 순서대로
    앞에서부터 뒤로 갈 때마다 '서류 점수에서 한 단계 높은 사람'보단 '면접 점수에서 높은 등수'가 나와야 합격
    
    """
    # SCORES.sort(key=lambda x: x[1])
    SCORES.sort(key=lambda x: x[0])

    print(SCORES)
    # result = N

    # interview =

    """
    일단 서류 성적 1등은 무조건 합격 : 1로 시작
    """
    result = 1
    value =SCORES[0]
    for i in range(1,N) :
        """
        면접 점수가 더 높으면
        """
        if SCORES[i][1] <  value[1] :
            """
            고용 확정 : += 1
            """
            result += 1
            """
            다음 서류점수 순위와의 비교를 위해 갱신
            """
            value = SCORES[i]
    print(result)

