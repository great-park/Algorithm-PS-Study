from sys import stdin
input = stdin.readline

NUM_QUANTITY, TARGET_POS = map(int, input().split())

NUM_RANGE = list(map(int, input().split()))
NUM_RANGE.sort()
CHECK = [False] * NUM_QUANTITY
NUMS = [0] * TARGET_POS

def dfs(pos, index) :
    if pos == TARGET_POS :
        print(*NUMS)
        return

    for i in range(index,NUM_QUANTITY) :
        if not CHECK[i] :
            NUMS[pos] = NUM_RANGE[i]
            CHECK[i] = True
            dfs(pos+1, i+1)
            CHECK[i] = False
dfs(0,0)