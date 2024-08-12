import sys
sys.stdin = open('rect.txt', 'r')
arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))
print(arr)
print(max(arr))
print(max(max(arr)))
zero_matrix = [[0] * max(max(arr)) for _ in range(max(max(arr)))]

cnt=0
for index in range(4):
    x1,y1,x2,y2 = arr[index]
    for x in range(x1,x2):
        for y in range(y1,y2):
            zero_matrix[x][y] += 1
            if zero_matrix[x][y] > 1:
                pass
            else:
                cnt+=1

print(cnt)


