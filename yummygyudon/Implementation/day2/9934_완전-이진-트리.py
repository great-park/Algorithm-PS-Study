import sys
input = sys.stdin.readline

K = int(input())
SEQUENCE = list(map(int, input().split()))

"""
1. 왼쪽 자식에 안들어 갔으면 왼쪽 자식 빌딩
2. 자식이 없거나 이미 자식들에 다 들어갔으면 현재 노드 방문

왼 -> 오 -> 부모
"""
NODE = [[] for _ in range(2**K)]
LAYER = [[] for _ in range(K+1)]

"""
중앙에서부터 부모 시작하는 이진 트리 특성
"""
depth = 1
def dfs(startIndex, endIndex,depth) :

    midIndex = (startIndex+endIndex)//2
    LAYER[depth].append(SEQUENCE[midIndex])
    # print(SEQUENCE[midIndex])

    if depth >= K :
    # if abs(startIndex-endIndex) == 1 : -> startIndex와 endIndex의 차가 1이면 한개의 값밖에 없다는 것
        return
    # leftChild = SEQUENCE[(startIndex+midIndex)//2]
    # rightChild = SEQUENCE[((midIndex+1)+endIndex)//2]
    # print("자식 : %d %d"%(leftChild, rightChild))
    # NODE[midIndex].append(leftChild)
    # NODE[midIndex].append(rightChild)
    dfs(startIndex, midIndex, depth+1)
    dfs(midIndex+1, endIndex, depth+1)

    # NODE[midIndex].append(dfs(nodes[:midIndex]))
    # NODE[midIndex].append(dfs(nodes[midIndex+1:]))

dfs(0, len(SEQUENCE), 1)
# print(NODE)
# print(LAYER)
for i in range(1, K+1) :
    print(*LAYER[i])





# 본래 노드 갯수는 2^K -1 이지만 인덱스를 위해
# CONNECT_NODE = [[] for _ in range(2**K)]
# CHILDREN = [[] for _ in range(2**K)]
# PARENT = [[] for _ in range(2**K)]
# CHECK = [False] * (2**K)
#
# for i in range(len(SEQUENCE)-1) :
#     """
#     다음에 갔다는 것 -> 해당 노드의 부모 노드 or 해당 노드의 오른쪽 노드 ( 인접 노드 중에
#     """
#     # if not CHECK[SEQUENCE[i]]
#     CONNECT_NODE[SEQUENCE[i]].append(SEQUENCE[i+1])
#     CONNECT_NODE[SEQUENCE[i+1]].append(SEQUENCE[i])
#
#
# number = SEQUENCE[0]
# for _ in range(2**K-1) :
#     CHECK[number] = True
#     print(CHECK)
#     if not CHECK[CONNECT_NODE[number][0]] :
#         CHILDREN[CONNECT_NODE[number][0]].append(number)
#         PARENT[number].append(CONNECT_NODE[number][0])
#         number = CONNECT_NODE[number][0]
#         continue
#     if not CHECK[CONNECT_NODE[number][-1]] :
#         PARENT[CONNECT_NODE[number][-1]].append(number)
#         number = CONNECT_NODE[number][-1]
#         continue
#     if CHECK[CONNECT_NODE[number][0]] and not CHECK[CONNECT_NODE[number][-1]] :
#         CHILDREN[PARENT[number][0]].append(number)
#         PARENT[PARENT[number][0]].append(CONNECT_NODE[number][-1])
#         number = CONNECT_NODE[number][-1]
#
# print("CONNECT : ",CONNECT_NODE)
# print("PARENT : ",PARENT)
# print("CHILDREN : ",CHILDREN)
#     # if len(CONNECT_NODE[number]) == 1 :
#     #     CHILDREN[CONNECT_NODE[number][0]].append(number)
#     #     number = CONNECT_NODE[number][0]
#     #     continue
#     # for nearNode in NODE[number] :
#     #     if not CHECK[nearNode] :
#     #         number = nearNode
#     # if not CHECK[visitNode] :


# def dfs(parentNode, depth) :
#     global number
#     if len(NODE[])
