import sys
sys.stdin =open('input.txt','r')
my_dict = {'q':'p','p':'q','d':'b','b':'d' }

def mirror(word):
    new_word =''
    for c in word:
        new_word+=my_dict[c]
    return new_word




T = int(input())
for test_case in range(1,T+1):
    word = input()

    word = list(word)
    word.reverse()
    word = ''.join(word)
    result = mirror(word)
    print(f'#{test_case} {result}')

