import sys
input = sys.stdin.readline

"""
A : 1
B : 2
Z : 26
-> ASCII 

"""
"""
<idx>
 0  1  2  3  4  5
[0, 2, 5, 1, 1, 4]
[1, 1, 0, 0, 0, 0] = 초기 DP

* 1번째 자릿수가 0이면 애초에 불가능하고 어차피 0보다 크다면 26안에 무조건 들기 때문에 1로 고정
* 3자릿수는 애초에 불가능하기 때문에 앞자리까지 합쳤을 경우만 확인하면 된다.

ex. [2] 자리 : 5이기 때문에 앞서 2([i-1])까지의 경우의 수까지 5를 이어붙여서 사용 가능 -> += DP[i-1]
    [1:2] 자리 : 25이기 때문에 가능 -> 0([i-2])까지의  경우의 수에서 25를 이어붙여서 사용가능  -> DP[i-2]
    [3] 자리를 보면 1이기 때문에 앞에 2, 5까지의 경우의 수(DP[i-1])를 사용할 수 있음
     but,  [2:3]이 26보다 크면 사용할 수 없기 때문에 2 까지의 경우의 수 (DP[i-2]) 사용 불가
"""
# CRYPTO_NUM = int(input())
CRYPTO_NUM = list(input().rstrip())
if CRYPTO_NUM[0] == '0' :
    print(0)
else :
    SIZE = len(CRYPTO_NUM)
    CRYPTO_NUM = ['0']+CRYPTO_NUM
    DP = [0] * (SIZE + 1)
    DP[0], DP[1] = 1, 1
    for i in range(2, SIZE+1) :
        if int(CRYPTO_NUM[i]) > 0 :
            DP[i] += DP[i-1]

        """
        ⬇ 2자리로 바꾸었을 때 계산 ⬇
        앞자리가 0일 경우 앞자리 확인할 필요 없음
        (붙여도 결국 첫번째 if문에서 처리한 값이기 때문에)
        """
        if CRYPTO_NUM[i-1] == '0' :
            continue
        """
        
        앞자리가 1이거나 (1이면 0부터 9 어떤 값이 와도 가능)
        
        앞자리가 2지만 해당 자리가 6보다 작거나 같으면 (20 ~ 26은 가능)
        앞자리와 합쳤다는 가정 하에 
        두 칸 앞 자리까지의 경우의 수를 따를 수 있음
        """
        if (CRYPTO_NUM[i-1] == '1') or (CRYPTO_NUM[i-1] == '2' and int(CRYPTO_NUM[i]) <= 6) :
            DP[i] += DP[i-2]
        print(DP)
    print(DP[SIZE]%1_000_000)




