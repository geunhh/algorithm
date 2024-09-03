def fact(n):
    global cnt
    cnt+=1
    if n==0:
        return 1
    else :
        return n*fact(n-1)
cnt=0
fact(10)
print(cnt)