from sys import stdin
from itertools import combinations
input = stdin.readline
N = int(input())
foods = []
for i in range(N):
    foods.append(list(map(int, input().split())))
# 0번-곱, 1번-합
min = 1e9

combination = []
# 모든 경우의 수
for i in range(1, N+1):
    combination.append(combinations(foods, i))

for each_count in combination:
    for each_case in each_count:  # ([3, 8], [5, 8])
        s, b = 1, 0
        for food in each_case:  # [3, 8]
            s *= food[0]
            b += food[1]
        temp_result = abs(s-b)
        if temp_result < min:
            min = temp_result
print(min)
