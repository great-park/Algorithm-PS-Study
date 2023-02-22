# from sys import stdin
# from collections import deque

# input = stdin.readline
# N = int(input())
# map = [list(input().rstrip()) for _ in range(N)]
# # dx = [0, 0, 1, -1]
# # dy = [1, -1, 0, 0]

# # def BFS(x, y):
# #     cnt = 0
# #     queue = deque([(x, y)])
# #     visited = [[False for _ in range(N)] for _ in range(N)]
# #     visited[y][x] = True
# #     while queue:
# #         x, y = queue.popleft()
# #         for i in range(4):
# #             nx, ny = x+dx[i], y+dy[i]
# #             if not visited[ny][nx]:
# #                 print(nx, ny)
# #                 if 0 <= nx and nx < N and 0 <= ny and ny < N:
# #                     if map[y][x] == map[ny][nx]:
# #                         queue.append([nx, ny])
# #                         visited[ny][nx] = True
# #                         cnt += 1
# #     return cnt

# # BFS가 아니라 행, 열 1줄로 탐색해야 함
# MAX = 0


# def search():
#     global MAX
#     for i in range(N):
#         cnt = 1
#         for j in range(1, N):
#             if map[i][j] == map[i][j-1]:
#                 cnt += 1
#                 NAX = max(cnt, MAX)
#             else:
#                 cnt = 1

#         for k in range(1, N):
#             if map[k][i] == map[k-1][i]:
#                 cnt += 1
#                 NAX = max(cnt, MAX)
#             else:
#                 cnt = 1


# for i in range(N):
#     for j in range(N):
#         if i + 1 < N:  # i + 1이 N 이내라면 교환 가능
#             map[i][j], map[i+1][j] = map[i+1][j], map[i][j]
#             search()
#             map[i][j], map[i+1][j] = map[i+1][j], map[i][j]
#         if j + 1 < N:
#             map[i][j], map[i][j+1] = map[i][j+1], map[i][j]
#             search()
#             map[i][j], map[i][j+1] = map[i][j+1], map[i][j]

# print(MAX)



import sys
input = sys.stdin.readline
# count는 data에서 오른쪽,아래로 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수
def count(data):
    Max = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if data[i][j] == data[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max,cnt)
        cnt = 1
        for j in range(1,n):
            if  data[j][i] == data[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            Max = max(Max,cnt)

    return Max
# 오른쪽 하고 아래부분만 신경써주면된다.
n = int(input())
data = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
        	# 인점한 것과 바꾸기
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
            temp=count(data)
            ans = max(ans,temp)
            # 바꿨던 것을 다시 원래대로 돌려놓기
            data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        # 행 바꾸기
        if i+1 < n:
        	# 인점한 것과 바꾸기
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
            temp=count(data)
            ans = max(ans,temp)
            # 바꿨던 것을 다시 원래대로 돌려놓기
            data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
print(ans)