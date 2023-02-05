import sys
input = sys.stdin.readline

N = int(input())
NUMS = list(map(int, input().split()))
UP = [1] * N
DOWN = [1] * N

for i in range(1, N) :
    """
    앞 숫자가 크거나 같으면
    UP에서 앞 숫자가 가진 상향 수열 길이값을 가져와서 +1
    """
    if NUMS[i] >= NUMS[i-1] :
        UP[i] = UP[i-1]+1
    """
    앞 숫자가 작거나 같으면
    DOWN에서 앞 숫자가 가진 하향 수열 길이값을 가져와서 +1
    """
    if NUMS[i] <= NUMS[i-1] :
        DOWN[i] = DOWN[i-1] + 1

    """
    조건문으로 분기되었고
    앞 자리 숫자가 가진 수열길이를 가져오기 때문에
    만약 상향일 경우
    하향에서는 앞 자리 숫자가 가진 값을 가져오는 연산을 안하고 건너뛰기 때문에
    처음에 저장했던 1이 계속 존재하게 됨
    (자동 초기화)
    """
    print(UP)
    print(DOWN)
    print()
    """
    [1, 2, 3, 4, 5, 6, 7, 8, 1]
    [1, 1, 2, 1, 2, 1, 1, 2, 3]
    """
"""
상향, 하향 각각 가장 길게 갔던 경우의 수들만 뽑아서
각 최대 길이에 max연산을 적용
"""
print(max(max(UP), max(DOWN)))
