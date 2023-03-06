# from sys import stdin
# input = stdin.readline
# N = int(input())
# move = list(input().rstrip())
# check = [0]*(2*N+2)
# position = N+1
# check[position] = 1

# for i, go in enumerate(move):
#     go = move[i]
#     if go == 'E':
#         position += 1
#         check[position] = 1
#     elif go == 'W':
#         position -= 1
#         check[position] = 1
# size = 0
# for value in check:
#     if value == 1:
#         size += 1

# result = N // size

# if N % size == 0:
#     print(result)
# else:
#     print(result + 1)
from sys import stdin

n = int(stdin.readline())
graph = stdin.readline().rstrip()
print(graph.count('EW'))
