# from sys import stdin
# input = stdin.readline
# N, K = map(int, input().split())
# course = list(map(int, input().split()))
# course_sum = []
# for i in range(1, N+1):
#     course_sum.append(sum(course[:i]))

# turnning = course_sum[-1]
# turrning_count = K // turnning
# left_course = K % turnning


# if turrning_count % 2 == 0:
#     for i in range(N):
#         if left_course <= course_sum[i]:
#             print(i)
#             break
# else:
#     for i in range(N-1, -1, -1):
#         if left_course >= turnning - course_sum[i]:
#             print(i)
#             break

from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
course = list(map(int, input().split()))


def solve():
    global K
    for i in range(N):
        K -= course[i]

        if K < 0:
            print(i+1)
            return

    for i in range(N-1, -1, -1):
        K -= course[i]

        if K < 0:
            print(i+1)
            return


solve()
