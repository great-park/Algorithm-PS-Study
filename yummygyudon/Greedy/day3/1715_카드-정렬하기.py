import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
CARDS = deque()
# for _ in range(N) :
#     CARDS.append(int(input()))
"""
작은 것들끼리 먼저 뭉쳐서 합치는 것이 관건

ex. 20, 20, 20, 30
(20+20), 20, 30 -> (20+20), (40+20), 30 -> (20+20), (40+20), (60+30) = 190
(20+20), 20, 30 -> 20, 30, (20+20) -> (20+30), 40 -> 50+ (50+40) = 140

위와 같은 반례 때문에 계속해서 정렬해주거나
앞에 지속적으로 작은값이 와야함
"""
# CARDS.sort()
#
# COUNT = [0]*N
# COUNT[0] = CARDS[0]
# for i in range(1,len(CARDS)) :
#     COUNT[i] = CARDS[i]+COUNT[i-1]
# print(sum(COUNT[1:]))

"""
deque는 원형 큐로 rotate도 가능하고
.reverse로 뒤집는 것도 가능하지만

sort가 안된다.

-> Priority Queue (우선순위 큐 제공) : 내부에서 heap을 결국 쓰기 때문에 heapq 쓰는게 효율적이라고 합니다.
Priority Queue : 568ms <<< Heap Queue : 3988ms
"""
from queue import PriorityQueue
q = PriorityQueue(maxsize=N)

for _ in range(N) :
    q.put(int(input()))

result = 0

"""
while len(q) >= 2로 해도 되지만
연산 자체가 총 N-1번의 연산이 일어나기 때문에
(N-1)번만 연산한다.
"""
for _ in range(N-1) :
    c1 = q.get()
    c2 = q.get()
    print(c1, c2)
    x1 = c1 + c2
    result += x1
    q.put(x1)
print(result)