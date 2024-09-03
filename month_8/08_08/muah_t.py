#다양한 연산자(^제곱 연산 포함), 괄호, 숫자 2자리 이상에 대한 표현식을 후위표기법으로 바꾸기

#Stack내에서의 연산 우선 순위
#괄호의 주요 목적은 연산 순서 명시
#괄호 안의 연산을 먼저 수행해야 하므로 스택안에서 괄호 '('는 낮은 우선순위를 갖도록함
#모든 연산자가 처리될때까지 괄호 '(' 스택에 남아있도록 함
#')' 닫는 괄호를 만났을 떄 , 스택에서 여는 괄호 '('를 만날떄까지 모든 연산자를 꺼내기 쉬움
# 즉 '('여는 괄호는 스택의 바닥에 위치게 함
isp = {'(':0, '+':1, '-':1, '*':2, '/':2, '^':3} #^:제곱연산

expression = "(335+4) * (42-6^2)/5" #계산할 표현식

stack = [0]*len(expression)
postfix =[]

# 표현식 순회
top=-1
i=0
while i< len(expression):           # 인덱스를 자유롭게 바꾸려면 while이 좋음.
    ch = expression[i]
    #숫자 먼저 파악
    if ch.isdigit():
        temp_num = ch
        # 연속된 숫자인지 확인.
        for j in range(i+1, len(expression)):
            if expression[j].isdigit():
                temp_num +=expression[j]
                i=j
            else:
                break
        postfix.append(temp_num)
    elif ch == '(' :
        top += 1
        stack[top] = ch
    elif ch == ')':
        # 연산자를 postfix에 넣어줌.
        while top > -1 and stack[top] != '(':
            postfix.append(stack[top])
            top -= 1
        top -= 1
    elif ch in isp:
        # 현재 연산자의 우선순위가 stack의 top연산자의 우선순위보다 같거나 작은 경우.
        # stack top에 있는 연산자를 postfix에 넣기
        while top >-1 and isp[stack[top]] >=isp[ch]:
            postfix.append(stack[top])
            top -= 1
        top+=1
        stack[top] =ch
    i += 1

    # stack에 남아있는 연산자들 pstfix에 추가
while top > -1:
    postfix.append(stack[top])
    top-=1

print(postfix)

