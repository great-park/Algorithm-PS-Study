### My Part ###
import sys
input = sys.stdin.readline

"""
1차 시도 : 87%에서 틀렸다고 하네요... (예제는 모두 통과)
- 자식 노드 리스트가 빈 리스트일 경우 -> 리프 노드로 취급
- 처음 시작할 때의 잎 노트 개수 세기
- 지울 때도 DFS로 빈 자식 노드 리스트를 가질 때(리프노드) 하나씩 지워진 잎노드(DELETED_LEAF) +1
"""
""" ⬇ 1차 시도 코드 ⬇ """
# N = int(input())
# CHILD = [[] for _ in range(N)]
# PARENT = list(map(int, input().split()))
# DEL = int(input())

"""(자신의 번호, 부모 노드 번호) 구조"""
# for idx, parentNum in enumerate(PARENT,start=0) :
#     if (parentNum == -1) :
#         """
#         부모 -1로 입력 받을 때 : 자신이 루트라는 의미
#         - 따로 해당 idx 등록할 노드가 없음
#         """
#         continue
#     CHILD[parentNum].append(idx)

# def countDeleteLeaf(node) : # 3 | 7, 6
#     global DELETED_LEAF
#     global CHILD
#     children = CHILD[node] # [6,7] | [] []
#     if not children :
#         del (CHILD[node]) # 7 6
#         return
#     length = len(CHILD) # 2
#     for i in range(length) : # 2번
#         countDeleteLeaf(CHILD[node].pop()) # 6, 7







# REMAINED_LEAF = 0
# DELETED_LEAF = 0

"""처음 시작할 때의 잎 노트 개수 세기"""
# for children in CHILD :
#     if not children :
#         REMAINED_LEAF += 1

"""삭제 노드 기준으로 삭제될 잎 노드 개수 세기"""
# countDeleteLeaf(DEL)

""" 남아있을 잎 노드 개수 = (기존 잎 노드 - 삭제될 잎 노드) """
# print(REMAINED_LEAF - DELETED_LEAF)


# for i in range(N) :
#     for child in CHILD[i] :
#         if DEL == child :
#             countDeleteLeaf(child)
#             del(CHILD[])


""" 
2차 시도  

"""

N = int(input())
CHILD = [[] for _ in range(N)]
PARENT = list(map(int, input().split()))
DEL = int(input())
ROOT = 0
REMOVED = -1e9

for idx, parentNum in enumerate(PARENT,start=0) :
    if (parentNum == -1) :
        """
        부모 -1로 입력 받을 때 : 자신이 루트라는 의미
        - 따로 해당 idx 등록할 노드가 없음
        """
        ROOT = idx
        continue
    CHILD[parentNum].append(idx)

"""
부모로서 등록되어있는 PARENT 에서 해당 노드 삭제 처리
CHILD에 자신의 자식으로 등록되어 있는 노드들도 DFS로 삭제 처리 메서드 실행
"""
def removeChildrenNodes(removeNode) :
    PARENT[removeNode] = REMOVED
    for i in range(len(CHILD[removeNode])) :
        removeChildrenNodes(CHILD[removeNode][i])


removeChildrenNodes(DEL)

COUNT = 0

for i in range(N) :
    """
    자신이 삭제되지 않았으며
    어떤 노드도 자신을 부모로 같지 않을 경우
    == "리프 노드"
    """
    if not PARENT[i] == REMOVED and i not in PARENT:
        COUNT += 1

print(COUNT)
