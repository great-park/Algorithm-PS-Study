import sys
input = sys.stdin.readline
dp = [[0]*16 for _ in range(16)]

while True:
    try:
        white, black = map(int, input().split())
        # w = 백 선수의 수, b = 흑 선수의 수
        for w in range(15, -1, -1):
            for b in range(15, -1, -1):
                if w != 0:
                    # 백 선수 영입 x VS 영입 o
                    dp[w][b] = max(dp[w][b], dp[w-1][b] + white)
                if b != 0:
                    # 흑 선수 영입 x VS 영입 o
                    dp[w][b] = max(dp[w][b], dp[w][b-1] + black)

                # => 백 영입 vs 흑 영입 vs 영입 X
        # for i in dp:
        #     print(i)
    except:
        print(dp[15][15])
        break
