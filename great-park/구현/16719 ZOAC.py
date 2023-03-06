from sys import stdin
from collections import deque

input = stdin.readline
_data = list(input().rstrip())
size = len(_data)
data = []
ans = ['?' for _ in range(size)]  # 출력 순서

for i, x in enumerate(_data):
    data.append([x, i])
data.sort(reverse=True)  # [[Z, 0], [O, 1], [C, 3], [A, 2]]

stack = deque()  # [[A, 2], [C, 3], [O, 1], [Z, 0]]
for element in data:
    stack.append(element)

first = stack.pop()
ans[first[1]] = first[0]  # [?, ?, A, ?]


def print_line():
    sub_result = ''
    for i in range(size):
        if ans[i] != '?':
            sub_result += ans[i]
    print(sub_result)


if size == 1:
    print(data[0][0])
else:
    while stack:
        # 한 번 출력 시 -> data에서 해당 문자 지우기 + ans에 추가하기
        print_line()  # 한 줄 출력
        next = stack.pop()
        ans[next[1]] = next[0]  # [?, ?, A, C]
    print_line()
