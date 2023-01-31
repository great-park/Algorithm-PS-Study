
"""
그림 : 상하좌우 방향 1로 연결된 것 -> 넓이 == 1의 개수

가장 넓은 그림의 넓이 출력
"""

"""
DFS 방식 : Recursion Error 재귀 오류 발생
"""
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# BOARD = []
# for _ in range(N) :
#     BOARD.append(list(map(int, input().split())))
#
# d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
# VISITED = [[False]*M for _ in range(N)]
# MAX = 0
# PAINT_COUNT = 0
# count = 0
# def paint(y, x) :
#     global count
#     count += 1
#     VISITED[y][x] = True
#     for i in range(4) :
#         nextY = y + d[i][0]
#         nextX = x + d[i][1]
#         if (0 <= nextY < N) and (0 <= nextX < M) and (BOARD[nextY][nextX] == 1) and not(VISITED[nextY][nextX]):
#             paint(nextY, nextX)
#
#
# for i in range(N) :
#     for k in range(M) :
#         if BOARD[i][k] == 1 and not(VISITED[i][k]) :
#             PAINT_COUNT += 1
#             paint(i, k)
#             MAX = max(count, MAX)
#             count = 0
# print(PAINT_COUNT)
# print(MAX)


"""
BFS 방식
"""
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

BOARD = []
for _ in range(N) :
    BOARD.append(list(map(int, input().split())))

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

VISITED = [[False]*M for _ in range(N)]
"""
그림이 한개도 없을 경우 -> BFS 함수 실행 0번
0을 그대로 출력
"""
MAX = 0
PAINT_COUNT = 0
def paintByBFS(y, x) :
    q = deque()
    q.append([y,x])
    """
    자기 자신 넓이 & 방문 처리 -> 자기 자신만 있을 때, 1이 그대로 출력
    """
    count = 1
    VISITED[y][x] = True
    while q :
        nowY, nowX= q.popleft()
        for i in range(4):
            nextY = nowY + d[i][0]
            nextX = nowX + d[i][1]
            """
            전체 영역에 벗어나지 않고 1이며 한번도 방문하지 않은 칸일 경우,
            == 그림 영역 발견
            """
            if (0 <= nextY < N) and (0 <= nextX < M) and BOARD[nextY][nextX] == 1 and not(VISITED[nextY][nextX]):
                """
                반환할 count 값에 +1 누적합 & 방문 처리 & 큐에 삽입
                """
                count+=1
                VISITED[nextY][nextX] = True
                q.append([nextY, nextX])
    return count

for i in range(N) :
    for k in range(M) :
        """
        BFS 처리가 안된 1 블럭이 발견되었을 때 BFS 실행
        """
        if BOARD[i][k] == 1 and not VISITED[i][k] :
            """
            - 전체 그림 갯수에 +1
            - 최대 넓이 갱신 : (이전 갱신값 & BFS 반환값
            """
            PAINT_COUNT += 1
            MAX = max(MAX, paintByBFS(i, k))

print(PAINT_COUNT)
print(MAX)