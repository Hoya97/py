#문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미
# #따옴표로 둘러싸여있으면 모두 문자열
"Life is too short, You need Python"
"a"
"123"

#문자열 만드는 방법
"a"
'a'
"""a"""
'''a'''

#문자열에 작은따옴표(')포함시키기
#Python's favorite food is perl
food = "Python's favorite food is perl" #큰따옴표(")로 둘러쌓아야한다
print(food) #Python's favorite food is perl


print("-"*77) #구분선


#문자열에 큰따옴표(") 포함시키기
# "Python is very easy." he says.

say = '"Python is very easy." he says.' #작은따옴표(')로 둘러쌓아야한다
print(say) #"Python is very easy." he says.


print("-"*77) #구분선


#\(백슬래시)를 이용해 작은따옴표(')와 큰따옴표()
푸드 = 'Python\'s favorite food is perl'
세이 = "\"Python is very easy.\" he says."
print(푸드)
print(세이)


print("-"*77) #구분선


#여러 줄인 문자열을 변수에 대입하고 싶을 떄
#줄을 바꾸기위한 이스케이프 코드 '\n' 삽입
multiline = "Life is too shrot\nYou need python"
print(multiline)

#연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""")이용
multilinee = '''  
Life is too shrot
You need python
'''
print(multilinee)

print("-"*77) #구분선

"""이스케이프 코드 
\n 문자열 안에서 줄을 바꿀때
\t 문자열 사이에 탭 간격을 줄 때 사용
\\ 문자 \(역슬래시)를 그대로 표현시 사용
\' 작은따옴표(')를 그대로 표현할 때 사용
\" 큰따옴표(")를 그대로 표현할 때 사용

활용빈도 낮음
\r 캐리지 리턴 (줄바꿈 문자, 현재 커서를 다음줄로 이동)
\f 폼 피드 (줄바꿈 문자, 현재 커서를 다음 줄로 이동)
\a 벨 소리 (출력 시 PC 스퍼커에서 삑 소리가 남
\b 백 스페이스
\000 널 문자
"""

#문자열 연산하기
#문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun"
print(head + tail) #Python is fun

#문자열 곱하기
# *의 의미는 문자열의 반복을 뜻함
q = "python"
print(q * 2)

#문자열 곱하기 응용
print("="*50)
print("My Program")
print("="*50)

print("-"*77) #구분선


#문자열 인덱싱과 슬라이싱
#인덱싱(Indexing)은 무엇인가 '가리킨다'는 의미, 슬라이싱(Slicing)


#문자열 인덱싱
# 파이썬은 0부터 숫자를 셈 a[번호]는 문자열 내 특정한 값을 뽑아내는 역할을 한다. 이것을 인덱싱
w = "Life is too short, You need Python"
e = w[0]+w[1]+w[2]+w[3]
print(w[0], w[15], w[-1], e) #L r n Life # w[-1]은 뒤에서부터 첫번째 문자


print("-"*77) #구분선

#문자열 슬라이싱

r = w[0:4] #w[시작번호:끝번호]를 지정하면 끝번호에 해당하는 것은 포함되지 않음
print(r)

t = w[19:] #끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 뽑아냄
print(t)

y = w[:17]#w[시작 번호:끝 번호]에 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아냄
print(y)

u = w[:] #w[시작 번호 : 끝 번호]에 시작번호 끝번호 생략시 문자열의 처음부터 끝까지 뽑아냄
print(u)


print("-"*77) #구분선

i = "20170410Rainy"
year = i[:4]
day = i[4:8]
weather = i[8:]
print(year)
print(day)
print(weather)

print("-"*77) #구분선

#문자열 Pithon을 Python으로 바꾸려면
p = "Pithon"
print(p[:1] + 'y' + p[2:]) #Python

print("-"*77) #구분선

#문자열 포매팅
#문자열 포매팅(Formatting)이란 문자열 내 어떤 값을 삽입하는 방법
#숫자 바로 대입: 문자열 안에 숫자를 넣고 싶은 자리에 %d라는 문자를 넣어 주고, 삽입할 숫자인3은 가장뒤에있는 % 문자 다음에 써넣음.

z = "I eat %d apples." % 3
print(z)
#I eat 3 apples.


#문자열 바로 대입

x = "I eat %s apples." % 'five'
print(x)
#I eat 3 apples.


#숫자값을 나타내는 변수로 대입
number = 33
c = "I eat %d apple." % number
print(c)
#I eat 3 apples

#2개 이상 값 넣기
numbe = 99
doy = "three"
print("I ate %d apples. so I was sick for %s days." %(numbe, doy))
#I ate 99 apples. so I was sick for three days.

"""
문자열 포맷 코드
%s 문자열(String)
%c 문자 1개(character)
%d 정수(Integer)
%f 부동 소수 (Floating-point)
%o 8진수
%x 16진수
%% Literal % (문자 '%' 자체)

%s는 자동으로 %뒤에 있는 값을 문자열로 바꾸므로 어떤 형태의 값이든 변환해 넣을수 있음
"""

#포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
print("Error is %d%%." % 98)
#Error is 98%.


print("-"*77) #구분선


#정렬과 공백
print("%10s" % "hi")
#'        hi'  "%10s"의 의미는 전체 길이가 10개인 문자열 공간에 hi를 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨두라는 의미

print("%-10sjane." % 'hi')
#hi        jane. hi를 왼쪽으로 정렬하고 나머지는 공백으로 채움


