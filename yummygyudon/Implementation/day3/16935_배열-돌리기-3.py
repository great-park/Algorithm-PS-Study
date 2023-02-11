import sys

input = sys.stdin.readline

N, M, TIME = map(int, input().split())
MATRIX = [list(map(int, input().split())) for _ in range(N)]
COMMANDS = list(map(int, input().split()))


# print(MATRIX)


def function(commandNum, matrix):
    if commandNum == 1:
        for i in range(N // 2):  # 0,1,2
            matrix[i], matrix[(N - 1) - i] = matrix[(N - 1) - i], matrix[i]
        return matrix

    if commandNum == 2:
        for i in range(N):
            for k in range(M // 2):
                matrix[i][k], matrix[i][(M - 1) - k] = matrix[i][(M - 1) - k], matrix[i][k]
        return matrix

    """
    3번과 4번은 가로 세로 길이가 서로 바뀌기 때문에 갱신 필요
    """
    if commandNum == 3:
        """
        가로 세로 바꾼 규격 생성

        -> 왼쪽에서의 값을 이번 자리로 가져옴
        """
        tmp = [[0] * N for _ in range(M)]
        for i in range(M):
            for k in range(N):
                # (0,1) = (1,0
                tmp[i][k] = matrix[(N - 1) - k][i]

        return tmp

    if commandNum == 4:
        """
        -> 오른쪽에서의 값을 이번자리로 가져옴
        """
        tmp = [[0] * N for _ in range(M)]
        for i in range(M):
            for k in range(N):
                # (0,1) = (1,0
                tmp[i][k] = matrix[k][(M - 1) - i]
        return tmp

    if commandNum == 5:
        tmp = [[0] * M for _ in range(N)]
        """
        1사분면 -> 2사분면
        """
        for i in range(N // 2):  # 상단
            for k in range(M // 2):  # 좌측
                tmp[i][M // 2 + k] = matrix[i][k]
        """
        2사분면 -> 3사분면
        """
        for i in range(N // 2):  # 상단
            for k in range(M // 2, M):  # 우측
                """ 절반 + i """
                tmp[N // 2 + i][k] = matrix[i][k]
        """
        3사분면 -> 4사분면
        """
        for i in range(N // 2, N):  # 하단
            for k in range(M // 2, M):  # 우측
                tmp[i][k - M // 2] = matrix[i][k]
        """
        4사분면 -> 1사분면
        """
        for i in range(N // 2, N):  # 하단
            for k in range(M // 2):  # 좌측
                tmp[i - N // 2][k] = matrix[i][k]
        return tmp

    if commandNum == 6:
        tmp = [[0] * M for _ in range(N)]
        """
        1사분면 -> 4사분면
        """
        for i in range(N // 2):  # 상단
            for k in range(M // 2):  # 좌측
                # 중간  + i 행
                tmp[N // 2 + i][k] = matrix[i][k]
        """
        4사분면 -> 3사분면
        """
        for i in range(N // 2, N):  # 하단
            for k in range(M // 2):  # 좌측
                # 아래 중간 + k 열
                tmp[i][M // 2 + k] = matrix[i][k]
        """
        3사분면 -> 2사분면
        """
        for i in range(N // 2, N):  # 하단
            for k in range(M // 2, M):  # 우측
                tmp[i - N // 2][k] = matrix[i][k]
        """
        2사분면 -> 1사분면
        """
        for i in range(N // 2):  # 상단
            for k in range(M // 2, M):  # 우측
                tmp[i][k - M // 2] = matrix[i][k]
        return tmp


for i in range(TIME):
    MATRIX = function(COMMANDS[i], MATRIX)
    if COMMANDS[i] in [3, 4]:
        N, M = M, N
for row in MATRIX:
    print(*row)