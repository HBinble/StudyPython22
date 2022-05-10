# CSV파일 읽기
import csv

file_name = './busanbus_211231.csv'

f = open(file_name, mode='r', encoding='utf-8')
reader = csv.reader(f, delimiter=',') # 구분자가 ,인 경우(csv 파일 열어서 구분자 확인 후 입력)

next(reader) # 제목줄이 있을 때 필요 없을 경우 
for line in reader:
    print(line)

f.close() ##필수

