import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# index 0층: 벽을 안 부수고 가는 경로
# index 1층: 벽을 부수고 가는 경로
move = [[[0, 0] for _ in range(M)] for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(x, y):
    queue = deque([(x, y, 0)])  # x좌표, y좌표, 부순 횟수
    move[y][x][0] = 1

    while queue:
        x, y, break_cnt = queue.popleft()

        if (x, y) == (M-1, N-1):
            return move[y][x][break_cnt]

        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:  # 범위 확인

                # 벽인 경우 벽을 부순다.
                if graph[next_y][next_x] == 1 and break_cnt == 0:
                    move[next_y][next_x][1] = move[y][x][0] + 1  # 기존 graph는 유지
                    queue.append([next_x, next_y, 1])

                # 이동 가능하며, 해당 break_cnt 층에서 아직 방문하지 않은 경우
                if graph[next_y][next_x] == 0 and move[next_y][next_x][break_cnt] == 0:
                    move[next_y][next_x][break_cnt] = move[y][x][break_cnt] + 1
                    queue.append([next_x, next_y, break_cnt])
    return -1


print(BFS(0, 0))
