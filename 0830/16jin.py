import sys
sys.stdin = open('input.txt')

hexaa ={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100',
        '5':'0101','6':'0110','7':'0111','8':'1000','9':'1001',
        'A':'1010','B':'1011','C':'1100','D':'1101','E':'1110',
        'F':'1111'}

for tc in range(1,int(input())+1):
    num = input()
    string_binary =''
    for n in num:
        string_binary+=hexaa[n]
    ###
    print(f'#{tc}',end=' ')
    for i in range(0,len(string_binary),7):
        print(int(string_binary[i:i+7],2),end=' ')
    print()






