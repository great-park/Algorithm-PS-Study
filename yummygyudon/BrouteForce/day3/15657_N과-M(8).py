from sys import stdin
input = stdin.readline

NUM_QUANTITY, TARGET_POS = map(int, input().split())

NUM_RANGE = list(map(int, input().split()))
NUM_RANGE.sort()
CHECK = [[False] * TARGET_POS for _ in range(NUM_QUANTITY)]
# CHECK = [False]*NUM_QUANTITY
NUMS = [0] * TARGET_POS

def dfs(depth,num, pos) :
    if pos == TARGET_POS :
        print(*NUMS)
        return
    for i in range(NUM_QUANTITY) :
        if num <= NUM_RANGE[i] and not CHECK[i][depth] :
            NUMS[pos] = NUM_RANGE[i]
            CHECK[i][depth] = True
            dfs(depth + 1, NUM_RANGE[i],pos + 1)
            CHECK[i][depth] = False

dfs(0,NUM_RANGE[0],0)