import sys
input = sys.stdin.readline

K = int(input())
N = int(input())

# UNABLE = "x"*(K-1)

START_SEQ = [chr(i) for i in range(65, 65 + K)]
END_SEQ = list(input().rstrip())
LADDER = []
RANDOM_LAYER = 0
for i in range(N) :
    layer = list(input().rstrip())
    if layer[0] == '?' :
        RANDOM_LAYER = i
    LADDER.append(layer)


# print(START_SEQ)
# print(LADDER)
# print(RANDOM_LAYER)
# print(BEFORE_RANDOM)

"""
"-" 문자열 idx가 더 작으면 : 왼쪽으로 이동
"-" 문자열 idx가 더 크면 : 오른쪽으로 이동
"""

"""
RANDOM_LAYER 직전까지만
"""
for i in range(RANDOM_LAYER) :
    for k in range(K-1) :
        if LADDER[i][k] == "-" :
            START_SEQ[k], START_SEQ[k+1] = START_SEQ[k+1], START_SEQ[k]

print(START_SEQ)

"""
RANDOM_LAYER 직후까지만
"""
for i in range(N-1, RANDOM_LAYER, -1) :
    for k in range(K-1) :
        if LADDER[i][k] == "-" :
            END_SEQ[k], END_SEQ[k+1] = END_SEQ[k+1], END_SEQ[k]

print(END_SEQ)

RANDOM_LADDER = ["*"] * (K-1)

for i in range(K-1):
    if START_SEQ[i] == END_SEQ[i+1] and START_SEQ[i+1] == END_SEQ[i] :
        RANDOM_LADDER[i] = "-"
        START_SEQ[i], START_SEQ[i+1] = START_SEQ[i+1], START_SEQ[i]

print()
print(START_SEQ)
print(END_SEQ)

"""
['C', 'A', 'D', 'B', 'E', 'G', 'F', 'H', 'I', 'J']
['C', 'A', 'B', 'D', 'G', 'E', 'F', 'H', 'J', 'I']

['C', 'A', 'B', 'D', 'G', 'E', 'F', 'H', 'J', 'I']
['C', 'A', 'B', 'D', 'G', 'E', 'F', 'H', 'J', 'I']
['*', '*', '-', '*', '-', '*', '*', '*', '-']
"""

"""
....?? 왜 여기서 전역변수 안쓰고 RANDOM_LADDER를 갱신하니까 해결이 되버리네요
"""
if START_SEQ != END_SEQ :
    RANDOM_LADDER = ["x"]*(K-1)
print(''.join(RANDOM_LADDER))


