from sys import stdin
input = stdin.readline

TARGET_NUM, TARGET_POS = map(int, input().split())
CHECK = [False] * TARGET_NUM
NUMS = [0] * TARGET_POS
# print(NUMS)
#
def calc(cnt, num) :
    if cnt == TARGET_POS :
        print(*NUMS)
        return
    for n in range(num, TARGET_NUM) :  # 0, 1 ,2, 3
        if not CHECK[n] :
            # print("now Pos :", cnt)
            # print("now num :", n+1)
            NUMS[cnt] = n+1
            CHECK[n] = True
            calc(cnt+1, n)
            CHECK[n] = False
calc(0,0)