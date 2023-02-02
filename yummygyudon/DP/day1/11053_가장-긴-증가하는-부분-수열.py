import sys
input = sys.stdin.readline
N = int(input())
NUMS = list(map(int, input().split()))
# CHECK = [0] * 1_001
CHECK = [0] * N
for idx in range(N) :
    """
    이전 값들 확인
    뒤에 있는 값들
    - 기준 값보다 작은 값 & 해당 작은 값이 가지는 수열이 가장 길다면 
    """
    for before in range(idx) :
        if NUMS[idx] > NUMS[before] and CHECK[idx] < CHECK[before] :
            CHECK[idx] = CHECK[before]
    CHECK[idx] += 1
    print(CHECK)

# print(CHECK)
print(max(CHECK))
"""
[1,2,1,3,2,5]
idx=0 : [+1, 0, 0, 0, 0, 0]
idx=1 : [1, 1+1, 0, 0, 0, 0]
idx=2 : [1, 2, +1, 0, 0, 0]
idx=3 : [1, 2, 1, 2+1, 0, 0] ->CHECK[3] 값은  CHECK[1] 값으로 갱신되어서 그 뒤에 작은 수가 있더라도 CHECK[3]값이 더 작으므로 갱신 안함
idx=4 : [1, 2, 1, 3, 1+1, 0]
idx=5 : [1, 2, 1, 3, 2, 3+1]
-> 최종 [1, 2, 1, 3, 2, 4]
"""