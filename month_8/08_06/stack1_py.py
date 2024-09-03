#%%
def stack(item):
    global top
    top+=1

top=-1
T=int(input())
for tc in range(1,T+1):
    arr = list(input().split())
    print(arr)
    