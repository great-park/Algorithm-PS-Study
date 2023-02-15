

import sys
N = int(sys.stdin.readline())
schedule = []
for _ in range(N) :
    schedule.append(list(map(int, sys.stdin.readline().split())))

schedule.sort(key= lambda x : x[0])
schedule.sort(key = lambda x : x[1])
last = 0
cnt = 0
for st, lt in schedule:
    if last <= st:
        cnt += 1
        last = lt
print(cnt)