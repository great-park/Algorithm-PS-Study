from sys import stdin
input = stdin.readline

NUM_QUANTITY, TARGET_POS = map(int, input().split())

NUM_RANGE = list(map(int,input().split()))
NUM_RANGE.sort()

CHECK = [False] * NUM_QUANTITY
NUMS = [0]*TARGET_POS

RESULTS = []
"""
값은 같더라도 
"""
def dfs(pos) :
    if pos == TARGET_POS :
        print(*NUMS)
        return
    remember_me = 0
    """
    각 순회마다 각 자리에 똑같은 값이 또 와서 순열을 만들지 않도록 만듦
    -> 앞 뒷자리는 같아도 상관없다. 같은 자리에 또 같은 숫자가 오게 되어 같은 순열만 만들지 않도록 만든다.
    """
    for i in range(NUM_QUANTITY) :
        if remember_me != NUM_RANGE[i] and not CHECK[i] :
            print("now NUM : ",NUM_RANGE[i])
            NUMS[pos] = NUM_RANGE[i]
            CHECK[i] = True
            print("before REMEMBER", remember_me)
            remember_me = NUM_RANGE[i]
            print("now REMEMBER",remember_me)
            dfs(pos+1)
            CHECK[i] = False
dfs(0)

for case in RESULTS :
    print(*case)
"""
set & join 활용 - 실패
"""
# NUM_RANGE.sort()
#
# CHECK = [False] * NUM_QUANTITY
# NUMS = [0]*TARGET_POS
#
# RESULTS = set()
# def dfs(pos) :
#     if pos == TARGET_POS :
#         perm = ' '.join(str(s) for s in NUMS)
#         RESULTS.add(perm)
#         return
#     for i in range(NUM_QUANTITY) :
#         if not CHECK[i] :
#             NUMS[pos] = NUM_RANGE[i]
#             CHECK[i] = True
#             dfs(pos+1)
#             CHECK[i] = False
# dfs(0)
# RESULTS = list(RESULTS)
# RESULTS.sort()
#
# for case in RESULTS :
#     print(case)

"""
in 연산자 & deepcopy 활용 - 시간 초과
"""
# NUM_RANGE.sort()
#
# CHECK = [False] * NUM_QUANTITY
# NUMS = [0]*TARGET_POS
#
# RESULTS = []
# from copy import deepcopy
# def dfs(pos) :
#     if pos == TARGET_POS :
#         if not NUMS in RESULTS :
#             RESULTS.append(deepcopy(NUMS))
#         return
#     for i in range(NUM_QUANTITY) :
#         if not CHECK[i] :
#             NUMS[pos] = NUM_RANGE[i]
#             CHECK[i] = True
#             dfs(pos+1)
#             CHECK[i] = False
# dfs(0)
#
# for case in RESULTS :
#     print(*case)

