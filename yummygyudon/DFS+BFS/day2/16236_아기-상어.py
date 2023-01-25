from collections import deque
import heapq
import sys
input = sys.stdin.readline

moving = [[0,1],[0,-1],[1,0],[-1,0]]
N = int(input())
MAP = []
"""
가장 처음에 아기 상어의 크기는 2
1초에 상하좌우로 인접한 한 칸씩 
"""

start_x, start_y = 0, 0
start_size = 2
for i in range(N):
    layer = list(map(int, input().split()))
    MAP.append(layer)
    for j in range(N) :
        if (layer[j] == 9) :
            start_y = i
            start_x = j

########################
def findFish(y,x,size) :
    q = deque()
    q.append( [y,x,0] )
    ableToEat = []
    visited = [[False]*N for _ in range(N)]
    visited[y][x] = True
    while q:
        y, x, move = q.popleft()
        for i in range(4) :
            ny = y + moving[i][0]
            nx = x + moving[i][1]
            n_move = move+1
            if (0 <= ny < N and 0 <= nx < N) and not visited[ny][nx]:
                """
                자신의 크기보다 큰 물고기 : 먹기 X, 이동 X
                자신과 크기가 같은 물고기 : 먹기 X, 이동 O
                자신보다 크기가 작은 물고기 : 먹기 O, 이동 O

                작거나 같으면 이동 가능 -> 작으면 먹기까지 가능
                """
                if (MAP[ny][nx] <= size) :
                    q.append([ny,nx,n_move])
                    visited[ny][nx] = True
                    if MAP[ny][nx] < size and MAP[ny][nx] != 0:
                        ableToEat.append([n_move, ny, nx])
                        # heapq.heappush(ableToEat, [n_move, ny, nx]) -> 나중에 힙으로 활용해보기
    """
    거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
    그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기
    -> 정렬 순서 : 거리 - y좌표 - x좌표 순
    """
    ableToEat.sort()
    return ableToEat


wasteTime = 0
eatenSize = 0
while True :
    MAP[start_y][start_x] = 0
    result = findFish(start_y, start_x, start_size)
    if not result :
        print(wasteTime)
        break
    else :
        move_cnt, n_y, n_x = result[0][0], result[0][1], result[0][2]
        wasteTime += move_cnt
        start_y = n_y
        start_x = n_x
        eatenSize += 1
        """
        물고기를 먹으면, 그 칸은 빈 칸이 된다.

        자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가
        (크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3)
        """
        if eatenSize == start_size :
            start_size += 1
            eatenSize = 0
