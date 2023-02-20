### My Part ###
import sys
input = sys.stdin.readline

N = int(input())

NUMS = []
USED = [False]*(N)
for _ in range(N) :
    NUMS.append(int(input()))
"""
1개의 값만 있으면 그냥 출력하고 끝내기
"""
if N == 1 :
    print(NUMS[0])
    sys.exit()
"""
음수 & 0부터 처리하기
"""
NUMS.sort()
result = 0

idx = 0
while True :
    if idx >= N :
        break
    if USED[idx] :
        idx+=1
        continue
    if NUMS[idx] < 0 :
        for i in range(idx+1, N):
            """
            (-) * (-) = (+) 인 부분도 고려해야 함.

            사용 안된 음수 혹은 0에 대해서 만나면 
            """
            if NUMS[i] <= 0 and not USED[i] :
                result += (NUMS[idx]*NUMS[i])
                USED[idx], USED[i] = True, True
                break
            else:
                result += NUMS[idx]
                USED[idx] = True
                break
        idx += 1
        """
        음수와 매칭되지도 않았다면 그냥 더하기
        """
    elif NUMS[idx] == 0 :
        result += NUMS[idx]
        USED[idx] = True
        idx += 1
    else :
        if (N-idx) % 2 == 1 :
            result += NUMS[idx]
            USED[idx] = True
            idx += 1
        else :
            result += max(NUMS[idx]*NUMS[idx+1], NUMS[idx]+NUMS[idx+1])
            USED[idx], USED[idx+1] = True, True
            idx += 2
print(result)




# NUMS.sort(reverse=True)
# for i in range(N) :
#     MAX, MIN = -1e9, 1e9
#     for k in range(i,N):
#         if (NUMS[i]*NUMS[k]) > M



"""시도 3"""
# for i in range(N) :
#     if USED[i] :
#         continue
#     USED[i] = True
#     if NUMS[i] < 0 :
#         for k in range(i,N) :
#             if NUMS[k] == 0 and not USED[k]:
#                 result += (NUMS[i]* NUMS[k])
#                 USED[k] = True
#                 break
#             if NUMS[k] > 0 :
#                 result += NUMS[i]
#                 break
#     elif NUMS[i] == 0 :
#         result += NUMS[i]
#     else :
#         if i+1 == N :
#             result += NUMS[i]
#         else :


