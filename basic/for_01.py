# for문 학습
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 한줄 주석
'''
다중 문자열 == 여러줄 주석
'''

''' result = 0

for x in range(1, 101): # 내가 원하는 값 +1(100(X) -> 101(O))
    result = result + x
    
print('배열의 합 =', result)

arr2 = ('me', 'my', 'friend', 'jane') #튜플

for item in arr2:
    print(f'{item * 2}')  # print(f'{item:>10}') 

arr2 = ['me', 'my', 'friend', 'jane'] #리스트

for item in arr2:
    print(f'{item * 2}')  # print(f'{item:>10}') 
'''
'''
## 1~10RKwl 수에서 짝수 구분하기
for num in range(1, 11, 2): # range (시작값, 마지막값+1, 증감 규칙)
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 홀수입니다.')
'''

# for문 내에서 사용하는 continue, break
values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = 0 
for item in values:
    num += 1 # num = num + 1
    if (num % 2) == 0:
        #break # 반복문 탈출
        continue # if 조건만 패스 다음값 진행
    else:
        print(f'{num}번 수는 {item}입니다.')

