import sys
sys.stdin = open('jul.txt')

N= int(input())
lst = list(map(int,input().split()))
result = []

for i in range(len(lst)):
    if lst[i] == 0:
        result.append(i+1)
    elif lst[i] >= 1:
        result.insert(i-lst[i],i+1)
print(*result)
# print(lst)
# lst.remove(lst[3])
# print(lst)
