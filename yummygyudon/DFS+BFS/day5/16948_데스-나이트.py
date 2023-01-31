from collections import deque
import sys
input = sys.stdin.readline

d = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

N = int(input())
nowY, nowX, targetY, targetX = map(int, input().split())

VISITED = [[-1]*N for _ in range(N)]


def bfs(y, x) :
    q = deque()
    q.append([y, x, 0])
    VISITED[nowY][nowX] = 0
    while q :
        y,x,move = q.popleft()
        if y == targetY and x == targetX :
            return move
        for dy,dx in d :
            nextY = y + dy
            nextX = x + dx
            if (0 <= nextY < N) and (0 <= nextX < N) and VISITED[nextY][nextX] == -1 :
                VISITED[nextY][nextX] = move+1
                q.append([nextY, nextX, move+1])
    return -1

print(bfs(nowY, nowX))