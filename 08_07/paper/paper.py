# 규칙(점화식)을 찾아서 재귀함수 또는 DP로 구하는 것 추천
# f(n) = 2 f(n-2) + f(n-1)
import sys
sys.stdin = open('4869_input.txt','r')

def paper(N): # 30
    n = N//10 # 30
    p = [0] * n
    p[0] = 1

    if n == 1:
        return p[0]
    else:
        p[1] = 3

    for i in range(2,n):
        p[i] = 2*p[i-2] + p[i-1]

    return p[n-1]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result = paper(N)
    print(f'{tc} {result}')