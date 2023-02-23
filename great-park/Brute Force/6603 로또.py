from sys import stdin
input = stdin.readline


def DFS(depth, temp, k, data):
    if depth == 6:
        print(*temp)

    for i in range(k):
        if data[i] not in temp:
            if len(temp) == 0:
                temp.append(data[i])
                DFS(depth+1, temp, k, data)
                temp.pop()
            elif data[i] > temp[-1]:
                temp.append(data[i])
                DFS(depth+1, temp, k, data)
                temp.pop()


while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    k, data = data[0], data[1:]
    DFS(0, [], k, data)
    print()
