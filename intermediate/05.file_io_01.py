# 파일 입출력 1 - 쓰기

# mode = w 새로생성 a 추가쓰기 r 읽기
f = open(r'C:/STUDY/StudyPython22/temp.txt', mode='a', encoding='utf-8')

f.write('안녕하세요.\n')
f.write('저는 이한빈입니다.\n')
f.write('한국사람이죠.\n')

f.close() #필수! : Network, DB, File(3가지) open 시 close 무조건 쓰기!!!
print('파일 생성완료')
