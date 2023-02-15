import sys
input = sys.stdin.readline

ODD = ['1','3','5','7','9']
oddCount = []
def dfs(cnt, numArr : list) :
    """
    numArr : str 요소 List
    들어올 수 있는 경우의 수
    - 한 자릿 수
    - 두 자릿 수
    - 세 자릿 수 이상
    """
    # global oddCount
    # print("This time : ", numArr)
    # temp = 0
    for num in numArr :
        """
        값 내의 홀수 갯수 세기
        """
        if num in ODD :
            # print(num)
            cnt += 1
    if len(numArr) == 1 :
        oddCount.append(cnt)
        return
    if len(numArr) <= 3 :
        temp = str(sum(list(map(int,numArr))))
        dfs(cnt,list(temp))
    else :
        """
        ex. 길이가 5일 때
        i : 1 -> k : 2 -> [:1], [1:2], [2:]
              -> k : 3 -> [:1], [1:3], [3:]
              -> k : 4 -> [:1], [1:4], [4:]
        i : 2 -> k : 3 -> [:2], [2:3], [3:]
              -> k : 4 -> [:2], [2:4], [4:]  
        i : 3 -> k : 4 -> [:3], [3:4], [4:]
        """
        for i in range(1, len(numArr) - 1):
            for k in range(i + 1, len(numArr)) :
                first = ''.join(numArr[:i])
                second = ''.join(numArr[i:k])
                third = ''.join(numArr[k:])
                temp = int(first) + int(second) + int(third)
                dfs(cnt, list(str(temp)))


NUM = list(input().rstrip())
dfs(0,NUM)
# if len(NUM) <= 3 :
#     dfs(0,NUM)
# else :
#     # cnt = 0
#     # for num in NUM:
#     #     """
#     #     값 내의 홀수 갯수 세기
#     #     """
#     #     if num in ODD:
#     #         print(num)
#     #         cnt += 1
#     for i in range(1, len(NUM) - 1):
#         for k in range(i + 1, len(NUM)):
#             first = ''.join(NUM[:i])
#             second = ''.join(NUM[i:k])
#             third = ''.join(NUM[k:])
#             print("%s %s %s" % (first, second, third))
#             temp = int(first) + int(second) + int(third)
#             dfs(0, list(str(temp)))
# print(oddCount)
print(min(oddCount), max(oddCount), sep=" ")


# 514 예시
"""
This time :  ['5', '1', '4']
5
1
This time :  ['1', '0']
1
This time :  ['1']
1
[4]
4 4
"""
# 82019 예시
""" 
82019
This time :  ['8', '2', '0', '1', '9']
1
9
8 2 019
This time :  ['2', '9']
9
This time :  ['1', '1']
1
1
This time :  ['2']
8 20 19
This time :  ['4', '7']
7
This time :  ['1', '1']
1
1
This time :  ['2']
8 201 9
This time :  ['2', '1', '8']
1
This time :  ['1', '1']
1
1
This time :  ['2']
82 0 19
This time :  ['1', '0', '1']
1
1
This time :  ['2']
82 01 9
This time :  ['9', '2']
9
This time :  ['1', '1']
1
1
This time :  ['2']
820 1 9
This time :  ['8', '3', '0']
3
This time :  ['1', '1']
1
1
This time :  ['2']
[5, 5, 5, 4, 5, 5]
"""