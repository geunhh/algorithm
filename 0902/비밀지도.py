
n=5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n,arr1,arr2):
    arr1_bin = []
    arr2_bin = []
    
    # 1. arr -> 2진수로 변환
    for i in range(n):
        arr1_bin.append(bin(arr1[i])[2:].zfill(n))
        arr2_bin.append(bin(arr2[i])[2:].zfill(n))
    
    print(arr1_bin)
    print(arr2_bin)
    
    # 2. 2진수 -> 지도.
    answer=[]
    for k in range(n):
        result_bin = bin(int(arr1_bin[k],2)| int(arr2_bin[k],2))
        answer.append(result_bin[2:].zfill(n).replace('1','#').replace('0',' '))
    
    return answer
    
   
    
solution(n,arr1,arr2)