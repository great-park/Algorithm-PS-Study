import sys
input = sys.stdin.readline

N = int(input())
"""
0~9이기 때문에 
A ~ J 까지만 알파벳이 나올 수 있음

chr(65) : A -> str type임
0 : A
"""
ALP_VAL_MAP = dict()
for _ in range(N) :
    word = list(input().rstrip())
    size = len(word)-1
    for i in range(len(word)) :
        if word[i] not in ALP_VAL_MAP.keys() :
            ALP_VAL_MAP[word[i]] = 1 * (10 ** (size - i))
        else :
            ALP_VAL_MAP[word[i]] = ALP_VAL_MAP.get(word[i]) + 1 * (10 ** (size - i))
# print(ALP_VAL_MAP)
"""
{'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
"""
ALP_VAL_MAP = list(ALP_VAL_MAP.items())
# print(ALP_VAL_MAP)
ALP_VAL_MAP.sort(key=lambda x : x[1], reverse=True)
# print(ALP_VAL_MAP)
"""
A = 10000
B = 1
C = 1000 + 10
D = 100
E = 10
F = 1
G = 100

⬇ (정렬) ⬇ 
A = 10000 : 9
C = 1000 + 10 : 8
D = 100 & G = 100 : 7 or 6
E = 10 : 5
B = 1 & F = 1 : 4 or 3

같은 가치를 가진 서로 다른 알파벳들은 서로 가능한 값 범위내에서 바뀌어도 상관없음
(D&G / B&F)
"""
result = 0
MAX = 9
for alp, value in ALP_VAL_MAP :
    result += (MAX * value)
    MAX -= 1
print(result)