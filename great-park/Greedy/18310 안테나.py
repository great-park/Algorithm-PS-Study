from sys import stdin
input = stdin.readline
N = int(input())
home = list(map(int, input().split()))

# 본인을 제외한 나머지 집들로의 거리의 합이 가장 작은 집을 고른다.
# min = 1e9
# result = []
# for i, location in enumerate(home):
#     sum = 0
#     for left in range(N):
#         sum += location - home[left]
#     if sum < min:
#         min = sum
#         result.append(i)
# result.sort()
# print(home[result[0]])

home.sort()
mid_index = (N-1) // 2

print(home[mid_index])
