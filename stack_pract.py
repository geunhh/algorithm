import sys
sys.stdin = open('stack.txt')

def recovery():
    stack=[]
    stack.append('0')
    # print(stack)
    cnt=0
    for mem in memory:
        if stack[-1] != mem:
            cnt+=1
            stack.pop()
            stack.append(mem)
    return cnt



for tc in range(1,1+int(input())):
    memory = input().strip()
    # print(memory)
    cnt = recovery()
    print(f'#{tc} {cnt}')




