from sys import stdin
input = stdin.readline
duck = list(input().rstrip())
size = len(duck)
duck_seq = ["q", "u", "a", "c", "k"]
ans = 0
complete = True


def find_duck():
    global ans, complete
    pointer = 0
    cur_duck_sound_size = 0
    exist = False
    for i in range(size):
        if duck[i] == 'X':
            continue

        if duck[i] == duck_seq[pointer]:
            duck[i] = 'X'  # X로 바꾸자
            cur_duck_sound_size += 1
            pointer += 1

        # 하나의 울음 소리를 찾음
        if pointer == 5:
            pointer = 0
        if cur_duck_sound_size == 5:
            exist = True

    # 한 마리 추가
    if exist:
        ans += 1
    if cur_duck_sound_size % 5 != 0:
        complete = False


def go():
    stop = False
    for i in range(size):
        if duck[i] == 'q':
            return not stop
    return stop


def valid():
    for i in range(size):
        if duck[i] != 'X':
            return False
        if ans == 0:
            return False
        if not complete:
            return False
    return True


while go():
    find_duck()

result = ans if valid() else -1
print(result)
