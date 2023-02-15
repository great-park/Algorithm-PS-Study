import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
total = 0
cost = price[0]

for i in range(N-1) :
    print("total : ", total)
    print("cost : ", cost)
    print("현재 위치 주유소 가격 비교 시작!!")

    if cost > price[i] :
        print("여기가 더 싸서 갱신")
        cost = price[i]
    total += cost*distance[i]

    print("cost : ", cost)
    print("total : ", total)
    print()
print(total)