import sys
sys.stdin = open('crush.txt')

for tc in range(1, int(input())+1):
    N,W,H = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(H)]
    for row in lst:
        print(row)

    break