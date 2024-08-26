import sys
sys.stdin = open('ddd.txt')
T = int(input())
for tc in range(1, 1 + T):
    n, w1, w2 = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort(reverse=True)
    # print(lst)
    w = min(w1, w2)             # 화물 중 더 적은 친구 구분.
    sum = 0
    for i in range(1, w + 1):   # 무거운 화물부터 하나씩 올려줌 (1층부터 w층까지)
        # print(i)
        sum += i * lst.pop(0)   # 무게 * 층
        sum += i * lst.pop(0)

    if w1 > w2:                 # 화물 남아있는 친구 찾아줌.
        y = w1
    else:
        y = w2
    # 남아있는 화물 처리
    for j in range(w + 1, y + 1):   # 이전에 올린층의 +1층부터 곱하고 더해줌.
        sum += j * lst.pop(0)
        # print(j, sum)
    print(sum)