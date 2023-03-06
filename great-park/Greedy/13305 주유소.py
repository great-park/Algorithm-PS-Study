from sys import stdin
input = stdin.readline
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# min_need = []  # [10, 6, 4]
# for i in range(N-1):
#     min_need.append(distance[i] * price[i])
# final_cost = min_need[0]

# for i in range(1, N-1):
#     # 이전 가격으로 현재 거리 지나기 vs 현재 가격으로 현재 거리 지나기
#     min_cost = 1e9
#     for k in range(i):
#         cost1 = distance[i] * price[k]
#         cost2 = distance[i] * price[i]

#         min_cost = cost1 if cost1 < cost2 else cost2
#     final_cost += min_cost
# print(final_cost)

"""
    싼 값을 만나면 미리 기름을 사는것.
    """
final_cost = 0
min_cost = price[0]

for i in range(N-1):
    min_cost = price[i] if price[i] < min_cost else min_cost
    final_cost += distance[i] * min_cost
print(final_cost)
