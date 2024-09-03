import sys
sys.stdin = open('calc.txt')

def clac2(node):
    if node:
        if value[node] in ['+', '/', '*', '-']:
            # 연산자일 경우 괄호로 묶음
            left = calc2(graph[node][0])
            right = calc2(graph[node][1])
            return f'({left}{value[node]}{right})'

        else:
            # 숫자일 경우
            return value[node]

for tc in range(1,11):
    N = int(input())    # 각 정보 개수
    arr=[]
    for _ in range(N):
        arr.append(input().split())


    graph = [[] for _ in range(N+1)]    # 인접 행렬 [[], [], [], [], [], []] 초기화
    value = [0]*(N+1)                   # value    [0, 0, 0, 0, 0, 0] 초기화

    # 인접 행렬 만들기.
    for lst in arr:
        # len==4 : 연산자가 잇을 때 ['1', '-', '2', '3']
        if len(lst)==4:
            graph[int(lst[0])] = [int(lst[2]),int(lst[3])]  # graph[1] = ['2','3']
            value[int(lst[0])] = lst[1]                     # value[1] = '-' 연산자는 따로 저장

        # len==2 : 끝단일 때
        else:
            graph[int(lst[0])] = [0,0]
            value[int(lst[0])] = lst[1]

    result = eval(clac2(1))
    print(f'#{tc} {int(result)}')