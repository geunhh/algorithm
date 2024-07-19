#%%
# 튜플값을 우회적으로 바꾸기
t1= (1,2,['사과','포도'])
t1[-1][0] = '귤'
print(t1)
# 튜플에는 주소값이 저장된다. 튜플 특성상 해당 주소값을 바꿀 수는 없다.
# 그러나 튜플 내 List 내부의 주소값을 바꾸는 건 가능.
# %%
# 논리 연산자
# 1) and (&)
print(True & True)
print(True and True)
print(True & False)

# or ( | )
print(True | True)
print(True or True)
print(True | False)
print(False | False)

# xor : ^만 사용가능
# 다르면 True, 같으면 False.
print(True ^ True)
print(True ^ True)
print(True ^ False)
print(False ^ False)
# %%
print(0b1011 & 0b0111)
print(bin(0b1011 & 0b0111))
print(str(bin(0b1011 & 0b0111)))
print(str(bin(0b1011 & 0b0111))[2:4],end='\n\n')

print(0b1111 | 0b0111)
print(bin(0b1111 | 0b0111))
###################################
# %%
# 내림 반올림 올림
num = 3.34567
# 1) 내림
floor_num = int(num)
print(floor_num)

# 2) 반올림
round_num = round(num)
print(round_num)
print(  round(num,2)  )
print(  round(num,4)  )

# 3) 올림
ceil_num = int(num +0.9999999999999999999)
print(ceil_num)

ceil_num = int(num) + (num != int(num))
print(ceil_num)

ceil_num = -(-num//1)
print(ceil_num)

import math
print(math.ceil(num))
