from sys import stdin
input = stdin.readline

# 음수는 최대한 묶어서 +로 만들기, 홀수개라서 남고 0이 있으면 서로 곱하기
# 묶을 때 최대한 큰 수끼리 묶기

N = int(input())
plus = []
minus = []
zero = []
one = []  # 1끼리는 묶으면 손해

for i in range(N):
    value = int(input())
    if value > 1:
        plus.append(value)
    elif value == 0:
        zero.append(value)
    elif value == 1:
        one.append(value)
    else:
        minus.append(value)

plus.sort(reverse=True)
minus.sort()
plus_size = len(plus)
minus_size = len(minus)
ans = 0

if minus_size % 2 == 0:
    for i in range(0, minus_size, 2):
        ans += minus[i]*minus[i+1]
else:
    for i in range(1, minus_size, 2):
        ans += minus[i]*minus[i+1]

    # 0있으면 곱해서 안 더해도 됨, 0없으면 더해야 함
    if len(zero) == 0:
        ans += minus[0]

if plus_size % 2 == 0:
    for i in range(0, plus_size, 2):
        ans += plus[i]*plus[i+1]
else:
    for i in range(1, plus_size, 2):
        ans += plus[i]*plus[i+1]
    ans += plus[0]
print(ans+sum(one))
