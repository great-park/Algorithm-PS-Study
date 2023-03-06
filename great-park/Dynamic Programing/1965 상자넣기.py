import sys
input = sys.stdin.readline
N = int(input())
box = list(map(int, input().split()))
# 가장 긴 증가하는 부분 수열 문제와 동일

# i을 마지막으로 갖는 부분 수열 중 길이의 최대값
dp = [1] * N

for i in range(N):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
