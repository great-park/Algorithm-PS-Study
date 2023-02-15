import sys
input = sys.stdin.readline

ex = list(sys.stdin.readline().rstrip().split('-'))
start = 0
for s in ex[0].split('+') :
    start += int(s)
for i in range(1, len(ex)) :
    s = 0
    nums = ex[i].split('+')
    for n in nums :
        s += int(n)
    start -= s
print(start)
