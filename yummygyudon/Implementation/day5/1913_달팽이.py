### My Part ###
import sys
input = sys.stdin.readline

N = int(input())
TARGET_NUM = int(input())

BOARD = [[0]*N for _ in range(N)]
END = N*N

# down, right, up, left = False, False, False, False
NEXT_DIRECTION = dict()
# NEXT_DIRECTION['down'] = 'right'
# NEXT_DIRECTION['right'] = 'up'
# NEXT_DIRECTION['up'] = 'left'
# NEXT_DIRECTION['left'] = 'down'
NEXT_DIRECTION[0] = 1
NEXT_DIRECTION[1] = 2
NEXT_DIRECTION[2] = 3
NEXT_DIRECTION[3] = 0

def move(y,x, num) :
    BOARD[y][x] = num

idx = 0
d = [[1, 0],[0, 1],[-1, 0],[0, -1]]

posY, posX = 0, 0
BOARD[posY][posX] = END
for num in range(END-1, 0, -1) :
    nextY = posY + d[idx][0]
    nextX = posX + d[idx][1]
    # print("이번에 등록할 Y 좌표", nextY)
    # print("이번에 등록할 X 좌표", nextX)
    # print()
    if not(0<=nextX<N and 0<=nextY<N) or not (BOARD[nextY][nextX] == 0) :
        idx = NEXT_DIRECTION[idx]
        nextY = posY + d[idx][0]
        nextX = posX + d[idx][1]
    move(nextY,nextX,num)
    posY = nextY
    posX = nextX

for layer in BOARD :
    print(*layer)
for i in range(N) :
    for k in range(N) :
        if BOARD[i][k] == TARGET_NUM :
            print(i+1, k+1, sep=" ")

