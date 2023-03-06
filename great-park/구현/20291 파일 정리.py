from sys import stdin
input = stdin.readline
N = int(input())
data = list(input() for _ in range(N))
ans = {}


def find(file):
    check = list(file)
    pointer = 0
    for i in range(len(check)):
        if check[i] == '.':
            pointer = i
    return ''.join(check[pointer+1:]).rstrip()


for i in range(N):
    extension = find(data[i])
    if extension in ans:
        ans[extension] += 1
    else:
        ans[extension] = 1

result = []
for key in ans:
    result.append([key, ans[key]])
result.sort()
for x in result:
    print(x[0], x[1])
