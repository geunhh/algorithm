from collections import deque

def solution(priorities, location):
    q = deque()
    cnt=0
    seq = sorted(priorities)
    for i in range(len(priorities)):
        q.appendleft([i, priorities[i]])
    while True:
        if q[-1][1] == seq[-1]:
            if q[-1][0] == location :
                cnt+=1
                return cnt
            q.pop()
            seq.pop()
            cnt+=1
        else:
            q.rotate(1)

priorities = [2,1,3,2]
priorities = [1, 1, 9, 1, 1, 1]
location = 0
result = solution(priorities,location)
print(result)