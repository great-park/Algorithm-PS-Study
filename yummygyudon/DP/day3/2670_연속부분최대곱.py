import sys
input = sys.stdin.readline

N = int(input())
FLOATS = []
for _ in range(N) :
    FLOATS.append(float(input()))

"""
1번째 방식-DP 갱신 : 시간 초과
"""
DP = [0.0] * N

# for i in range(N) : # 0
#     tmp = FLOATS[i]
#     for k in range(i+1,N) : # 1,2,3,4,5,6,7
#         tmp *= FLOATS[k]
#         DP[i] = max(tmp, DP[i])
#     print(DP)
# print("%.3f"%max(DP))
#
# for i in range(N-1,-1,-1) : # 7
#     tmp = FLOATS[i]
#     for k in range(1, i) : # 1,2,3,4,5,68
#         tmp *= FLOATS[-k]
#         DP[i] = max(tmp, DP[i])
#     print(DP)

"""
2번째 방식-MAX변수 갱신 : 시간 초과
"""
# MAX = 0.0
# for i in range(N) : # 0
#     tmp = FLOATS[i]
#     for k in range(i+1,N) : # 1,2,3,4,5,6,7
#         tmp *= FLOATS[k]
#         MAX = max(tmp, MAX)
#     print(MAX)
# print("%.3f"%MAX)


"""
** DP 말고 FLOATS 자체에서 해보자
1번째 방식 적용 : 시간 초과가 났습니다.
"""
# for i in range(N) : # 0
#     tmp = FLOATS[i]
#     for k in range(i+1,N) : # 1,2,3,4,5,6,7
#         tmp *= FLOATS[k]
#         FLOATS[i] = max(tmp, FLOATS[i])
#     print(FLOATS)
# print("%.3f"%max(FLOATS))

"""
3번째 방식 : ...? 횡재
2중 for문에서 시간초과가 뜬 거 같습니다.
"""
for i in range(1, N) : # 0
    FLOATS[i] = max(FLOATS[i], FLOATS[i]*FLOATS[i-1])
    print(FLOATS)
print("%.3f"%max(FLOATS))
