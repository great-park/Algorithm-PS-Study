import sys
input = sys.stdin.readline

"""
1. 비어있는 칸 중 "좋아하는 학생"이 "인접한 칸에" 가장 많은 칸으로
2. 1번 조건의 칸이 여러 개 -> 인접한 칸에 비어있는 칸이 가장 많은 칸으로
3. 비어있는 칸까지 여러개라면 행 번호가 가장 작은 칸으로
4. 행 번호가 가장 작은 칸도 여러개면 열 번호가 가장 작은 칸으로
"""

"""
좋아하는 학생 수 0 = 0
좋아하는 학생 수 1 = 1
좋아하는 학생 수 2 = 10
좋아하는 학생 수 3 = 100
좋아하는 학생 수 4 = 1000
"""
N = int(input())
MAP = [[0]*N for _ in range(N)]
LOVE = dict()
for _ in range(N*N) :
    values = list(map(int, input().split()))
    LOVE[values[0]] = values[1:]

print(LOVE)
print(list(LOVE.keys()))

# 상 우 하 좌
d = [[-1,0],[0, 1],[1,0],[0,-1]]

"""
"""
def firstMapping(studentNum) :
    friendsPos = []
    for friend in LOVE[studentNum] :
        for i in range(N) :
            for k in range(N) :
                """
                자리 배치 중 좋아하는 학생이 있을 경우
                좋아하는 학생 주변에 들어갈 수 있는 자리가 있는지 체크
                -> 주변에 들어갈 곳이 있으면 삽입
                """
                if friend == MAP[i][k] :
                    for ablePos in checkAblePos(i,k) :
                        friendsPos.append(ablePos)

    if not friendsPos :
        print("좋아하는 친구가 없다")
        return checkBestBlank()
    print("좋아하는 친구 발견")
    """
    가능한 칸들 중 주변에 가장 좋아하는 친구가 많은 칸
    """
    return findNearFriend(studentNum, friendsPos)
def checkAblePos(y,x) :
    ablePos = []
    for i in range(4) :
        ny = y + d[i][0]
        nx = x + d[i][1]
        if 0<=ny<N and 0<=nx<N and MAP[ny][nx] == 0 :
            ablePos.append([ny,nx])
    return ablePos
"""
인접칸 중 비어 있는 칸
"""
def checkBestBlank() :
    print("비어있는 칸 찾기")
    blanks = []
    for i in range(N) :
        for k in range(N) :
            if MAP[i][k] == 0 :
                cnt = 0
                for j in range(4) :
                    ny = i+d[j][0]
                    nx = k+d[j][1]
                    if 0<=ny<N and 0<=nx<N and MAP[ny][nx] == 0 :
                        cnt+=1
                blanks.append( [cnt,i,k] )
    blanks.sort(key=lambda pos : (-pos[0], pos[1], pos[2]))
    print(blanks)
    return [blanks[0][1], blanks[0][2]]
"""
"""
def findNearFriend(studentNum, ablePositions : list) :
    findResult = []
    for ablePos in ablePositions :
        near_cnt = 0
        blank_cnt = 0
        for i in range(4):
            ny = ablePos[0] + d[i][0]
            nx = ablePos[1] + d[i][1]
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] in LOVE[studentNum]:
                near_cnt += 1
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] == 0:
                blank_cnt += 1
        findResult.append([near_cnt,blank_cnt, ablePos[0], ablePos[1]])
    findResult.sort(key=lambda pos : (-pos[0],-pos[1], pos[2], pos[3]))
    print(findResult)
    return [findResult[0][2], findResult[0][3]]

for studentNum in list(LOVE.keys()) :
    print("자리 찾을 학생 번호 : ",studentNum)
    y, x = firstMapping(studentNum)
    MAP[y][x] = studentNum
    print(MAP)

SCORE = dict()
SCORE[0] = 0
SCORE[1] = 1
SCORE[2] = 10
SCORE[3] = 100
SCORE[4] = 1000
SURVEY = 0
for i in range(N) :
    for k in range(N):
        checkStudent = MAP[i][k]
        print("만족도 조사 대상 : ", checkStudent)
        cnt = 0
        for j in range(4):
            ny = i + d[j][0]
            nx = k + d[j][1]
            if 0 <= ny < N and 0 <= nx < N and MAP[ny][nx] in LOVE[checkStudent]:
                cnt += 1
        print("만족도 : ",cnt)
        SURVEY += SCORE[cnt]
print("만족도 총 합 : ", SURVEY)

