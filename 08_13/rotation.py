import sys
sys.stdin = open('5097_input.txt')
from collections import deque

T = int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    lst = list(map(int, input().split()))
    d=deque(lst)

    for _ in range(M):
        d.append(d.popleft())

    print(f'#{tc} {d[0]}')
