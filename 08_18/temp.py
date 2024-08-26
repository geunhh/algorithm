N, K = map(int, input().split())
temps = list(map(int, input().split()))
# print(temps)
max_sum=sum(temps[0:K])
cur_sum =max_sum
for i in range(1,N-K+1):
    # print(i)
    cur_sum = cur_sum - temps[i-1] + temps[i+K-1]
    if max_sum < cur_sum:
        max_sum = cur_sum
print(max_sum)

