### My Part ###
import sys
input = sys.stdin.readline

RECORD = list(input().rstrip())
SIZE = len(RECORD)

"""
정상적으로 오리가 1마리 이상이라면 quack의 길이만큼 정확히 나누어 떨어져야함
-> 처음 시작할 때, 1차 필터링
"""
if SIZE % 5 != 0:
    print(-1)
else :
    """ 다음에 나올 수 있는 값에 대한 딕셔너리 """
    NEXT_SOUND = dict()
    NEXT_SOUND['q'] = 'u'
    NEXT_SOUND['u'] = 'a'
    NEXT_SOUND['a'] = 'c'
    NEXT_SOUND['c'] = 'k'
    NEXT_SOUND['k'] = 'q'

    CHECKED = [False] * len(RECORD)
    COUNT = 0
    """
    두번째 for문에 i+1, SIZE를 돌기 때문에
    i의 범위는 SIZE-1까지만
    """
    for i in range(SIZE-1) :
        """
        아직 세보지 않은 울음소리의 시작일 경우
        """
        if RECORD[i] == 'q' and not CHECKED[i] :
            """
            for 문 시작전에 count + 1 해주고 방문 처리
            """
            count = 1
            CHECKED[i] = True
            next = NEXT_SOUND.get(RECORD[i])
            """
            다음칸 ~ 끝까지 브루트포스
            """
            for k in range(i+1,SIZE) :
                """
                해당칸이 앞선 소리의 다음 소리가 맞고 방문한 적 없다면
                count +1 & 방문 처리 & 다음소리 갱신
                """
                if RECORD[k] == next and not CHECKED[k]:
                    count += 1
                    CHECKED[k] = True
                    next = NEXT_SOUND.get(RECORD[k])
            """
            비정상적인 울음소리일 경우 -> 오리가 없다고 처리해버리고 break
            """
            if count % 5 == 0 :
                COUNT += 1
            else :
                COUNT = 0
                break

    """
    비정상적인 울음소리 == 오리가 없는 경우 -> -1 출력
    """
    if COUNT == 0 :
        print(-1)
    else :
        print(COUNT)

