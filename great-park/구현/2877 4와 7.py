import math
K = int(input())
"""
    4, 7
    44, 47, 74, 77
    444, 447, 474, 477, 744, 747, 774, 777
    4444444  4444447
    => n의 자리 -> 2^n의 경우의 수

    -> ex) 474 -> 4*100 + 7*10 + 4*1 => 010 
    -> 3자리수의 3번째 => 2 + 4 // + 3 = 9번째
    -> 
    """
if K == 1:
    print(4)
else:
    scale = 0
    for i in range(1, K):
        x = int(math.pow(2, i))
        if K-x < 0:
            scale = i
            break
        K -= x
    ans = ''
    b_K = list(format(K-1, 'b'))
    front_four_count = K - len(b_K)
    for _ in range(front_four_count):
        ans += '4'
    for value in b_K:
        if value == '1':
            ans += '7'
        else:
            ans += '4'
    print(ans)
