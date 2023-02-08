### My Part ###
import sys
import string
input = sys.stdin.readline


N = int(input())
""" 시도 1 : 틀렸습니다 (예제는 통과 - 질문 추가 반례도 통과) """
# SMART_KEY = set()
# """
# - 왼쪽 -> 오른쪽
# 1. 첫 글자
# 2. 왼쪽부터 차례대로 알파벳 -> 안된 것 있으면 단축키로
# 3. 어떤 것도 단축키가 안되면 그냥 놔두기
# """
# INDEXES = []
# WORDS = []
#
# for _ in range(N) :
#     WORD = input().rstrip()
#     done = False
#     if WORD[0] not in SMART_KEY and not done:
#         WORDS.append(WORD)
#         INDEXES.append(0)
#         SMART_KEY.add(WORD[0].upper())
#         SMART_KEY.add(WORD[0].lower())
#         done = True
#     else :
#         wordList = list(WORD.split())
#         for word in wordList :
#             if word[0] not in SMART_KEY and not done :
#                 WORDS.append(" ".join(wordList))
#                 INDEXES.append(WORD.find(word[0]))
#                 SMART_KEY.add(word[0].upper())
#                 SMART_KEY.add(word[0].lower())
#                 done = True
#                 break
#         for i in range(len(WORD)) :
#             if WORD[i] not in SMART_KEY and WORD[i] != " " and not done :
#                 WORDS.append(WORD)
#                 INDEXES.append(WORD.find(WORD[i],i))
#                 SMART_KEY.add(WORD[i].upper())
#                 SMART_KEY.add(WORD[i].lower())
#                 done = True
#                 break
#     if not done :
#         WORDS.append(WORD)
#         INDEXES.append(-1)
#
#
# for i in range(len(WORDS)) :
#     targetIndex = INDEXES[i]
#     word = WORDS[i]
#     print(word[:targetIndex] + "[" + word[targetIndex] + "]" + word[targetIndex + 1:])

    # [[ Legacy ]]
    # for k in range(len(word)) :
    #     if k == targetIndex :
    #         print("[%s]"%word[k],end="")
    #         continue
    #     print(word[k],end="")
    # if i < len(WORDS)-1 :
    #     print()

""" 시도 2 :  """
""" 단축기로 지정된 알파벳 """
SMART_KEY = set()
""" 모든 단어 탐색 """
for _ in range(N):
    WORDS = list(input().rstrip().split())

    """" 1번과 2번의 방법을 수행 """
    for i in range(len(WORDS)):
        """ 현재 단어의 첫 글자가 단축기로 지정되어 있지 않다면 """
        if WORDS[i][0].upper() not in SMART_KEY:
            """이미 사용한 SMART_KEY로 등록"""
            SMART_KEY.add(WORDS[i][0].upper())
            WORDS[i] = "[" + WORDS[i][0] + "]" + WORDS[i][1:]
            print(" ".join(WORDS))
            """
            첫 번째 글자에서 발견될 경우에도 break
            -> 첫번째 단어의 첫 글자가 있으면 다음 단어의 첫글자로 넘어감
            """
            break

    else:
        """
        반복문이 break를 통과 X -> 처음부터 모든 글자 순회
        단축키 설정 완료 여부
        """
        done = False
        for i in range(len(WORDS)):
            for k in range(len(WORDS[i])):
                if WORDS[i][k].upper() not in SMART_KEY:
                    SMART_KEY.add(WORDS[i][k].upper())
                    done = True
                    WORDS[i] = WORDS[i][:k] + "[" + WORDS[i][k] + "]" + WORDS[i][k + 1:]
                    print(" ".join(WORDS))
                    break
            if done:
                break

        """
        끝까지 단축키 설정할 글자를 못찾았으면 그냥 출력
        """
        if not done :
            print(" ".join(WORDS))