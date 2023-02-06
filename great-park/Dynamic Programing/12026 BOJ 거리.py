# k칸 만큼 점프를 하는데 필요한 에너지의 양은 k*k
import sys
input = sys.stdin.readline
N = int(input())
blocks = list(input().rstrip())
visited = True
dp = list([1e9, not visited] for _ in range(N))
dp[0][0], dp[0][1] = 0, True


for i in range(1, N):
    block = blocks[i]
    check_jump = '?'

    if block == 'B':
        check_jump = 'J'
    elif block == 'O':
        check_jump = 'B'
    else:
        check_jump = 'O'

    for j in range(i):
        if check_jump == blocks[j]:
            print("---------------------------")
            print(check_jump, block, " j, i ->", j, i)
            print()

            print(dp[i][0], "점프 X")
            print(dp[j][0], "점프하기전,", pow(i-j, 2),
                  "더하면",  dp[j][0] + pow(i-j, 2))
            # j -> i로 점프
            dp[i][0] = min(dp[i][0], dp[j][0] + pow(i-j, 2))
            print(dp[i][0], '결과')
            print("---------------------------")
            if dp[i][0] != 1e9:
                dp[i][1] = True

if dp[N-1][1]:
    print(dp[N-1][0])
else:
    print(-1)
