import sys

input = sys.stdin.readline

n, distance = map(int, input().split())
home_location = [0] * n
for i in range(n):
    home_location[i] = int(input())
start, end = 1, max(home_location)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt += (home_location[i] // mid)

    if cnt >= distance:
        start = mid + 1
    else:
        end = mid - 1

print(end)