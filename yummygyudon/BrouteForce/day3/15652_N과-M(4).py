from sys import stdin
input = stdin.readline

TARGET_NUM, TARGET_POS = map(int, input().split())
CHECK = [[False]*TARGET_POS] * TARGET_NUM
NUMS = [0] * TARGET_POS

def dfs(depth,pos,num) :
    if pos == TARGET_POS :
        print(*NUMS)
        return

    for i in range(num,TARGET_NUM) :
        if not CHECK[pos][depth] :
            NUMS[pos] = i+1
            CHECK[i][depth] = True
            dfs(depth+1, pos+1,i)
            CHECK[i][depth] = False
dfs(0,0,0)