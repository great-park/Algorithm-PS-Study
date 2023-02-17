### My Part ###
import sys
input = sys.stdin.readline

"""
1. 주식 += 1
2. 원하는 만큼 주식 매도 
3. Nothing
"""

"""
3    5    9
 (+2) (+4)
3일 때 산 것 : 9에서 팔면 +6
5일 때 산 것 : 9에서 팔면 +4    

1    1    3    1    2
 (+0) (+2) (-2) (+1)
0    0    4
            
1일 때 산 것 : 2개 * 3에서 팔면 2*2 = +4
1일 때 산 것 : 1개 * 2에서 팔면 1*1 = + 1
"""
TC = int(input())
for _ in range(TC) :
    DAY = int(input())-1
    CHART = list(map(int, input().split()))
    benefit = 0
    MAX = 0
    holding = []
    """
    시도 1
    """
    # d = 0
    # DAY = int(input())-1
    # CHART = list(map(int, input().split()))
    # while d < DAY :
    #
    #     if CHART[d] <= CHART[d+1] :
    #         holding.append(CHART[d])
    #     else :
    #         for _ in range(len(holding)) :
    #             benefit += CHART[d] - holding.pop()
    #     print(holding)
    #     d += 1
    # print(holding)
    # if holding :
    #     for i in range(len(holding)):
    #         benefit += CHART[DAY] - holding.pop()
    # print(benefit)
    """시도 2"""
    # DAY = int(input())
    # CHART = list(map(int, input().split())) + [0]
    # MAX = 0
    # for day in range(DAY+1) :
    #     # print("Today = ", CHART[day])
    #     if CHART[day] >= MAX :
    #         holding.append(CHART[day])
    #         MAX = CHART[day]
    #     else :
    #         for i in range(len(holding)):
    #             benefit += (MAX - holding.pop())
    #         holding.append(CHART[day])
    #         MAX = CHART[day]
    # print(benefit)
    """
    역순
    """
    for day in range(DAY, -1, -1) :
        print("현재 최고액 : ", MAX)
        if CHART[day] > MAX :
            MAX = CHART[day]
        else :
            print("매도 후 이익 = %d : %d - %d(%d일 주식가)"%(MAX - CHART[day], MAX, CHART[day], day+1))
            benefit += MAX - CHART[day]
    print(benefit)
    print()

"""
앞에서부터 순회했을 때의 반례
<< 반례 >>
1
4
1 2 1 100
    
# Output
100
    
# Answer
296

-> 만약 마지막에 개떡상하면 중간에 오르락 내리락해서
손해를 보더라도 기다렸다가
개떡상 가격에 매도하는게 이득(갖고 있는 주식 수가 많은게 유리)
"""

