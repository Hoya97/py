#if문
돈 = 1
if 돈:
    print("택시")
else:
    print("도보")
#택시 #돈에 입력된 1은 참 따라서 if문 다음의 문장이 수행되 "택시"가 출력된다
"""조건문이 참이면 if문 다음의 문장(if블록)들을 수행하고 거짓이면 else문 다음의 문장(else블록)들을 수행하게 되므로 
else문은 독립적으로 사용할수 없다"""

#들여쓰기
""" 
if문을 만들 때는 if 조건문: 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)를 해줘야 한다.
if 조건문:
    수행문장1
    수행문장2
    수행문장3
들여쓰기를 안할시 오류 
들여쓰기는 2가지를 혼용해서 쓰지말자
조건문 다음에 콜론(:) {whole,for,def,class문에도 포함}
"""

#조건문이란?
"""
if 조건문에서 조건문이란 참과 거짓을 판단하는 문장
숫자형에서 거짓은0 참은 0이 아닌 숫자이다. 문자열 리스트 튜플 딕셔너리는 공백이면 거짓이다
"""

print("="*50)#구분선

#비교연산자(<,>,==,!=,<=,>=)
"""
x < y   :x가 y보다 작다
x > y   :x가 y보다 크다
x == y  :x와 y가 같다
x != y  :x와 y가 같지않다
x >= y  :x가 y보다 크거나 같다
x <= y  :x가 y보다 작거나 같다
"""
x = 3
y = 2
print(x > y) #True  #조건문 참
print(x < y) #False #조건문이 거짓
print(x == y)#False #같지않다 거짓
print(x != y)#True  #같지 않기에 참

돈 = 2000
if 돈 >= 3000:
    print("택시를 타고 가세요")
else:
    print("걸어가세요")
#걸어가세요


print("="*50)#구분선

#and,or,not
"""
x or y  :x와 y 둘 중 하나만 참이면 참이다 
x and y :x와 y 모두 참이어야 참이다
not x   :x가 거짓이면 참이다
"""


#x in s,x not in s
"""
x in 리스트      x not in 리스트
x in 튜플        x not in 튜플
x in 문자열      x not in 문자열
"""

print(1 in [1,2,3]) #True #1이 [1,2,3] 안에 있는가?
print(1 not in [1,2,3])#False #1이 [1,2,3]안에 없는가?

주머니 = ['종이','휴대전화','돈'] #주머니 안에 종이 휴대전화 돈이있다
if '돈' in 주머니:
    print("버스를 타라")
else:
    print("걸어가라")
#버스를 타라

print("="*50)#구분선

#조건문에 아무 일도 하지않게 하기
주머니 = ['종이','휴대전화','돈']
if '돈' in 주머니:
    pass
else:
    print("카드를 꺼내라")
#주머니 안에 돈이 있기에 if문 다음 문장인 pass가 수행되고 아무런 결과값도 보여주지 않는다


#다양한 조건을 판단하는 elif
"""
주머니에 돈이 있으면 택시를 타고 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라
"""
#if와 else만으로 표현
pocket = ['paper','cellphone'] #주머니 안에 종이, 휴대전화가 있다.
card = 1 #카드를 가지고 있다.
if 'money' in pocket:
    print("택시타세요")
else:
    if card:
        print("택시타세요")
    else:
        print("걸어가세요")
#택시타세요
#elif 사용
pocket = ['paper','cellphone']
card = 1
if 'money' in pocket: #주머니에 돈이 있으면
    print("택시타요")
elif card: #주머니에 돈이 없고 카드가 있으면
    print("택시타요")
else: #주머니에 돈도 없고 카드도 없으면
    print("걸어가요")
#택시타요
print("="*50)#구분선

#elif는 이전 조건문이 거짓일 때 수행 된다
#if,elif,else를 모두 사용할 때 기본 구조
"""
if 조건문:
    수행할 문장 1-1
    수행할 문장 1-2
    ...
elif 조건문2:
    수행할 문장2-1
    수행할 문장2-2
    ...
...
elif 조건문N:
    수행할 문장N-1
    수행할 문장N-2
    ...
...
else:
    수행할 문장A
    수행할 문장B
    ...
"""

#if문 한 줄 작성
pocket = ['paper','cellphone']
if 'money' in pocket:
    print("버스타요")
else:
    pass
#if문  다음에 수행 문장이 한줄이고 else문 다음 수행문장도 한줄이다.
pocket = ['paper','cellphone']
if 'money' in pocket: print("버스타요")
else: pass
#if문 다음의 수행문장을 콜론(:) 바로 뒤에 적었다.else문 역시 같다.
