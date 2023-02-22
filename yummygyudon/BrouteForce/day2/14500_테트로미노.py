"""
FEAT($BrouteForce) : 14500 테트로미노 문제 완료
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
BOARD = []

for _ in range(N) :
    BOARD.append(list(map(int, input().split())))
"""
왼쪽 끝 상단부터 시작 가정

"하나"만 놓는 거임
"""
"""
# 총 19가지
"""
METRICS_CASE=[
        # ㅣ 자 (2가지)
        [(0,0),(0,1),(0,2),(0,3)], # ㅡ
        [(0,0),(1,0),(2,0),(3,0)], # ㅣ

        # ㅁ 자 (1가지)
        [(0,0),(1,0),(0,1),(1,1)], # ㅁ
        
        # ㄱ 자 돌리기 & 대칭 ( 8가지 )
        [(0,0),(1,0),(2,0),(2,1)], # ⎣
        [(0,1),(1,1),(2,1),(2,0)], # ⌋
        
        [(0,0),(0,1),(1,1),(2,1)], # ⌉
        [(0,0),(0,1),(1,0),(2,0)], # ⎡
        
        [(1,0),(1,1),(1,2),(0,2)], 
        [(0,0),(0,1),(0,2),(1,2)],   
        
        [(1,0),(0,0),(0,1),(0,2)],
        [(0,0),(1,0),(1,1),(1,2)], 
        
        # Z 자 돌리기 & 대칭 ( 4가지 )
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        
        [(1,0),(1,1),(0,1),(0,2)],
        [(0,0),(0,1),(1,1),(1,2)],
        
        # ㅜ 자 돌리기 & 대칭 ( 4가지 )
        [(0,1),(1,0),(1,1),(1,2)], # ㅗ
        [(0,0),(0,1),(0,2),(1,1)], # ㅜ

        [(0,0),(1,0),(2,0),(1,1)], # ㅏ
        [(1,0),(0,1),(1,1),(2,1)] ] # ㅓ

def checkIsPossible(y,x) :
    if 0<=y<N and 0<=x<M :
        return True
    else:
        return False

MAX = -1e9
def checkBlock(y,x) :
    global MAX
    for case in METRICS_CASE :
        score = 0
        for dy, dx in case :
            if not checkIsPossible(y+dy, x+dx) :
                score = 0
                break
            score += BOARD[y+dy][x+dx]
        MAX = max(MAX, score)

for i in range(N) :
    for k in range(M) :
        checkBlock(i,k)
print(MAX)
