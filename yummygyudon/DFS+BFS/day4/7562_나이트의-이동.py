from collections import deque
import sys
input = sys.stdin.readline

# 9시 방향 -> 정시계방향으로 순서대로
d = [[-1, -2],[-2, -1],[-2, 1],[-1 ,2], [1, 2],[2, 1],[2,-1],[1,-2]]
def moveChess(nowPosition : list, targetPosition : list, visitCheckList : list, boardSize : int) :
    n_y, n_x = nowPosition
    t_y, t_x = targetPosition
    q = deque()
    q.append([n_y, n_x, 0])
    visitCheckList[n_y][n_x] = True
    while q :
        y, x, move = q.popleft()
        if (y == t_y) and (x == t_x) :
            print(move)
            break
        for i in range(8) :
            next_y = y + d[i][0]
            next_x = x + d[i][1]
            if (0 <= next_y < boardSize) and (0 <= next_x < boardSize) and not(visitCheckList[next_y][next_x]) :
                visitCheckList[next_y][next_x] = True
                q.append([next_y, next_x, move+1])



TC = int(input())
for _ in range(TC) :
    I = int(input())
    now = list(map(int, input().split()))
    target = list(map(int, input().split()))
    visited = [[False]*I for _ in range(I)]
    moveChess(now, target, visited, I)

