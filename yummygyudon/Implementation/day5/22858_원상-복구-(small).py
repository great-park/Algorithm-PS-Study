import sys
input = sys.stdin.readline

N, SHUFFLE = map(int, input().split())

RESULT = [0] + list(map(int, input().split()))
D = [0] + list(map(int,input().split()))

"""
역방향으로 보내주기
ex. 
D = [4, 3, 1, 2, 5]

P[i] = P[D[i]] 방식으로 셔플됨
-> 돌려놓으려면 P[D[i]] = P[i] 로 실행
"""
for _ in range(SHUFFLE) :
    temp = [0]*(N+1)
    for i in range(1,N+1) :
        # print("P의 D[i] 번째 -> P의 i 번째 :: %d 번째 -> %d 번째"%(D[i], i))
        temp[D[i]] = RESULT[i]
    RESULT = temp
print(*RESULT[1:])
"""
P : [4, 3, 1, 2, 5]
⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆

P의 D[i] 번째 -> P의 i 번째 :: 4 번째 -> 1 번째
P의 D[i] 번째 -> P의 i 번째 :: 3 번째 -> 2 번째
P의 D[i] 번째 -> P의 i 번째 :: 1 번째 -> 3 번째
P의 D[i] 번째 -> P의 i 번째 :: 2 번째 -> 4 번째
P의 D[i] 번째 -> P의 i 번째 :: 5 번째 -> 5 번째

P : [3, 5, 1, 4, 2]
⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆

P의 D[i] 번째 -> P의 i 번째 :: 4 번째 -> 1 번째
P의 D[i] 번째 -> P의 i 번째 :: 3 번째 -> 2 번째
P의 D[i] 번째 -> P의 i 번째 :: 1 번째 -> 3 번째
P의 D[i] 번째 -> P의 i 번째 :: 2 번째 -> 4 번째
P의 D[i] 번째 -> P의 i 번째 :: 5 번째 -> 5 번째

P의 i 번째 자리에 P의 D[i]번째 숫자로 바꿔주기
- P의 1 번째 자리 <- P의 4번째 숫자
- P의 2 번째 자리 <- P의 3번째 숫자
- P의 3 번째 자리 <- P의 1번째 숫자
- P의 4 번째 자리 <- P의 2번째 숫자
- P의 5 번째 자리 <- P의 5번째 숫자
P : [1, 4, 5, 3, 2]
"""
