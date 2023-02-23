import sys
from collections import deque
input = sys.stdin.readline
# 이동 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 정답 보관
ans = []


def BFS(a, b, M, N):  # BFS로 탐색 - graph의 값이 1인 구간에서 호출할 것임
    queue = deque([(a, b)])
    # 초기값 처리
    graph[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 지도 범위 확인
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1
    ans.append(cnt)
    return


def solve(graph, M, N):
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                BFS(i, j, M, N)
    return


# test case 개수
T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    graph = list([0]*N for _ in range(M))
    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    solve(graph, M, N)
    print(len(ans))
    ans = []
