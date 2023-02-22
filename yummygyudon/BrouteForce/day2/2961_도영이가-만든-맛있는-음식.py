import sys
input = sys.stdin.readline



"""
1이상 10이하이기 때문에 
비트 마스킹이 가능할 것 같았다.
"""
N = int(input())
INGREDIENT = []
for _ in range(N):
    s, b = map(int, input().split())
    INGREDIENT.append([s,b])

index = 1
result = 1e9

def multi(nums:list) :
    result = nums[0]
    for i in range(1, len(nums)) :
        result *= nums[i]
    return result

while index < (1 << N) : # 16가지 경우의 수가 다 돌때 까지
    print(index,"번째 경우의 수 !")
    MIN = 1e9
    nowS, nowB = [], []
    used = ""
    for k in range(N) :
        if index & (1 << k) :
            print("k : ", k)
            print(INGREDIENT[k])
            used += str(k)+" "
            nowS.append(INGREDIENT[k][0])
            nowB.append(INGREDIENT[k][1])
            print("nowS : ", nowS)
            print("nowB : ", nowB)
            MIN = min(MIN, abs(multi(nowS)-sum(nowB)))
            print("MIN : ",MIN)
            result = min(result, MIN)
            print()
    index += 1
    print("사용한 값들의 주소 : ",used)
    print()
    print()
print(result)
"""
0 번째 경우의 수 !료


1 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
0 

2 번째 경우의 수 !
k :  1
nowS :  [2]
nowB :  [6]
MIN :  4
1 

3 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  1
nowS :  [1, 2]
nowB :  [7, 6]
MIN :  6
0 1 

4 번째 경우의 수 !
k :  2
nowS :  [3]
nowB :  [8]
MIN :  5
2 

5 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  2
nowS :  [1, 3]
nowB :  [7, 8]
MIN :  6
0 2 

6 번째 경우의 수 !
k :  1
nowS :  [2]
nowB :  [6]
MIN :  4
k :  2
nowS :  [2, 3]
nowB :  [6, 8]
MIN :  4
1 2 

7 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  1
nowS :  [1, 2]
nowB :  [7, 6]
MIN :  6
k :  2
nowS :  [1, 2, 3]
nowB :  [7, 6, 8]
MIN :  6
0 1 2 

8 번째 경우의 수 !
k :  3
nowS :  [4]
nowB :  [9]
MIN :  5
3 

9 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  3
nowS :  [1, 4]
nowB :  [7, 9]
MIN :  6
0 3 

10 번째 경우의 수 !
k :  1
nowS :  [2]
nowB :  [6]
MIN :  4
k :  3
nowS :  [2, 4]
nowB :  [6, 9]
MIN :  4
1 3 

11 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  1
nowS :  [1, 2]
nowB :  [7, 6]
MIN :  6
k :  3
nowS :  [1, 2, 4]
nowB :  [7, 6, 9]
MIN :  6
0 1 3 

12 번째 경우의 수 !
k :  2
nowS :  [3]
nowB :  [8]
MIN :  5
k :  3
nowS :  [3, 4]
nowB :  [8, 9]
MIN :  5
2 3 

13 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  2
nowS :  [1, 3]
nowB :  [7, 8]
MIN :  6
k :  3
nowS :  [1, 3, 4]
nowB :  [7, 8, 9]
MIN :  6
0 2 3 

14 번째 경우의 수 !
k :  1
nowS :  [2]
nowB :  [6]
MIN :  4
k :  2
nowS :  [2, 3]
nowB :  [6, 8]
MIN :  4
k :  3
nowS :  [2, 3, 4]
nowB :  [6, 8, 9]
MIN :  1
1 2 3 

15 번째 경우의 수 !
k :  0
nowS :  [1]
nowB :  [7]
MIN :  6
k :  1
nowS :  [1, 2]
nowB :  [7, 6]
MIN :  6
k :  2
nowS :  [1, 2, 3]
nowB :  [7, 6, 8]
MIN :  6
k :  3
nowS :  [1, 2, 3, 4]
nowB :  [7, 6, 8, 9]
MIN :  6
0 1 2 3 
"""


"""
itertools combinations 활용
"""
from itertools import combinations
combi = []
for i in range(1,N+1) :
    combi.append(combinations(INGREDIENT, i))
result = 1e9
for case in combi :
    for eachCombi in case :
        tmp_s = 1
        tmp_b = 0
        for ingredient in eachCombi :
            tmp_s *= ingredient[0]
            tmp_b += ingredient[1]
        result = min(result, abs(tmp_s-tmp_b))
print(result)




# if N >= 2 :
#
# print(result)

"""
반례
3번 재료 -> 무조건 다음 재료로 2번 재료 써야하는 것이 아닌 (1번,3번), (2번, 3번)
"""
# total_s, total_b = INGREDIENT[0][0], INGREDIENT[0][1]
# result = abs(total_s - total_b)
# print("첫 시작 result : ",result)

# if N >= 2 :
#     for i in range(1, N) :
#         # print("i : ", i)
#         tmp_s, tmp_b = INGREDIENT[i][0], INGREDIENT[i][1]
#         result = min(result, abs(tmp_s - tmp_b))
#         # print("반복 시작 result : ",result)
#         for k in range(i-1, -1, -1) :
#             tmp_s *= INGREDIENT[k][0]
#             tmp_b += INGREDIENT[k][1]
#             result = min(result, abs(tmp_s - tmp_b))
#         #     print("k : ", k)
#         #     print("k 이후 result : ", result)
#         # print()


