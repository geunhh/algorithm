import sys
sys.stdin = open('candy.txt')

def calc(A,B,C):
    eats = 0
    if B < 2 or C < 3:
        return -1
    if B >= C:
        eats += B-(C-1)
        B = C-1
    if A >= B:
        eats += A-(B-1)
        A = B-1
    return eats





for tc in range(1,int(input())+1):
    A,B,C = map(int, input().split())
    result = calc(A,B,C)
    print(f'#{tc} {result}')



