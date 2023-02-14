import sys
input = sys.stdin.readline
import math
K = int(input())
# time = 1
# number = 4
# while True :
#     if time == K :
#         print(number)
#         break
#     number +=1
#     tmp = str(number)
#     if '4' in tmp or '7' in tmp :
#         if
#         time += 1

"""
그놈의 첫째 자리는 1인것때문에 2의 제곱만큼 나누어 떨어질 때마다 한 자리 씩 늘어나는 바람에
인덱싱이 힘들어서 bin 써버렸습니다.

처음엔 앞에서부터 각 자릿수 제곱만큼
 (K -= K에 2로 나눈값 ** 몫)을 해가면서 발생하는 나머지를 인덱스로 사용하려 했으나
2진수 특성상 제곱번째마다 한 자리씩 늘어나는 바람에 힘들어졌습니다.
"""
DEFAULT = ['4','7']


""" 
1부터 계산 X -> 1씩 큰 값의 이진수 값으로 인덱스 구해야함
2번째 까지는 7인 것 처럼 2자리가 되기 가장 마지막 값
(만약 해당 번째 숫자의 값을 그대로 이진수로 변환해서 사용하면 1번째일 때, slicing하면 아무값도 없음)

** 자릿수가 동일한 범위들로 만들 수 있음 **

1 : bin(2) -> 2의 2진수 -> 10 -> 0
2 : bin(3) -> 3의 2진수 -> 11 -> 1

3 : bin(4) -> 4의 2진수 -> 100 -> 00
4 : bin(5) -> 5의 2진수 -> 101 -> 01
5 : bin(6) -> 6의 2진수 -> 110 -> 10
6 : bin(7) -> 7의 2진수 -> 111 -> 11

( 0 ~ 1 : 1자리 : -1번째부터 0번째 / 2 ~ 3 : 2자리 : 1번째부터 2번째 / 
  4 ~ 7 : 3자리 : 3번째부터 6번째 / 8 ~ 15 : 4자리 : 7번째부터 14번째 / 16 ~ 31 : 5자리 : 15번째부터 30번째 / ... )
"""
BIN = bin(K+1)
""" 0b 부분 빼기 """
INDEXES = list(BIN[3:])

print(INDEXES)
answer = ''
for idx in INDEXES :
    answer += DEFAULT[int(idx)]

print(answer)
"""
원하는 번째 수가 
2의 몇승 이하인지 확인
"""
# tmp = 0
# time = 0
# while True :
#     tmp += int(math.pow(2, time))
#     # print(tmp)
#     if K-1 <= tmp :
#         break
#     time+=1
#
# """
# time : 정답의 자릿수
# """
# answer = 0
# print(K%2)
# print(K//2)
# print(bin(K))

# 6번째 일
#
# print(time)
# print("번째의 2진",format(K, 'b'))
# for i in range(time, 0, -1) :K-(2**i))
#     print("K : ",K)
#     print("해당 자릿수의 경의 수 : ", 2**i)
#     print("해당 자릿수에 올  숫자의 인덱스 : ", ( % 2)
#     answer += DEFAULT[K%2] * (10**(i-1))
#     K -= 2 ** i  # -4
#     print(answer)
#     print()


# for i in range(1, time+1) :
#     print("K : ", K)
#     print("해당 자릿수에 올  숫자의 인덱스 : ", K % 2)
#     answer += DEFAULT[K % 2] * (10 ** (i))
#     print("answer", answer)
#     K = (K * (K // 2))
#
# answer += DEFAULT[K%2]
# print(answer)