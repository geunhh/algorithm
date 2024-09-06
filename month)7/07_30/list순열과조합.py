#%% 
# 1) 순열 및 조합의 경우의 수 얻기.

import math

#1-1 ) 순열
#순서를 고려하여 나열 (ex> 줄세우기)
#ex [1,2,3] != [3,2,1]
print(math.perm(5,3))   #5P3 다섯개 중 3개 줄 세우기

#1-2 ) 조합
#순서를 고려하지 않고 나열 (ex) 조 만들기)
#ex) [1,2,3] == [2,1,3] != [1,2,4]
print(math.comb(5,3)) #5C3 다섯개중 3개 선택

#%%
# 순환 가능한 객체(iterable)의 순열 및 조합 모두 얻기

#2-1) 순열
from itertools import permutations

arr = ['a','b','c','d','e']
perms = permutations(arr,3)
print(list(perms))

#2-2 조합
from itertools import combinations
combs = list(combinations(arr,3))
print(combs)

#2-3) 중복순열 : 중복을 허용해서 만든 수열
from itertools import product
pros = list(product(arr,repeat=3))
print(pros)

#2-4) 중복조합 : 중복을 허용해서 만든 조합
from itertools import combinations_with_replacement
re_combs = combinations_with_replacement(arr, r=3)
print(list(re_combs))

#2-5) 여러 순환 가능한 객체들의 모든 조합 (중복 x)
arr1 = [1,2,3]
arr2 = ['a','b','c']
arr3 = ['가','난','다']
pros = product(arr1,arr2,arr3)
print(list(pros))

#2-6) 여러 순환가능한 객체들의 모든 조합 (중복 o)
pros = product(arr1,arr2,repeat=2)
print(list(pros))

# %%
