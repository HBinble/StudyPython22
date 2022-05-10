# 1. 반지름 값을 입력받아 원의 넓이를 구하여 출력하는 프로그램을 구현하세요. 
    # 파이는 3.141592 입니다.


""" area = float(input('반지름: '))
pi = 3.141592

print("="*15, "결과","="*15)
print('원의 넓이 :', area*area*pi) """

# 2. 태양계는 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 혜왕성, 명왕성으로 구성됩니다. 
    # 영어이름은 Mercury, Venus, Earth, Mars, Jupiter,  Saturn, Uranus, Neptune 입니다. 
    # 행성의 한글이름을 입력하면 영어행성명이 출력되는 프로그램을 구현하세요.

""" solarsys = {'수성':'Mercury', 
            '금성':'Venus', 
            '지구':'Earth', 
            '화성':'Mars', 
            '목성':'Jupiter',
            '토성':'Saturn', 
            '천왕성':'Uranus', 
            '혜왕성':'Neptune'}

name = input('행성의 한글이름을 입력하세요 : ')

print(solarsys[name]) """

# 3. 입력한 한글 문자열의 단어의 수를 출력하는 프로그램을 구현하세요. 
    # 예) 흐르는 강물을 거꾸로 거슬러 오르는 연어들의 = 6

""" def count_word(text):
    length = len(text)
    count = 0
    for x in range (length):
        if text[x] == ' ':
            if x != 0:
                count = count + 1
        elif x == length - 1:
            count = count + 1
    return count

input_txt = input('문장을 입력하세요 : ')
print(input_txt, '=', count_word(input_txt)) """



# 4. 입력한 수를 거꾸로 출력하는 프로그램을 구현하세요. 
    # 예) 1 4 5 9 2 --> 2 9 5 4 1  (exam04.py)

# def reverse_num(num):
#     reverse = int(str(num)[::-1])
#     count = 0
#     for x in range(reverse):
#         if reverse == 0:
#             if x != 0:
#                 count = count + 1
#         elif x == reverse - 1:
#             count = count + 1
#     return count

# # input_txt = input('문장을 입력하세요 : ')
# # print(input_txt, '=', reverse_num(input_txt))

# input_num = input('수를 입력하세요 : ')
# print('거꾸로 출력된 값은 :', reverse_num(input_num))


# 5. 구구단을 수행할 단번호를 입력하면 그 단의 9까지의 결과를 나열하는 프로그램을 입력하세요. 
    # 예) 3 --> 3 6 9 12 15 18 21 24 27
# num = 0

# num = int(input())

# for x in range(2,10):
#     print('단을 입력하세요 \n단번호 : ', end = ' ')
#     for y in range(1, 10):
#         print(f'{x}x{y}={x*y:2d}', end=' ')
#     print('')      


# while True:
#     gugudan = int(input('구구단을 외우자 : '))
#     if gugudan == 0:
#         break

#     i = 1
#     print(gugudan, '단')
#     for x in range(1,10):
#         print(gugudan, '*', i, ' = ', gugudan*i, end=' ')

x = 0

while True:
    if x == 0:
        print('0을 입력하였습니다.')
        break

    else:        
        for x in range(2,10):
            for y in range(1, 10):
                print(f'{x*y}', end=' ')

x = int(input('구구단을 외우자(숫자를 입력하시오) '))






