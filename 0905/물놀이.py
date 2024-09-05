import sys
sys.stdin= open('water.txt')
from _collections import deque

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    lst = [input() for _ in range(N)]
    deq = deque()
    print(lst)

    for i in range(N):
        for j in range(M):
            print(lst[i][j])


