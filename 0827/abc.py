'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def dfs(node):

    if node == 0:
        
        return
    
    print(node, end=' ')
    dfs(left[node])
    dfs(right[node])

N=13
E = N-1
arr = list(map(int,input().split()))
left = [0]*(N+1)    # 왼쪽 자식번호를 저장할 list
right = [0]*(N+1)   # 오른쪽 자식번호를 저장할 list.
par = [0]*(N+1)     # 부모 배열.

for i in range(E):
    parent,child = arr[i*2],arr[i*2+1]
    
    # 왼쪽 자식이 없다? 0이다?
    if left[parent] == 0:
        left[parent] = child    # 삽입
    # 왼쪽은 있는데 오른쪽이 없어??
    else : 
        right[parent] = child
# print(left)
# print(right)

dfs(1)


