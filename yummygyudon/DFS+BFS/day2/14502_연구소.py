import copy
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 0:빈 칸 / 1:벽 / 2:바이러스
LAB_MAP = []
moving = [[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(N) :
    LAB_MAP.append(list(map(int, input().split())))



# 벽 3개가 세워지는 모든 경우의 수에서 bfs 수행
def bfs() :
    q = deque()
    current_map = copy.deepcopy(LAB_MAP)
    for y in range(N) :
        for x in range(M) :
            if LAB_MAP[y][x] == 2 :
                q.append([y,x])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + moving[i][0]
            nx = x + moving[i][1]
            if 0 <= ny < N and 0 <= nx < M :
                if current_map[ny][nx] == 0 :
                    current_map[ny][nx] = 2 # 감염 처리
                    q.append([ny,nx])

    global answer
    empty_cnt = 0
    for y in range(N) :
        for x in range(M) :
            if current_map[y][x] == 0 :
                empty_cnt += 1
    answer = max(answer, empty_cnt)

def dfs(wall_cnt) :
    if wall_cnt == 3 : # 경우에 따라 벽을 세우는게 아니라 모든 3개의 벽을 세운 상황을 확인하는 방법
        bfs()
        return
    # 모든 빈칸의 위치에서 dfs 시작
    for y in range(N) :
        for x in range(M) :
            if LAB_MAP[y][x] == 0 :
                LAB_MAP[y][x] = 1 # 벽으로 만들어주고
                dfs(wall_cnt+1) # 벽으로 만든 경우에서의 상황으로 dfs 재귀
                LAB_MAP[y][x] = 0 # 다시 원상복귀 -> 초기화의 부분때문에 bfs에서 deepcopy가 필요한 것

answer = 0
dfs(0)
print(answer)