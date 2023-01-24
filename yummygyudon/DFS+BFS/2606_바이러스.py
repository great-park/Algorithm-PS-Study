import sys
input = sys.stdin.readline
N = int(input())
M = int(input())


"""
UnionFind 방식
"""
def find_parent(Parent, x) :
    if Parent[x] != x :
        Parent[x] = find_parent(Parent,Parent[x])
    return Parent[x]

def union_parent(Parent, a, b) :
    a = find_parent(Parent, a)
    b = find_parent(Parent, b)
    if a < b :
        Parent[b] = a
    else :
        Parent[a] = b

route = [list(map(int, input().split())) for _ in range(M)]

Parent = [0] * (N+1)

# 각자의 index에 맞춰 자기 자신 등록
for i in range(1,N+1) :
    Parent[i] = i


for _ in range(2) :
    for x,y in route :
    # x, y = map(int, input().split())
        union_parent(Parent,x, y)
cnt = 0
for i in range(2,len(Parent)) :
    if Parent[i] == 1 :
        cnt += 1
print(cnt)