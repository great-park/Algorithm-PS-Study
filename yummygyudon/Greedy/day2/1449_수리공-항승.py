import sys
input = sys.stdin.readline

N, L = map(int, input().split())
HOLES = list(map(int, input().split()))
HOLES.sort()

tapeEnd = 0
usedTapeQuantity = 0
for hole in HOLES :
    """
    구멍 크기에 테이프 길이를 더해서
    테이프 길이가 끝날 때까지 중간에 있는 구멍까지 한 번에 커버 
    """
    if hole <= tapeEnd :
        continue
    else :
        tapeEnd = hole + L - 1
        usedTapeQuantity+=1
print(usedTapeQuantity)