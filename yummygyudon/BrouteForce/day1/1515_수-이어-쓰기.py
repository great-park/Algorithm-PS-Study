from sys import stdin
input = stdin.readline
NUMBERS = list(input().rstrip())
print(NUMBERS)
# result = 0
# start = 0
# overTime = 0
# for num in NUMBERS :
#     if num > start :
#         start = num
#         continue
#     if num <= start :
#         overTime += 1
# result += start
# print(result)



"""
반례 : 111111

11 차례에서 1이 한 번에 두개가 빠져야 하지만 
한 번만 세고 넘어감.
"""
# start = 0
# while len(NUMBERS) > 0 :
#     target = NUMBERS.pop(0)
#     start += 1
#     print("Target : ", target)
#     print("시작값 : ",start)
#     number = list(str(start))
#     if target in number :
#         # start += 1
#         print("같은 값 포함 : ",start)
#     else :
#         print("같은 값 포함될 때까지 while문")
#         while target not in number :
#             start += 1
#             number = list(str(start))
#             print("while문 : ",start)
#     print()
#
# print("결과 : ", start)


start = 0
while True :
    start += 1
    number = list(str(start))

    print("시작값 : ",start)
    print("남은 비교 문자열 : ", NUMBERS)
    """
    하나라도 어긋나면 종료
    -> 이번 start 값 구성 숫자가 떨어졌을 때
    -> 입력 값 구성 숫자가 떨어졌을 때
    """
    while number and NUMBERS :
        """
        위 반례를 해결하는 갱신 법
        - 속적으로 갱신하기
        """
        print("Target : ", NUMBERS[0])
        print("Target과 비교할 start 값 구성 요소 : ", number[0])
        if number[0] == NUMBERS[0] :
            # NUMBERS = NUMBERS[1:]#NUMBERS.pop(0)
            NUMBERS.pop(0)
        """
        다르던 같던 start 값의 구성 숫자를 계속 소모해야 
        len(number) > 0 조건에 걸리게 되어 다음 start값으로 넘어갈 수 있음
        """
        # number = number[1:]
        number.pop(0)
    print()
    """
    만약 입력 값 구성 숫자가 떨어져서 while문이 종료된거면 
    start 출력하고 종료
    """
    if not NUMBERS :
        print("더 이상 비교할 값 없음")
        print(start)
        break

