# a = 1
# print(a)

# def vartest(x): # x -> a , a와 def vartest(a)와는 다르다!
#     print(x) # 지역변수
#     x = x + 10
#     return x

# a = vartest(3)
# print(a)


a = 1
print(a)

def vartest():
    global a # 전역변수
    print(a)
    a = a + 10
    return a

a = vartest()
print(a)


while a < 10:
    pass

for x in range(1,11):
    pass

if a ==13:
    pass # pass : 코드 오류 시 실행하게 하는 것