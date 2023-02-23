import sys
input = sys.stdin.readline

H, W = map(int, input().split())
MATRIX_A = []
MATRIX_B = []
for _ in range(H) :
    MATRIX_A.append(list(map(int, input().rstrip())))
for _ in range(H) :
    MATRIX_B.append(list(map(int, input().rstrip())))
def change(x, y) :
    for i in range(x, x+3) :
        for k in range(y, y+3) :
            """
            1 - 1 : 0
            1 - 0 : 1
            """
            # MATRIX_A[i][k] = 1 - MATRIX_A[i][k]
            if MATRIX_A[i][k] == 0 :
                MATRIX_A[i][k] = 1
            elif MATRIX_A[i][k] == 1 :
                MATRIX_A[i][k] = 0

"""
range에 음수가 들어갈 경우
알아서 for문을 돌지 않음
-> 딱 길이가 3 이상일 때만 for문 작용
-> 3 x 2더라도 2인 부분에서 for문이 안돌기 때문에 skip 됨
"""
"""
틀린걸 발견할 때마다 
해당 지점부터 3x3영역이 존재한다면 지점으로부터 3x3 영역 뒤집어 버리기
"""
COUNT = 0
for move_d in range(H - 3 + 1) :
    for move_r in range(W - 3 + 1):
        if MATRIX_A[move_d][move_r] != MATRIX_B[move_d][move_r] :
            change(move_d, move_r)
            COUNT += 1
"""
뒤집는 처리 이후에도
틀린 게 있으면 불가능하다는 것 -> -1로 바꾸기
"""
for i in range(H) :
    for k in range(W):
        if MATRIX_A[i][k] != MATRIX_B[i][k] :
            COUNT = -1
            break
print(COUNT)

# for i in range(-2) :
#     print("음수여도 출력")