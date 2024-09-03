def f(t,p):
    N=len(t)
    M=len(p)

    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
            else:
                return i
    return -1



# t='TTTTTATTAATA'
t= 'ABAFSDWWG'

p='TTA'
result = f(t,p)
print(result)