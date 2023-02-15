import sys
input = sys.stdin.readline

""" 메모리 초과 """
# N, K = map(int, input().split())
# SECTIONS = list(map(int,input().split()))
# COURSE = [0]*sum(SECTIONS)
# index = 0
# for i in range(1, N+1) : # 0, 1, 2, 3, 4,
#     for _ in range(SECTIONS[i-1]) :
#         COURSE[index] = i
#         index += 1
#
# if K < len(COURSE) :
#     print(COURSE[K])
# else :
#     print(COURSE[-(K-len(COURSE))])

"""통과"""
N, K = map(int, input().split())
SECTIONS = [0]+list(map(int,input().split()))
# pathCost = sum(SECTIONS)

for i in range(1,N+1) :
    K -= SECTIONS[i]
    if K < 0 :
        print(i)
        break
if K >= 0 :
    for i in range(N, 0, -1) :
        K -= SECTIONS[i]
        if K < 0 :
            print(i)
            break

