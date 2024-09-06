import sys
from collections import defaultdict
sys.stdin = open('cell.txt')

for tc in range(1,int(input())+1):
    ''' N : 세로크기, M 가로크기, K 배양 시간
    '''
    N,M,K = map(int,input().split())
    inp = [list(map(int,input().split())) for _ in range(N)]
    print(inp)
    board= defaultdict(lambda :None)
    print(board)
    for i in range(N):
        for j in range(M):
            board[i,j] = inp[i][j]

    board[-1,-9] = 5
    print(board)
    for i in range(-1,10):
        for j in range(-9,10):
            print(board[i,j])

    break
