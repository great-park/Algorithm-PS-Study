from sys import stdin
input = stdin.readline

# 1. 입력된 순 단어 첫 글자 (해당 글자 단축키 없을 시)
# 2. 왼쪽부터 차례대로
# 3. 그대로

N = int(input())
data = list([input().split(), 0, 0] for _ in range(N))  # with 단축키 지정 인덱스
short_cut = []  # 단축키 모음


def find_short_cut(words):
    word = words[0]  # [Save, As]
    done = False
    word_seq_id = 0  # 단어 인덱스

    # 1. 현 단축키 유무로 단어의 첫글자 넣기
    for char in word:
        char_list = list(char)
        if char_list[0] not in short_cut:
            short_cut.append(char_list[0])
            done = True
            words[1] = word_seq_id
            words[2] = 0
        word_seq_id += 1

    # 2. 왼쪽부터 순서대로 검사하기
    if not done:
        word_seq_id = 0  # 단어 인덱스 초기화
        for char in word:
            char_list = list(char)
            for i in range(len(char_list)):
                if char_list[i].isupper():

                    if char_list[i] not in short_cut:
                        short_cut.append(char_list[i])
                        done = True
                        words[1] = word_seq_id
                        words[2] = i
                else:
                    if char_list[i].upper() not in short_cut:
                        short_cut.append(char_list[i])
                        done = True
                        words[1] = word_seq_id
                        words[2] = i

                if done:
                    break
            word_seq_id += 1


def make_result(words):
    word = words[0]
    word_seq_id = words[1]
    inword_id = words[2]

    word_list = list(word[word_seq_id])
    word_list[inword_id] = '[' + word_list[inword_id] + ']'
    word[word_seq_id] = word_list

    return word


for i in range(N):
    find_short_cut(data[i])  # 한 줄당 shor_cut 찾기

    result = make_result(data[i])

    for x in result:
        if x == result[-1]:
            for y in x:
                print(y, end='')
        else:
            for y in x:
                if y == x[-1]:
                    print(y, end=' ')
                else:
                    print(y, end='')

    print()
