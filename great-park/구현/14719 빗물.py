# from sys import stdin
# input = stdin.readline
# H, W = map(int, input().split())
# blocks = list(map(int, input().split()))
# max_height = max(blocks)
# size = len(blocks) - 1


# def check_row(h):
#     rain_area = 0
#     green_area = 0
#     flag = 0
#     for i in range(size+1):
#         if blocks[i] < h:
#             green_area += 1
#         else:
#             flag += 1
#             if flag > 1:
#                 # 연속된 높은 기둥 지나치기
#                 while(True):
#                     if i+1 <= size:
#                         if blocks[i+1] <= height:
#                             i += 1
#                         else:
#                             break
#                     else:
#                         break

#                 flag = 0
#                 rain_area = green_area
#             green_area = 0
#     return rain_area


# ans_area = 0
# for height in range(max_height, 0, -1):
#     ans_area += check_row(height)
# print(ans_area)

H, W = [*map(int, input().split())]
blocks = [*map(int, input().split())]
result = 0  # 빗물의 고인 양
for i in range(1, W-1):  # 맨 왼쪽과 맨 오른쪽은 고일 수 없다.
    left_max = max(blocks[:i])  # 왼쪽에서 제일 높은 블록
    right_max = max(blocks[i+1:])  # 오른쪽에서 제일 높은 블록

    lower_one = min(left_max, right_max)  # 그중 가장 낮은 블록

    if blocks[i] < lower_one:  # 현재 블록이 lower_one 블록 보다는 낮아야 빗물이 고인다.
        result += lower_one - blocks[i]
print(result)
