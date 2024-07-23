# 리스트와 반복문.
nums = [1,2,3,4,5]

# 값만 참조하고 싶은 경우.
for n in nums:
    print(n)

# 인덱스를 통해 리스트 참조
# ex) 위치 찾을 때, 리스트 수정
for n in range(len(nums)): # range()로 만든 경우 이후에 nums 변수에 접근해서 값의 수나 index가 바뀌어도 range는 바뀌지 않음.
    print(nums[n])

#%%
nums = [1,2,3,4,5]

# 리스트의 특정 요소 삭제. -> 에러.
for i in range(len(nums)): 
    if nums[i] %2 == 0:
        del nums[i] 
# %%

# 삭제 시 인덱스를 거꾸로 참조
nums = [1,2,3,4,5]

for i in range(len(nums)-1,-1,-1): 
    if nums[i] %2 == 0:
        del nums[i] 
print(nums)
# %%
## while 문 활용
while any(i%2 ==0 for i in nums) :
    # 하나씩 지우기.
    for i in range(len(nums)):
        if nums[i]%2 ==0:
            del nums[i]
            break
print(nums)
# %%
nums = [1,2,3,4,5]

for i, num in enumerate(nums):
    print(i,num)
# %%
# 입력된 정수 자리수별로 더하기
# 12345 => 1+2+3+4+5

num = 12345
sum=0
for num in str(num):
    sum += int(num)
print(sum)

# 위의 코드는 형변환에 시간이 소요되기 때문에 아래 코드가 시간이 덜 소요됨.

num = 12345
result = 0
while num :
    result += num % 10
    num = num//10
print(sum)

while num : 
    mok, res = divmod(num,10)
    result += res
    num=mok
print(result)
# %%
lastDayList = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(len(lastDayList)):
    print(f"{i+1}월 - ",end='')
    for day in range(lastDayList[i]):
        print(f"{day+1}일,",end='')
    print()
# %%
# 50 중 369 짝.

for i in range(51):
    if (i % 10 in [3,6,9]):
        print('짝 ',end='')
    if (i//10 in [3,6,9]):
        print('짝 ',end='')
    else:
        print(f"{i} ",end='')

# %%
# 소수 찾기.
# 2,3,5,7,11,13,17 ...
# 1) 2~ 자기숫자 전까지 나누기.
# 2) 자기숫자 // 2
# 2.5) 자기숫자의 제곱근까지
#  if 16. (1,16),(2,8),(4,4),(8,2),(16,1) 제곱근을 기준으로 뒤집어짐.
num =131

for i in range(2,int(num**(1/2)+1)):
    if num%i == 0:      
        print('소수 아님')  
        break
    else :
        pass
    
        
# %%
# 최대 공약수
# 두 수 a,b의 최대공약수는 b와 (a를 b로 나눈 나머지)의 최대 공약수와 같다.
# 위 성질을 반복적으로 적용해서 결국 (a를 b로 나눈 나머지)가 0이 되는 시점의 나누는 수가 최대 공약수(a)이다.

def cal_1 (num1, num2):  # num1, num2 대소 비교까지 했어야 함.
    
    a=num2
    b=num1%num2
    
    if a%b == 0:
        return b
    else :
        return cal_1(a,b)

def cal_2 (num1,num2):
    num3 = cal_1(num1,num2)

    return (num1*num2) // num3

cal_1(18,48)  
cal_2(18,48)



# (a, (a%b))

# 최소 공배수
# a*b // 최대공약수
# %%
# 셋 set
fruits = ['사과','사과','포도','귤']
fruits_set = set(fruits)
print(fruits_set)
fruits_set1 = {f for f in fruits} # set()도 comprehension이 가능하다
print(fruits_set1)
for f in fruits_set1:
    print(f)
# %%
# Dict 
fruits = ['사과','포도','귤']

nums = [100,100,50]

# Dict comprehension
fruit_dict = {k:v for k,v in zip(fruits,nums)} 
print(fruit_dict)

for key in fruit_dict.keys():
    print(key)
for key in fruit_dict.values():
    print(key)
for key,v in fruit_dict.items():
    print(key,v)


# %%
# 딕셔너리와 리스트
score_dict = {'국어':[],'수학':[]}
print(score_dict)
score_dict['국어'].append(30)
score_dict['수학'].append(50)
print(score_dict)

#키가 없는 경우 리스트에 값 넣기.
#score_dict['영어'].append(50) # 에러
score_dict.setdefault('영어',[]).append(50)
print(score_dict)
# setdefault는 딕셔너리에 키가 존재하면, 해당 키의 값을 반환
# 키가 존재하지 않으면 키를 새로 만들고 지정된 기본값을 할당 후 반환.

score_dict.get('영어',[])
# get은 딕셔너리에 키가 존재하지 않으면, 지정된 기본값은 반환.
# 기본값 지정 안 하면 None 반환

# if setdefault가 없었다면?
# 과학점수를 리스트에 추가
if '과학' in score_dict:
    score_dict['과학'].append(30)
else :
    score_dict['과학'] = [30]
# %%
# defaultdict : 일반 딕셔너리와 달리, 존재하지 않는 키에 접근할 때 기본값을 반환
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())
#%%
# 과일 개수
fruits = ['사과','사과','사과','바나ㅏㄴ','키위']

fruit_dict = defaultdict(int)
print(fruit_dict)
for f in fruits:
    fruit_dict[f] +=1
print(fruit_dict)
# %%
dictt = defaultdict(list)
print(dictt)
input = [1,2,3,4,5,6]
for i in input :
    if dictt[i] ==4:
        break
    dictt[i] = str(i)+'번'
    

print(dictt)