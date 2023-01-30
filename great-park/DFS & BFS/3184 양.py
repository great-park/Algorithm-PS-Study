import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 울타리 내부를 BFS 실시
# 양과 늑대의 마리 수를 저장한다. -> 결과 계산


def BFS(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    sheep, wolf = 0, 0

    # 탐색 시작 점 -> 양 or 늑대 확인
    if graph[y][x] == 'o':
        sheep += 1
    elif graph[y][x] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < C and 0 <= next_y < R:  # 범위 확인
                if not visited[next_y][next_x] and graph[next_y][next_x] != '#':  # 탐색 가능 확인
                    queue.append([next_x, next_y])
                    visited[next_y][next_x] = True
                    # 양 or 늑대에 따라 마리 수 증가
                    if graph[next_y][next_x] == 'o':
                        sheep += 1
                    elif graph[next_y][next_x] == 'v':
                        wolf += 1
    return (sheep, wolf)


def solve():
    total_sheep, total_wolf = 0, 0
    for x in range(C):
        for y in range(R):
            if graph[y][x] != '#' and not visited[y][x]:
                sheep, wolf = BFS(x, y)

                # 해당 울타리 영역 내에서 양이 늑대보다 수가 많다면 이긴다.
                if sheep > wolf:
                    wolf = 0
                # 그렇지 않다면 모두 잡아먹힌다.
                else:
                    sheep = 0
                total_sheep += sheep
                total_wolf += wolf
    print(total_sheep, end=' ')
    print(total_wolf, end=' ')


solve()
