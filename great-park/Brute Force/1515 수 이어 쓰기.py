from sys import stdin

# 1씩 증가시키면서 같아지면 다음으로 넘기기

# 이렇게 되면 뒷자리 삭제하는 경우만 처리됨
# data = list(map(int, input().rstrip()))
# result = 0
# i = 0
# while True:
#     while result % 10 != data[i]:
#         result += 1
#     i += 1
#     if i == len(data):
#         break
# print(result)

# 숫자말고 문자열로 처리
data = list(input().rstrip())  # 234092
i = 0
while data:
    i += 1

    # '2'
    result = str(i)  # '2', '3', .. '19', '20'

    for k in range(len(result)):  # 0
        if result[k] == data[0]:  # '2' vs  '2'
            data = data[1:]  # 맨 앞 자르기 -> 34092
        if not data:
            print(i)
            break
