n = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

m = price[0] # 처음에는 가격이 얼마든간에 주유를 하고 시작
result = 0

# 처음 기름가격보다 그다음 기름가격이 싸다면, 미리 주유할 필요 없으므로
# 딱 처음에 이동할 거리만큼만 주유하고 그 다음 주유소에서 주유한다. 이 과정을 계속 반복하게 된다.
for i in range(0, n-1):
    if price[i] < m: # 지금 가격이 뒤에 가격보다 싸면 일단 기름 넣고 감
        m = price[i]
    result += m * roads[i] # 가격 * 거리만큼 result에 저장

print(result)