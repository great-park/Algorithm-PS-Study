import sys
input = sys.stdin.readline
"""
확장자 별로 몇개씩 있는지
확장가 사전순 정렬
"""
N = int(input())

EXTENSION = dict()

for _ in range(N) :
    name, extension = input().rstrip().split(".")
    if extension not in EXTENSION :
        EXTENSION[extension] = 1
    else :
        EXTENSION[extension] = EXTENSION.get(extension) + 1

print(EXTENSION)
KEYS = list(EXTENSION.keys())
KEYS.sort()
for key in KEYS :
    print(key, EXTENSION[key], sep=" ", end="\n")