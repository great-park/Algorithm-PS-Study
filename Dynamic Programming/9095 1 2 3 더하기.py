x = int(input())

# 1 : 1 (1개)
# 2 : 1+1, 2 (2개)
# 3 : 1+1+1, 1+2, 2+1, 3 (4개)
# 4 : 1+1+1+1, 1+1+2, 1+2+1, 1+3, 2+1+1, 2+2, 3+1 (7개)
# 5 : 1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+1+3, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1, 1+3+1, 3+1+1, 2+3, 3+2
#     총 13개
# ==>> n번째 경우 = n-1번째 + n-2번째 + n-3번째

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)

for i in range(x):
    n = int(input())
    print(solution(n))