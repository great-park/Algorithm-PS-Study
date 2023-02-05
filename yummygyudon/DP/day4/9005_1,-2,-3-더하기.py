import sys
input = sys.stdin.readline

N = int(input())

"""
CASE 1 : 단순 조건식 활용
"""
def fibo(num) :
    if num == 1 :
        return 1
    elif num == 2 :
        return 2
    elif num == 3 :
        return 4
    else :
        return fibo(num-3) + fibo(num-2) + fibo(num-1)

for i in range(N):
    print(fibo(int(input())))

"""
CASE 2 : 기본 값 구성 DP Array & DFS 활용하기
"""
# 최소 경우의 수 DP
basic_case = [0, 1, 2, 4]

# n-3, n-2, n-1 들이 1,2,3 중 하나의 값이면 return 됨
# 입력값 조건이 1 이상의 값부터이기 때문에 문제는 발생하지 않음.
def sum_case(n):
    if n == 1 :
        return basic_case[1]
    elif n == 2 :
        return basic_case[2]
    elif n == 3 :
        return basic_case[3]
    return sum_case(n-3)+sum_case(n-2)+sum_case(n-1)

for _ in range(N):
    print(sum_case(int(input())))