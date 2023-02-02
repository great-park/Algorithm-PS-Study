"""

"""

import sys
input = sys.stdin.readline

C, N = map(int,input().split())

TABLE = [[0,0] for _ in range(N)]
for i in range(N) :
    cost, customer = map(int, input().split())
    TABLE[i][0] = cost
    TABLE[i][1] = customer
TABLE.sort(key= lambda x : x[1], reverse=True)
"""
" 적어도 C명 늘이기 위해 " : 해당 목표까지 딱 맞춰서 최소 금액이 아님
-> 목표 인원보다 오버되어 고객이 오더라도 최소 비용을 구하는 것이 관건
-> 한 번에 오버될 수 있는 최대 인원만큼 비용계산 칸을 늘려야함
"""
OVERABLE = TABLE[0][1] ## 가장 높은 고객 증가치 기준으로 내림차순 정렬 했기 때문에 첫번째 행의 고객 증가치 == 최대로 오버될 수 있는 증가치
CUSTOMER_PER_COST = [1e9] * (C + OVERABLE)
CUSTOMER_PER_COST[0] = 0
print(TABLE)


# for i in range(C+1) : # 0,1,2,3,4,5,6,7,8,9,10
#     print("****** %d ******"%i)
#     for cost, customer in TABLE:  # 1, 3
#         if i+customer <= C :
#             CUSTOMER_PER_COST[i+customer] = min(CUSTOMER_PER_COST[i+customer], cost + CUSTOMER_PER_COST[i])
#         print(CUSTOMER_PER_COST)
#     print(f"*****************")

# for cost, customer in TABLE :
#     print("****** %d 원 ******" % cost)
#     for i in range(C, 0, -1):
#         if i-customer >= 0 :
#             CUSTOMER_PER_COST[i-customer] = min(CUSTOMER_PER_COST[i-customer], cost + CUSTOMER_PER_COST[i])
#         print(CUSTOMER_PER_COST)

for cost, customer in TABLE:
    for i in range(customer, C+OVERABLE):
        CUSTOMER_PER_COST[i] = min(CUSTOMER_PER_COST[i], cost + CUSTOMER_PER_COST[i-customer])
print(CUSTOMER_PER_COST)
"""
목표 인원부터 이후까지의 최소 비용 추출 -> 목표인원이 넘어갔음에도 목표인원 위치의 DP값보다 작으면 
넘어갔더라도 해당 오버 인원 수 위치의 DP값이 출력되어야 함.
"""
print(min(CUSTOMER_PER_COST[C:]))


# for cost, customer in TABLE:
#     print("****** %d 원 ******" % cost)
#     for i in range(1, C+1):
#         # if i - customer >= 0:
#         if i % customer == 0 :
#             CUSTOMER_PER_COST[i] = min(CUSTOMER_PER_COST[i], cost + CUSTOMER_PER_COST[i-customer])
#         print(CUSTOMER_PER_COST)
# print(CUSTOMER_PER_COST)
# print(CUSTOMER_PER_COST[C])