import sys
input = sys.stdin.readline

"""
크레인 N 대 -> 동시에 움직임 : 무게 제한 -> 무게 제한보다 무거운 박스는 움직일 수 없음

1분에 박스 1개

모든 박스를 옮기는데 드는 최소 시간
"""
N = int(input())
CRANE_LIMIT = list(map(int, input().split()))

BOX_QUANTITY = int(input())
BOX_WEIGHT = list(map(int, input().split()))


"""
매번 한계무게가 높은 크레인부터 비교하며 높은 무게부터 옮기기
"""
CRANE_LIMIT.sort(reverse=True)
BOX_WEIGHT.sort(reverse=True)


if CRANE_LIMIT[0] < BOX_WEIGHT[0] :
    print(-1)
else :
    result = 0
    while BOX_WEIGHT:
        idx = 0
        i = 0
        while i < N:
            if idx == len(BOX_WEIGHT):
                break
            elif CRANE_LIMIT[i] >= BOX_WEIGHT[idx]:
                BOX_WEIGHT.pop(idx)
                i += 1
            else:
                idx += 1
        result += 1
    print(result)



"""
while(!box.isEmpty()){
    int idx = 0;
    
    // crane
    for(int i = 0; i < crane.size(); ){
        if(idx == box.size) {
            break;
        } else if(crane.get(i) >= box.get(idx){
            box.remove(idx);
            i++;
        } else {
            idx++;
        }
    }
    res++;
} 
"""




