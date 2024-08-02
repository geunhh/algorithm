import sys
sys.stdin = open("4864_input.txt", "r")

def comp(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    for i in range(len2-len1+1): # 0 1 2 ... len2-len1)
        print(str1,str2[i:i+len1])
        if str1[:] == str2[i:i+len1]:
            return 1
    return 0



T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    print(str1, str2)
    result = comp(str1,str2)
    print(f'#{test_case} {result}')