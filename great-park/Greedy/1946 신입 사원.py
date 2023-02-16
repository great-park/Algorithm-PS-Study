from sys import stdin
input = stdin.readline
T = int(input())

for i in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort()  # 서류 성적순

  """
  1 4
  2 3
  3 2
  4 1
  5 5
  """
    result = 1
    # 면접 점수 평가
    min = data[0][1]
    for k in range(1, N):
        if data[k][1] < min:
            min = data[k][1]
            result += 1
    print(result)
