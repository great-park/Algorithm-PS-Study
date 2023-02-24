from sys import stdin
input = stdin.readline

NUM_QUANTITY, TARGET_POS = map(int, input().split())

NUM_RANGE = list(map(int, input().split()))
NUM_RANGE.sort()

CHECK = [[False]*TARGET_POS for _ in range(NUM_QUANTITY)]
NUMS = [0] * TARGET_POS

def dfs(depth, pos) :
    if pos == TARGET_POS :
        print(*NUMS)
        return
    for i in range(NUM_QUANTITY) :
        if not CHECK[i][depth] :
            NUMS[pos] = NUM_RANGE[i]
            CHECK[i][depth] = True
            dfs(depth+1, pos+1)
            CHECK[i][depth] = False
dfs(0,0)
