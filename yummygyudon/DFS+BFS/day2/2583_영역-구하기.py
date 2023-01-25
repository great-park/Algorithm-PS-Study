from collections import deque
import sys
input = sys.stdin.readline


# 높이(y축), 너비(x축), 직사각형 개수
H, W, Square = map(int,input().split())
m = [[0]*W for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(y, x) :
    q = deque()
    q.append([y,x])
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == 0 :
                m[ny][nx] = 1
                q.append([ny,nx])
                cnt += 1
    return cnt

"""
왼쪽 아래 꼭짓점의 x, y좌표값 & 오른쪽 위 꼭짓점의 x, y좌표값
"""
for _ in range(Square) :
    x1, y1, x2, y2 = map(int, input().split())
    # 직사각형 색칠
    for i in range(x1, x2) :
        for k in range(y1, y2):
            m[k][i] = 1

# 영역 갯수 세기
result = []
for i in range(H):
    for k in range(W):
        if m[i][k] == 0 :
            m[i][k] = 1
            result.append(bfs(i,k))

result.sort()
"""
BFS를 실행 했다 == 영역이 있다
영역 크기를 담는 result 요소 길이 == BFS 실행 횟수
"""
print(len(result))
for c in result :
    print(c, end = ' ')