import sys
input = sys.stdin.readline
A = int(input())
data = list(map(int, input().split()))
# dp[i] =  data[i]을 마지막 값으로 가지는 가장 긴 증가하는 부분 수열의 길이
dp = [1] * (A)

for i in range(A):
    for j in range(i):
      # data[i]가 마지막 값이 되기 위해 이전 마지막 값보다 커야 됨
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
