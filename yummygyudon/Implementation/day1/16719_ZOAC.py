import sys
input = sys.stdin.readline

WORD = input().rstrip()
SIZE = len(WORD)
INDEXES = []
print(WORD[0:SIZE])
def dfs(startIndex,endIndex) :
    # global CHAR
    global INDEXES
    if startIndex == endIndex :
        return
    # if not strings :
    #     return
    print("확인 영역 : ", WORD[startIndex:endIndex])
    sortedWord = sorted(WORD[startIndex:endIndex])
    print("확인 영역 내 가장 작은 단어를 찾기 위해 정렬 : ", sortedWord)

    index = WORD.find(sortedWord[0],startIndex)
    INDEXES.append(index)
    INDEXES.sort()
    char = ''
    # CHAR += WORD[startIndex]
    for idx in INDEXES :
        char += WORD[idx]
    print(char)
    print()

    # # if startIndex < SIZE-1 :
    dfs(index+1,endIndex)
    dfs(startIndex, index)

dfs(0, SIZE)
#
# sortedWord = sorted(WORD)
# startIndex = WORD.index(sortedWord[0])
# print(WORD[startIndex+1:])
# dfs(startIndex, WORD[startIndex+1:])