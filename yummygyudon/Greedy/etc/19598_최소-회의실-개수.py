from sys import stdin
import heapq

input = stdin.readline
N = int(input())
SCHEDULE = []
ROOM = []

for i in range(N) :
    SCHEDULE.append(list(map(int, input().split())))
SCHEDULE.sort(key = lambda x : (x[0], x[1]))
heapq.heappush(ROOM, SCHEDULE[0][1])
for s, e in SCHEDULE[1:] :
    if ROOM[0] <= s :
        heapq.heappop(ROOM)
    heapq.heappush(ROOM, e)
print(len(ROOM))
