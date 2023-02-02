import sys
input = sys.stdin.readline

"""
1. x가 3으로 나누어 떨어지면 3으로 나누기
2. x가 2로 나누어 떨어지면 2로 나누기
3. 1을 빼기
"""
"""
방식 1 : DFS 방식
"""
# def calculate(number : int, count : int) : # 2, 0
#     if NUMS[number] < count :
#         return
#     if number == 1 :
#         print(count)
#         sys.exit(0)
#     NUMS[number] = count
#     if number % 3 == 0 :
#         calculate(number//3, count + 1)
#     if number % 2 == 0 :
#         calculate(number//2, count + 1)
#     calculate(number-1, count + 1)

N = int(input())
NUMS = [1e9]*(N+1)
NUMS[N] = 0
"""
이미 도달 했다면 더 빨리 도착했던 것이기 때문에 min()연산으로 비교 후 저장
( 처음 도달하더라도 1e9 라는 임의의 큰 수가 있어서 자동으로 처음 도달했을 때의 연산횟수가 저장 )
"""
for num in range(N, 0, -1) : # 10
    nowValue = NUMS[num] # 0
    """
    가장 느리게 도달하는 -1 이동을 먼저 해줌
    """
    NUMS[num - 1] = min(nowValue + 1, NUMS[num - 1])
    """
    그 다음 느리게 도달하는 //2 이동을 해줌
    """
    if num % 2 == 0:
        target = num // 2
        NUMS[target] = min(nowValue+1, NUMS[target])
    """
    가장 빠르게 도달할 수 있는 //3 이동을 해줌
    """
    if num % 3 == 0 :
        target = num // 3
        NUMS[target] = min(nowValue+1, NUMS[target])
    print(NUMS)

print(NUMS[1])


"""
과거 제출 -> 메모리 & 시간 효율 훨씬 높음
N에서 1로 가는 것이 아닌
역으로 1에서 N으로 가는 방식
"""
# X = int(input())
# d= [0]*(X+1)
#
# for i in range(2, X+1) :
#     d[i] = d[i-1] +1
#     if i % 2 == 0 :
#         d[i] = min(d[i], d[i//2]+1)
#     if i % 3 == 0 :
#         d[i] = min(d[i], d[i//3]+1)
# print(d[X])