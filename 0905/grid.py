'''
1차원 배열로 받아서 (i-1),(i+1),(i+N),(i-N)을 i로 visited와함께  재귀로 넘김.
'''
import sys
sys.stdin = open('grid.txt')
sys.setrecursionlimit(10000000)

def func1(i, visited):
    # print(i,visited)
    if i < 0 or i >= 16 :
        return

    if len(visited) == 7 :
        result.add(visited)
        return

    if i % 4 != 0 :
        func1(i - 1, visited + lst[i])
    if i % 4 != 3:
        func1(i + 1, visited + lst[i])
    if i >= 4 :
        func1(i - 4, visited + lst[i])
    if i < 12:
        func1(i + 4, visited + lst[i])



for tc in range(1,int(input())+1):
    lst = []
    for _ in range(4):
        inp = list(input().split())
        for i in range(4):
            lst.append(inp[i])

    result = set()
    # print(lst)

    for i in range(16):
        func1(i,'')


    print(f'#{tc} {len(result)}')

# print(sorted(list(set(result))))

