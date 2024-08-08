import sys
sys.stdin = open('calc_input.txt','r')

my_dict = {'+': 1, '-': 1, '/': 2, '*': 2}

T = int(input())
for tc in range(1, 1 + T):
    words = input()
    # words = '9+8+5+9+2+4+1+8+3+9+3+8+7+8+6+8+9+4+1+1+7+6+1+5+8+7+6+9+6+3+1+3+1+7+5+9+2+8+4+3+7+3+4+7+3+4+8+3+2+6+6'
    words = '3+5*2'
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


    result += (''.join(stack[::-1])) # 후위 표기 끝.
    print(f'#{tc} {result}')




