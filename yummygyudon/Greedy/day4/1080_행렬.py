import sys
input = sys.stdin.readline

h, w = map(int,input().split())
arr_A = []
arr_B = []
for _ in range(h) :
    arr_A.append(list(map(int,list(input()))))
for _ in range(h) :
    arr_B.append(list(map(int,list(input()))))
def change(x, y) :
    for i in range(x, x+3) :
        for j in range(y, y+3) :
            arr_A[i][j] = 1-arr_A[i][j]
cnt = 0
for move_d in range(h-3+1) :
    for move_r in range(w-3+1):
        if arr_A[move_d][move_r] != arr_B[move_d][move_r] :
            cnt+=1
            change(move_d, move_r)
for i in range(h) :
    for j in range(w):
        if arr_A[i][j] != arr_B[i][j] :
            cnt= -1
print(cnt)