"""
밑에 있는 코드들도 다 되는 코드였습니다..ㅋㅋㅋㅋ

풀 문제를 잘골라야 시간 낭비가 없을 것 같습니다

풀이 수 많은 순 > 정답률이 어느정도 보장되어 있는 문제 순 : 이렇게 잘 뽑아보죠
"""
# RANDOM_LADDER = ['']*(K-1)
# # RANDOM_LADDER = []
# # checkIdx = 0
# # while True :
# #     if START_SEQ[checkIdx] == END_SEQ[checkIdx] :
# #         RANDOM_LADDER.append('*')
# #         checkIdx += 1
# #     elif START_SEQ[checkIdx] == END_SEQ[checkIdx+1] :
# #         RANDOM_LADDER.append('-')
# #         RANDOM_LADDER.append('*')
# #         checkIdx += 2
# #     if len(RANDOM_LADDER) >= K-1 :
# #         break
#
# # CROSS_BEFORE = False
# # for i in range(K-1) :
# #     if START_SEQ[i] == END_SEQ[i] :
# #         RANDOM_LADDER.append('*')
# #         continue
# #     else :
# #         if START_SEQ[i] == END_SEQ[i + 1] :
# #             if END_SEQ[i] == START_SEQ[i + 1] :
# #                 RANDOM_LADDER.append('-')
# #                 CROSS_BEFORE = True
# #                 continue
# #         else :
# #             if CROSS_BEFORE and START_SEQ[i] == END_SEQ[i - 1] :
# #                 RANDOM_LADDER.append('*')
# #                 CROSS_BEFORE = False
# #                 continue
# SAME_BEFORE = False
# CROSS_BEFORE = False
# for i in range(1, K) :
#     if START_SEQ[i] == END_SEQ[i] and START_SEQ[i-1] == END_SEQ[i-1]:
#         RANDOM_LADDER[i - 1] = "*"
#         continue
#     if START_SEQ[i] != END_SEQ[i] and START_SEQ[i-1] == END_SEQ[i-1]  : #and START_SEQ[i] != END_SEQ[i-1] and START_SEQ[i-1] == END_SEQ[i]
#         RANDOM_LADDER[i - 1] = "*"
#         continue
#     if START_SEQ[i] != END_SEQ[i] and START_SEQ[i-1] != END_SEQ[i-1] and START_SEQ[i] == END_SEQ[i-1] and START_SEQ[i-1] == END_SEQ[i] :
#         RANDOM_LADDER[i-1] = "-"
#         CROSS_BEFORE = True
#         continue
#     if START_SEQ[i] != END_SEQ[i] and START_SEQ[i - 1] != END_SEQ[i - 1] and START_SEQ[i] != END_SEQ[i - 1] and START_SEQ[i-1] != END_SEQ[i] and CROSS_BEFORE:
#         RANDOM_LADDER[i - 1] = "*"
#         CROSS_BEFORE = False
#         continue
#     if START_SEQ[i] != END_SEQ[i] and START_SEQ[i - 1] == END_SEQ[i - 1] and START_SEQ[i] != END_SEQ[i - 1] and START_SEQ[i-1] != END_SEQ[i] and CROSS_BEFORE:
#         RANDOM_LADDER[i - 1] = "*"
#         CROSS_BEFORE = False
#         continue
#     if START_SEQ[i] == END_SEQ[i] and START_SEQ[i - 1] != END_SEQ[i - 1] and CROSS_BEFORE:
#         RANDOM_LADDER[i - 1] = "*"
#         CROSS_BEFORE = False
#         continue
#
#     # if START_SEQ[i] == END_SEQ[i] :
#     #     RANDOM_LADDER[i-1] = "*"
#     #     SAME_BEFORE = True
#     #     # RANDOM_LADDER.append('*')
#     #     continue
#     # else :
#     #     if START_SEQ[i] == END_SEQ[i - 1] and START_SEQ[i-1] == END_SEQ[i - 1]:
#     #         RANDOM_LADDER[i - 1] = "-"
#     #         CROSS_BEFORE = True
#     #         SAME_BEFORE = False
#     #         continue
#     #     if START_SEQ[i] != END_SEQ[i - 1] and SAME_BEFORE:
#     #         RANDOM_LADDER[i - 1] = "*"
#     #         SAME_BEFORE = False
#     #         continue
#     #     if START_SEQ[i] != END_SEQ[i - 1] and CROSS_BEFORE:
#     #         RANDOM_LADDER[i - 1] = "*"
#     #         CROSS_BEFORE = False
#
#
#
#     # if START_SEQ[i] == END_SEQ[i] and START_SEQ[i+1] == END_SEQ[i+1] :
#     #     # RANDOM_LADDER.append('*')
#     #     RANDOM_LADDER[i] = '*'
#     # elif START_SEQ[i] == END_SEQ[i + 1] and START_SEQ[i + 1] == END_SEQ[i] and not CROSS_BEFORE :
#     #     """
#     #     대각 선에 있는 값들이 서로 같을 때
#     #     """
#     #     # RANDOM_LADDER.append('-')
#     #     RANDOM_LADDER[i] = '-'
#     #     CROSS_BEFORE = True
#     # elif not (START_SEQ[i] == END_SEQ[i] and START_SEQ[i+1] == END_SEQ[i+1]) and CROSS_BEFORE :
#     #     # RANDOM_LADDER.append('*')
#     #     RANDOM_LADDER[i] = '*'
#     #     CROSS_BEFORE = False
#     # elif START_SEQ[i] == END_SEQ[i] and START_SEQ[i+1] != END_SEQ[i+1] :
#     #     """
#     #     만약 바로 밑은 같은데  옆에는 바로 밑과 같지 않을 경우
#     #     """
#     #     RANDOM_LADDER.append('*')
#     #
#     # elif START_SEQ[i] != END_SEQ[i+1] and START_SEQ[i+1] != END_SEQ[i] :
#     #     RANDOM_LADDER.append('*')
#
#
#
# # print(RANDOM_LADDER)
# if '' in RANDOM_LADDER :
#     print(UNABLE)
# else :
#     print(''.join(RANDOM_LADDER))
#
# # if len(RANDOM_LADDER) == K-1 :
# #     print(''.join(RANDOM_LADDER))
# # else :
# #     print(UNABLE)
