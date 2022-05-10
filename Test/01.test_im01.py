# 2번문제
print('---행성 영문이름 찾기 프로그램 v1.2---')

dic = {'수성':'Mercury', '금성':'Venus', '지구':'Earth', '화성':'Mars',
       '목성':'Jupiter', '토성':'Saturn', '천왕성':'Uranus', '혜왕성':'Neptune '}
name = input('찾으실 행성의 한글이름을 입력하세요.')

print('입력하신 행성은', f'{name}', '입니다.')
print('입력하신 행성의 영문이름은', f'{dic[name]}', '입니다.')
print('---행성 영문이름 찾기 프로그램 종료---')

# # 2번문제

# solarsys = {'수성':'Mercury', 
#             '금성':'Venus', 
#             '지구':'Earth', 
#             '화성':'Mars', 
#             '목성':'Jupiter',
#             '토성':'Saturn', 
#             '천왕성':'Uranus', 
#             '혜왕성':'Neptune'}

# name = input('행성의 한글이름을 입력하세요 : ')

# print(solarsys[name])