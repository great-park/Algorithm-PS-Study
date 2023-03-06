from sys import stdin
input = stdin.readline
N = int(input())
seq = list(map(int, input().split()))
ans = []
idx_list = []
each_result = []
MAX = 0


def calculate(ans):
    global MAX
    temp = 0
    for i in range(N-1):
        temp += abs(ans[i] - ans[i+1])
    MAX = max(MAX, temp)


def DFS():
    if len(ans) == N:
        calculate(ans)
        return

    for i in range(N):
        if i not in idx_list:
            idx_list.append(i)
            ans.append(seq[i])
            DFS()
            ans.pop()
            idx_list.pop()


DFS()
print(MAX)
