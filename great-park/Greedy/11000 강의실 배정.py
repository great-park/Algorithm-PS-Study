# from sys import stdin
# from collections import deque
# input = stdin.readline
# N = int(input())
# time_table = []
# for i in range(N):
#     time_table.append(list(map(int, input().split())))
# # 강의 시간이 길면 짧은 강의를 포함시킬 수 있기때문에 시작시간 순으로 정렬
# time_table.sort(key=lambda x: (x[0], x[1]))

"""
1
"""
# ex_room = time_table[0]
# cnt = 0
# for i in range(1, N):
#     if time_table[i][0] >= ex_room[1]:
#         cnt += 1
#         ex_room = time_table[i]
#     else:
#         cnt += 1
# print(cnt)

"""
2
"""
# ans = deque()  # 끝나는 시간 담기
# ans.append(time_table[0][1])

# for i in range(1, N):
#     if time_table[i][0] >= ans[0]:
#         ans.popleft()
#         ans.append(time_table[i][1])
#     else:
#         ans.append(time_table[i][1])
# print(len(ans))

import heapq
import sys

N = int(input())
C = []
h = []
for i in range(N):
    C.append(list(map(int, sys.stdin.readline().split())))

C = sorted(C,key = lambda x: x[0])

for i in range(N):
    if len(h) != 0 and h[0]<= C[i][0]:
        heapq.heappop(h)
    heapq.heappush(h,C[i][1])
    
print(len(h))
