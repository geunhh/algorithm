# 스택의 push,pop 함수
def push(stack, item):
    global top
    top += 1
    if top == len(stack):
        top = len(stack) - 1
        print('Overflow')
    else:
        stack[top] = item


def pop(stack):
    global top
    if top == -1:
        return None
    else:
        top -= 1
        return stack[top + 1]

    # 여는 괄호는 짝이 있거