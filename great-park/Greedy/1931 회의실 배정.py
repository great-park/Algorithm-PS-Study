import sys

N = int(input())
time_table = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append([start, end])

# 순서대로 정렬 후 일찍 끝나는 순으로 배치
# time_table.sort(key=lambda x: x[1])
"""
  13
  34
  44
  
  13
  44
  34
  이 경우 34을 원래 할 수 있는데 ex_room[1]이 3에서 4가 되면서 제외됨
"""
time_table.sort(key=lambda x: x[0])
time_table.sort(key=lambda x: x[1])
count = 1
ex_room = time_table[0]
for room in time_table[1:]:
    if ex_room[1] <= room[0]:
        count += 1
        ex_room = room
print(count)
