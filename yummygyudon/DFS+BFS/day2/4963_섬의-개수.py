import sys
input = sys.stdin.readline
dx =[0,0,1,-1, 1,1,-1,-1]
dy =[1,-1,0,0, 1,-1,1,-1]

from collections import deque

def bfs(w,h) :
    q = deque()
    q.append([h, w])
    visited[h][w] = 1
    while q:
        h, w = q.popleft()
        for i in range(8):
            nw = w + dx[i]
            nh = h + dy[i]
            if 0 <= nw < W and 0 <= nh < H:
                if m[nh][nw] == 1 and visited[nh][nw] == 0:
                    visited[nh][nw] = 1
                    q.append([nh, nw])


while True :
    W, H = map(int, input().split())
    if W==0 and H ==0 :
        break
    m = []
    visited = [[0]*W for _ in range(H)]
    for _ in range(H) :
        m.append(list(map(int, input().split())))

    land=0
    for i in range(H):
        for k in range(W) :
            if m[i][k] == 1 and visited[i][k] == 0 :
                bfs(k,i)
                land+=1
    print(land)