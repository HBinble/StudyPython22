# 파일 입출력 2 - 파일 읽기

f = open(file = './temp.txt', mode='r', encoding='utf-8')

# t = f.read() # 모든 파일 읽을 때(잘 안씀)
while True:
    line = f.readline() # 한줄 씩 읽을 때 
    if not line: break

    print(line, end='')

f.close ##필수
print('파일 읽기 완료')