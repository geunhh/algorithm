import sys
sys.stdin = open('pip.txt')


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
print(board)
i,j=0,0
while not (i==N and j==N-1):
    print(i,j)
    i+=1
    j+=1
