STACK_SIZE=10
stack = [0]*STACK_SIZE
top = -1

# push(1)
top += 1
stack[top] = 1
top += 1
stack[top] = 2
top += 1
stack[top] = 3
print(stack)

top -= 1
print(stack[top+1])
print(stack[top])
top -=1




