#%%
# 거스름돈 문제
money = 5670 #거슬러줄 돈
changes = [1000,500,100,50,10]

# 각 돈 단위별로 몇개씩 고객에게 줄까?
'''
money //1000 -> 5
money %1000 -> 670

money // 500 -> 1
money % 500 -> 170

money // 100 -> 1
money % 100 -> 70
'''
for change in changes:
    mok,res =divmod(money,change)
    print(change,mok)

    money = res
    if money == 0:
        break


