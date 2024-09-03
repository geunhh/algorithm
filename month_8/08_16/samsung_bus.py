

import sys
sys.stdin = open('bus.txt')


T= int(input())
for tc in range(1,T+1):
    bus_mat = [0] * 5001

    for _ in range(int(input())):       # 노선만큼 돌려
        A, B = map(int, input().split())
        for i in range(A,B+1):
            bus_mat[i] += 1

    p = int(input())
    print(f'#{tc}', end = ' ')
    for i in range(p):
        print( bus_mat[int(input())], end=' ' )
    print()


