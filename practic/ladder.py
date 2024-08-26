import sys
sys.stdin = open('ladder.txt')

def where_start(lst):
    for i in range(100):
        if lst[i] == 2:
            return i

def where_dest(i,j):
    while 1:
        # 도착지 찾았다.
        if i == 0:
            return j
        if j-1>=0 and lst[i][j-1]==1:
            j-=1
        elif j+1 < 100 and lst[i][j+1]:
            j+=1
        else:
            i-=1

        lst[i][j] = 0




for tc in range(1,11):
    tc_=int(input())
    lst = [list(map(int,input().split())) for _ in range(100)]
    start = where_start(lst[-1])
    start = [99,start]
    result = where_dest(start[0],start[1])
    print(f'#{tc} {result}')
