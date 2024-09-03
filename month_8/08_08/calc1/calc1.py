import sys
sys.stdin = open('input.txt', 'r')

my_dict = {'+': 1, '-': 1, '/': 2, '*': 2}

def cal(right, left, oper):
    if oper == '/':
        return int(left) / int(right)
    elif oper == '*':
        return int(left) * int(right)
    elif oper == '+':
        return int(left) + int(right)
    elif oper == '-':
        return int(left) - int(right)


T = 10
for tc in range(1, 1 + T):
    # words = input()
    N = int(input())
    words = input()
    stack = []
    result = ''

    for word in words:
        # 연산자가 아니면 결과에 그냥 넣음
        if word not in my_dict:
            result += word

        # 연산자일 경우 우선순위 고려
        elif word in my_dict:
            # stack 이 비었다? 그냥 넣어줌
            if not stack:
                stack.append(word)
            # 스택이 비어있지 않은데, stack[-1]의 우선순위가 나보다 낮다.
            elif stack and my_dict[stack[-1]] < my_dict[word]:
                stack.append(word)
            else:
                while True:
                    if not stack or (my_dict[stack[-1]] < my_dict[word]):  # stack[-1]이 나보다 우선순위가 낮아지면,
                        stack.append(word)  # 펑
                        break
                    pop_val = stack.pop()  # 아니면, pop하고
                    result += pop_val  # 팝한거 넣어주기.

    result += (''.join(stack[::-1]))

    # 계산하기
    stack = []

    for word in result:
        # 피연산자를 만나면 스택에 push
        if not stack or (word not in my_dict):
            stack.append(word)
        # 연산자를 만나면 필요한 만큼 피연산자를 스택에서 pop하여 연산하고 다시 스택에 push
        elif stack and (word in my_dict) :
            oper = word
            right = stack.pop()
            left = stack.pop()
            sol = cal(right,left,oper)
            # sol = str(eval(left + oper + right))    # 연산하고
            stack.append(sol)                       # push
    else :
        print(f'#{tc}',end=' ' )
        print(*stack)







