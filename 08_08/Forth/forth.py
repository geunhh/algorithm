'''
숫자는 스택에 넣기.
연산자를 만나면 스택의 숫자 두개 꺼내서 더하고 결과 다시 스택에 넣기.
'.'은 스택에서 숫자 꺼내 출력하기.
형식이 이상하면, error 출력.
- 연산 하려는데, not stack이거나, pop 한게 연산자일 때 error.
'''
def cal(right, left, oper):
    if oper == '/':
        return str(int(left) // int(right))
    elif oper == '*':
        return str(int(left) * int(right))
    elif oper == '+':
        return str(int(left) + int(right))
    elif oper == '-':
        return str(int(left) - int(right))
    return 'error'

def forth(arr):
    for elem in arr:
        # print(elem, '할거임')
        if elem == '.':
            if len(stack)!=1:
                return ['error']
            return stack
        # stack 비었는데, elem이 숫자가 아니다?
        if not stack and elem.isdigit() == False:
            return ['error']
        # elem 이 숫자다. -> push
        elif elem.isdigit():
            stack.append(elem)
            # print(stack)
        # elem 이 숫자다 아니다 -> 연산자이면?
        elif elem.isdigit() == False:
            # 연산하려는데 남은 애가 한명이다? 연산 못함.
            if len(stack) <2:
                return ['error']
            # elem은 oper로 저장 #
            oper = elem
            right = stack.pop()
            left = stack.pop()
            # print(oper, right, left)
            # pop으로 뽑은 애들이 숫자가 아니다?
            if right.isdigit() == False or left.isdigit() ==False:
            # if not (right.isdigit() and left.isdigit()):
                return ['error']
            else :
                cal_v = cal(right, left, oper)
                # print(cal_v)
                stack.append(cal_v)
                # print(stack)





import sys
sys.stdin = open('4874_input.txt','r')

T= int(input())

for tc in range(1,T+1):
    stack =[]
    arr = list(input().split())

    result = forth(arr)
    print(f'#{tc}',end=' ')
    print(*result)