#소수점 표현하기
print("%0.4f" % 3.42134234)
#3.4213  // 3.42134234를 소수점 네번짜 자리까지만 나타내고 싶은 경우 위와같이 사용 0.4f에 숫자4는 소수점 뒤에 나올 숫자의 개수이다

print("\'%10.4f\'" % 3.42134234)
#'    3.4213' 3.42134234를 소수점 네번짜 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에 오른쪽으로 정렬


print("-"*77) #구분선


#문자 개수 세기 (count)
aa = "hobby"
print(aa.count('b'))
#문자열 중 문자 b의 개수를 반환함

print("-"*77) #구분선

#위치 알려주기1(find)
aaa = 'Python is best choice'
print(aaa.find('b')) #10 문자열 중 문자b가 처음으로 나온 위치를 반환함
print(aaa.find('k')) #-1 만약 찾는 문자나 문자열이 존재하지 않는다면 -1 반환함

#위치 알려주기2(index)
ㅁ = 'Life is too  short'
print(ㅁ.index('t'))
#문자열 중 문자t가 맨처음으로 나온 위치를 반환. 찾는 문자나 문자열이 존재하지 않는다면 오류 발생

#문자열 삽입(join)
asdf = ","
print(asdf.join('abcd'))

#소문자를 대문자로 바꾸기(upper)
zz = "hi"
print(zz.upper())

#대문자를 소문자로 바꾸기(lower)
qw = "HI"
print(qw.lower())

#왼쪽 공백 지우기
qe = "   hi   "
print(qe.lstrip())

#오른쪽 공백 지우기
print(qe.rstrip())

#양쪽 공백 지우기(strip)
print(qe.strip())

#문자열 바꾸기 (replace)
pp = "Life is too shrot"
print(pp.replace("Life", "Your leg"))
'''Your leg is too shrot    replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 내의 특정한 값을 다른값으로 치환해줌
'''

#문자열 나누기 (split)
print(pp.split()) #공백을 기준으로 문자열 나눔

qp = "a:b:c:d"
print(qp.split(':')) #기호를 기준으로 문자열 나눔


print("-"*77) #구분선


#고급 문자열 포매팅
#숫자 바로 대입
print("I eat {0} apples." .format(3))
#{0}부분이 숫자3으로 바뀜 I eat 3 apples.

#문자열 바로 대입
print("I eat {0} apples.".format("five"))
#{0}부분이 문자열 five로 바뀜 I eat five apples.

#숫자값을 가진 변수로 대입
넘버 = 333
print("I eat {0} apples.".format(넘버))
#I eat 333 apples. 문자열 {0} 항목이 number 변수의 값인 333으로 바뀜


#2개 이상의 값 넣기
넘바 = 100
데이 = "삼일"
print("I ate {0} apples. so I was sick for {1} days.".format(넘바, 데이))
"""
I ate 100 apples. so I was sick for 삼일 days.
2개 이상의 값을 넣을땐 문자열의 {0}, {1}과 같은 인덱스 항목들이 format 함수의 입력값들로 순서에 맞게 바뀜
{0}은 format 함수의 처음 입력값인 넘바로 바뀌고 {1}은 format 함수의 두번째 입력값인 데이로 바뀜
"""

#이름으로 넣기
print("I ate {nu} apples. so I was sick for {de} days.".format(nu=10, de=32))
'''
I ate 10 apples. so I was sick for 32 days.
{name}형태를 이용할 경우 format 함수의 입력값에 반드시 name=value와 같은 형태의 입력값이 있어야한다 
위 예의 문자열의 {nu},{de}가 format 함수의 입력값인 nu=10, de=32값으로 바뀌는것을 보여줌
'''

#인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {de} days.".format(11, de=324))
#I ate 11 apples. so I was sick for 324 days.  인덱스 항목과 name=value 형태를 혼용하는것도 가능

#왼쪽정렬
print("{0:<10}".format("hi"))
# "hi        "  ||| :<10표현식을 이용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

#오른쪽 정렬
print("{0:>10}".format("hi"))
# "         hi" 오른쪽 정렬은 :< 대신 :>을 이용하면 됨. 화살표 방향으로 정렬된다고 생각하면된다

#가운데 정렬
print("{0:^10}".format("hi"))
# '    hi    '    :^ 기호를 이용해 가운데 정렬도 가능



print("-"*77) #구분선


#공백 채우기
print("{0:=^10}".format("hi")) #====hi====
print("{0:!<10}".format("hi")) #hi!!!!!!!!
"""
정렬시 공백문자 대신 지정한 문자값으로 채워 넣는것도 가능. 채워 넣을 문자값은 정렬 문자인 <,>,^바로 앞에 넣어야 한다
"""

#소수점 표현
yy = 3.141592
print("{0:0.4f}".format(yy)) #3.1416
#format 함수를 이용해 소수점을 4자리까지만 표현하는 방법을 보여둔다 0.4f
print("{0:10.4f}".format(yy)) #'    3.1416'
#자릿수를 10으로도 맞추수 있다 10.f
print("{0:@<10.4f}".format(yy)) #'3.1416@@@@'

#'{'또는 '}'문자 표현하기
print("{{ and }}".format()) #{ and }
"""
foramt 함수를 이용해 문자열 포매팅 할 경우 { and }와 같은 중괄호(brace) 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은
경우에는 위 예의 {{ and }}처럼 2개를 연속해서 사용하면 된다
"""
