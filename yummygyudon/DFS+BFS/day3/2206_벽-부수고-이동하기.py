from collections import deque
import sys
input = sys.stdin.readline

"""
(1,1) 출발 ~ (N, M) 도착이지만
(0,0) 출발 ~ (N-1, M-1) 과 동일하기 때문에 상관 없음
"""
# N : 세로 / M : 가로
N, M = map(int, input().split())
MAP = [list(map(int, list(input().rstrip()))) for _ in range(N)]

"""
MOVE 삼중 리스트
- Depth 3 index 0층 : 벽을 안부수고 가는 경로
- Depth 3 index 1층 : 벽을 부수고 가는 경로
"""
MOVE =[ [[0]*2 for _ in range(M)] for _ in range(N)] # 0과 1을 갖는 crush 값을 통해 indexing까지
# 우, 좌, 히, 싱
d = [[0,1], [0,-1], [1,0], [-1,0]]

""" (0,0)은 항상 0이라는 가정 """
def startMove() :
    q = deque()
    # MOVE에서 최단 거리 체크를 하기 때문에 Heap 활용 실패
    # q.append([0,0,0,False]) # [ (y좌표), (x좌표), (부순 횟수) ]
    # heapq.heappush(heap, [0,0,0,0])
    q.append([0,0,0])
    """
    처음 시작 : 안 부순 상태이기 때문에 0
    - 시작하는 칸과 끝나는 칸도 포함해서 센다는 조건
    """
    MOVE[0][0][0] = 1
    while q :
        y, x, crush = q.popleft()
        if (y == N-1) and (x == M-1) :
            # 초기 result 변수에 값을 대입하는 방식 -> 런타임 에러 -> 바로 return해서 끝내기
            return MOVE[y][x][crush]
        for i in range(4) :
            ny = y + d[i][0]
            nx = x + d[i][1]
            if 0 <= ny < N and 0 <= nx < M :
                """벽일 경우 & 한번도 부순적 없는 경우"""
                """
                벽은 "한 번"만 부술 수 있음
                """
                if MAP[ny][nx] == 1 and crush == 0:
                    MOVE[ny][nx][1] = MOVE[y][x][crush] + 1 # 이동 전에 저장되어 있던 값
                    q.append([ny, nx, 1]) # crush를 1로 변경
                """이동 가능한 칸일 경우 & 해당 crush의 상태로 최초 방문인 경우 : 동일 crush 층 내에서 최단 거리로 도착한 경우"""
                if MAP[ny][nx] == 0 and MOVE[ny][nx][crush] == 0  :
                    MOVE[ny][nx][crush] = MOVE[y][x][crush] + 1
                    q.append([ny, nx, crush]) # crush 유지
    return -1

print(startMove())







"""
과거 제출 코드
"""
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# d = [[0,1], [0,-1], [1,0], [-1,0]]
#
# def bfs() :
#     q = deque()
#     q.append([0, 0, 1]) # (1,1) 좌표 시작 & 벽 부술 수 있는 횟수
#     # 끝나는 칸도 포함해서 세야함
#     dis = [[[0] * 2 for _ in range(W)] for _ in range(H)]
#     dis[0][0][1] = 1
#     while q :
#         x, y, crack = q.popleft()
#         if x == W-1 and y == H-1 :
#             return dis[y][x][crack]
#         for i in range(4):
#             nx = x+d[i][0]
#             ny = y+d[i][1]
#             if 0 <= nx < W and 0 <= ny < H :
#                 if m[ny][nx] == 1 and crack == 1  :#and dis[ny][nx][crack-1] == 0
#                     dis[ny][nx][0] = dis[y][x][1] + 1
#                     q.append([nx, ny, 0])
#                 elif m[ny][nx] == 0  and dis[ny][nx][crack] == 0 :
#                     dis[ny][nx][crack] = dis[y][x][crack] + 1
#                     q.append([nx, ny, crack])
#     return -1
#
# H, W =  map(int, input().split())
# m = [list(map(int, list(input().rstrip()))) for _ in range(H)]
# print(bfs())