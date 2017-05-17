#함수
#파이썬 함수의 구조
"""
def sum(a,b)
    return a + b
이 함수의 함수명은 sum이고 입력 인수로 2개의 값을 받으며 결과값은 2개의 입력값을 더한 값 이다
"""
def sum(a,b):
    return a+b
a = 3
b = 4
c = sum(a,b)
print(c) # 7

#일반적인 함수 - 입력값이 있고 결과앖이 있는 함수가 일반적인 함수
"""
def 함수명(입력 인수):
    수행할 문장
    ...
    return 결과값
"""
def sum(a,b):
    result = a+b
    return result # a+b의 결과값 리턴

a=sum(3,4)
print(a) # 7
## 결과값을 받을 변수 = 함수명(입력 인수 1, 입력 인수 2,,,)

#입력값이 없는 함수
def say():
    return 'HI'
a = say()
print(a) # HI
## 결과값을 받을 변수=함수명()

#결과값이 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))
sum(3,4) #3, 4의 합은 7입니다.
## 함수명(입력 인수1,입력 인수2,,,)

#결과값이 진짜 없는지 확인
a=sum(3,4)
print(a) #None
##결과값이 없음

#입력값도 결과값도 없는 함수
def say():
    print('Hi')
say() #HI
##함수명()

###입력값이 몇개가 될지 모를때는?
"""
def 함수명(*입력 변수):
    수행할 문장
    ...
"""

#여러 개의 입력 값을 받는 함수 만들기
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i #*args에 입력받은 모든 값을 더한다
    return sum
result = sum_many(1,2,3) #sum_many 함수의 결과값을 result 변수에 대입
print(result) #6
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result) # 55

print("="*50)#구분선

def sum_mul(choice, *args):
    if choice == "sum": #입력 인수 choice에 'sum'을 입력 받았을 때
        result = 0
        for i in args:
            result = result + i # args에 입력받은 모든 값을 더한다
    elif choice == "mul": #입력 인수 choice에 'mul'을 입력받았을 때
        result = 1
        for i in args:
            result = result*i # *args에 입력받은 모든 값을 곱한다.
        return result
result = sum_mul('sum',1,2,3,4,5)
print(result) #15 None 오류
result = sum_mul('mul',1,2,3,4,5)
print(result) # 120

#함수의 결과값은 언제나 하나
def sum_and_mul(a,b):
    return a+b,a*b
result = sum_and_mul(3,4)
print(result) #(7, 12)
sum, mul = sum_and_mul(3,4)
print(sum, mul) # 7 12

##return문을 2번 사용시 첫번째 리턴문만 실행된다

#return의 다른 쓰임새
#함수를 빠져나가고자 할 때 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_ncik(nick):
    if nick == "바보":
        return
    print("나의 별병은 %s입니다."% nick)

#입력 인수에 초깃값 미리 설정하기
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자")
    else:
        print("여자")
say_myself("이건호",21)
"""
나의 이름은 이건호입니다.
나이는 27살입니다.
남자
"""

say_myself("이예은",18,False)
"""
나의 이름은 이예은입니다.
나이는 18살입니다.
여자
"""

##함수 안에서 함수 밖의 변수를 변경하는 방법
#return 이용하기
a = 1
def vartest(a):
    a=a+1
    return a
a = vartest(a) #vartest(a)의 결과값을 함수 밖의 변수 a에 대입
print(a)
#vartest 함수는 입력으로 들어온 값에 1을 더한 값을 돌려준다. 띠라서
#a=vartest(a)라고 대입하면 a가 vartest 함수의 결과값으로 바뀐다.
#여기서도 물론 vartest 함ㅅ우 안의 a 변수는 함수 밖의 a와는 다른 것이다

#global 명령어 이용하기
a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)
"""
vartest 함수 안 global a라는 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻.
하지만 프로그래밍을 할때 global 명령어는 사용하지 않는것이 좋다. 왜냐면 함수는
독립적으로 존재하는 것이 좋기 때문이다. 외부 변수에 종속적인 함수는 그다지 좋은 함수가
아니다. 그러므로 가급적 global명령어를 사용하는 이방법은 피하고 첫째 방법을 사용하는것이
좋다."""