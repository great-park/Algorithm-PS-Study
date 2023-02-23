from sys import stdin
input = stdin.readline
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for people in data:
    cnt = 0

    # 나보다 덩치가 큰 사람 수 구하기
    for another in data:
        if people[0] < another[0] and people[1] < another[1]:
            cnt += 1
    print(cnt+1, end=' ')


# win_cnt = [[i, 0] for i in range(N)]

# for i in range(N):
#     for k in range(N):
#         if i != k:
#             one = data[i]
#             two = data[k]
#             if one[0] > two[0]:
#                 if one[1] > two[1]:
#                     win_cnt[i][1] += 1
#             elif two[0] > one[0]:
#                 if two[1] > two[1]:
#                     win_cnt[k][1] += 1
# win_cnt.sort(key=lambda x: x[1], reverse=True)
# rank = [0]*N
# cur = 1
# next = cur
# for idx, rank_info in enumerate(win_cnt):
#     real_idx = rank_info[0]

#     if idx != 0:
#         if win_cnt[idx][1] == win_cnt[idx-1][1]:
#             rank[real_idx] = cur
#             next += 1
#         else:
#             rank[real_idx] = next
#             next += 1
#             cur = next


# print(rank)
