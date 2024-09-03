import sys
sys.stdin = open('calc.txt')

def calc(node):
    if node : # node가 있으면, 연산자 별로 처리.
        if value[node] == '+':
            return calc(graph[node][0]) + calc(graph[node][1])
        elif value[node] == '-':                                 #여기
            return calc(graph[node][0]) - calc(graph[node][1])
            # graph[1][0] - graph[1][1
        elif value[node] == '/':
            return calc(graph[node][0]) // calc(graph[node][1])
        elif value[node] == '*':
            return calc(graph[node][0]) * calc(graph[node][1])
        else: # 숫자일 때:
            return int(value[node])


def calc2(node):
    if node:
        if value[node] in ['+','/','*','-']:
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
    #[['1', '-', '2', '3'], ['2', '-', '4', '5'], ['3', '10'], ['4', '88'], ['5', '65']]


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
    # print(graph)        # [[], [2, 3], [4, 5], [0, 0], [0, 0], [0, 0]]
    # print(value)        # [0, '-', '-', '10', '88', '65']

    result = eval(calc2(1))
    print(f'#{tc} {int(result)}')