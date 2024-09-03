def f(i,N):
    if i ==N:
        return
    else:
        print(arr[i])
        f(i+1,N)

arr=[1,2,3]
N=3
f(0,N)